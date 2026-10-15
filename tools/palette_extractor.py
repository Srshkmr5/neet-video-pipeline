"""
Palette & Aesthetic Extractor Tool
Analyzes reference keyframes and extracts dominant color palettes, contrast ratios,
and Manim theme dictionary presets.
"""

from pathlib import Path
from typing import List, Dict, Any, Tuple
import numpy as np
from PIL import Image
import json
import sys

def rgb_to_hex(rgb: Tuple[int, int, int]) -> str:
    return f"#{int(rgb[0]):02X}{int(rgb[1]):02X}{int(rgb[2]):02X}"

def get_luminance(rgb: np.ndarray) -> float:
    # Relative luminance standard formula
    return 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]

def get_saturation(rgb: np.ndarray) -> float:
    r, g, b = rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin
    if cmax == 0:
        return 0
    return delta / cmax

def kmeans_quantize(pixels: np.ndarray, k: int = 5, max_iters: int = 15) -> Tuple[np.ndarray, np.ndarray]:
    """Lightweight K-Means clustering using numpy without external ML dependencies."""
    np.random.seed(42)
    indices = np.random.choice(len(pixels), k, replace=False)
    centers = pixels[indices].astype(float)
    
    for _ in range(max_iters):
        # Distances to all centers
        dists = np.linalg.norm(pixels[:, np.newaxis] - centers, axis=2)
        labels = np.argmin(dists, axis=1)
        
        new_centers = []
        for i in range(k):
            cluster_pts = pixels[labels == i]
            if len(cluster_pts) > 0:
                new_centers.append(cluster_pts.mean(axis=0))
            else:
                new_centers.append(centers[i])
        new_centers = np.array(new_centers)
        if np.allclose(centers, new_centers, atol=1.0):
            break
        centers = new_centers
        
    counts = np.bincount(labels, minlength=k)
    return centers, counts

def extract_palette_from_images(image_paths: List[Path], k: int = 6) -> Dict[str, Any]:
    all_pixels = []
    for p in image_paths:
        img = Image.open(p).convert("RGB")
        # Downsample for fast clustering
        img.thumbnail((120, 80))
        arr = np.array(img).reshape(-1, 3)
        all_pixels.append(arr)
        
    pixels = np.vstack(all_pixels)
    centers, counts = kmeans_quantize(pixels, k=k)
    
    # Sort clusters by frequency
    sorted_idx = np.argsort(-counts)
    centers = centers[sorted_idx]
    counts = counts[sorted_idx]
    
    # Classify colors
    # Dominant background is usually the most frequent or lowest/highest luminance
    # Let's inspect frequency & saturation
    bg_cand = centers[0]
    bg_lum = get_luminance(bg_cand)
    is_dark_theme = bg_lum < 128
    
    # Text color: highest contrast with bg
    contrast_scores = [abs(get_luminance(c) - bg_lum) for c in centers]
    text_idx = int(np.argmax(contrast_scores))
    text_cand = centers[text_idx]
    
    # If text candidate contrast is too low, supply clean readable contrast
    if abs(get_luminance(text_cand) - bg_lum) < 80:
        text_cand = np.array([245, 245, 245]) if is_dark_theme else np.array([15, 23, 42])

    # Accents: high saturation + adequate luminance contrast with background
    accents = []
    for idx, c in enumerate(centers):
        if idx == 0 or idx == text_idx:
            continue
        c_lum = get_luminance(c)
        c_contrast = abs(c_lum - bg_lum)
        if c_contrast >= 50:  # Must be visible against background
            score = get_saturation(c) * 1.5 + (c_contrast / 255.0)
            accents.append((score, c))
        
    accents.sort(key=lambda x: -x[0])
    accent_colors = [a[1] for a in accents]
    
    # Modern educational palette fallbacks if image had low chroma
    vibrant_dark_defaults = [
        np.array([56, 189, 248]),   # Cyan #38BDF8
        np.array([245, 158, 11]),   # Amber #F59E0B
        np.array([16, 185, 129]),   # Emerald #10B981
    ]
    vibrant_light_defaults = [
        np.array([2, 132, 199]),    # Deep Sky #0284C7
        np.array([217, 119, 6]),    # Dark Amber #D97706
        np.array([5, 150, 105]),    # Dark Green #059669
    ]
    defaults = vibrant_dark_defaults if is_dark_theme else vibrant_light_defaults
    
    while len(accent_colors) < 3:
        accent_colors.append(defaults[len(accent_colors)])
        
    theme = {
        "is_dark_theme": bool(is_dark_theme),
        "background": rgb_to_hex(bg_cand),
        "text_primary": rgb_to_hex(text_cand),
        "accent_primary": rgb_to_hex(accent_colors[0]),
        "accent_secondary": rgb_to_hex(accent_colors[1]),
        "accent_tertiary": rgb_to_hex(accent_colors[2]),
        "all_palette": [rgb_to_hex(c) for c in centers]
    }
    
    return theme

if __name__ == "__main__":
    if len(sys.argv) > 1:
        paths = [Path(p) for p in sys.argv[1:]]
        th = extract_palette_from_images(paths)
        print(json.dumps(th, indent=2))
    else:
        print("Usage: python tools/palette_extractor.py <image1.png> [image2.png ...]")
