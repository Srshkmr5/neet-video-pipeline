"""
Emergent Pacing Engine for NEET UG Video Pipeline
Derived from MASTER_BLUEPRINT.md v1.1 Section 4
"""
from typing import Dict, List, Any
from config import TIER_HOLD_TIMES

class PacingEngine:
    @staticmethod
    def calculate_beat_duration(tier: str, narration_duration: float, repeat_count: int = 1) -> float:
        """
        Duration formula:
        beat_duration = narration_audio_duration + visual_hold + repetition_passes
        """
        hold = TIER_HOLD_TIMES.get(tier, 1.5)
        # Settle & release have fixed minimal holds regardless of narration
        if tier == "settle":
            return max(narration_duration + 2.0, hold)
        elif tier == "release":
            return max(narration_duration + 2.5, hold)
        elif tier == "critical":
            # Critical repetition multiplier
            repetition_passes = (repeat_count - 1) * 1.5
            return narration_duration + hold + repetition_passes
        else:
            return narration_duration + hold

    @staticmethod
    def compute_total_video_duration(beat_durations: List[float]) -> float:
        return sum(beat_durations)

    @staticmethod
    def derive_length_badge(total_seconds: float) -> str:
        """
        Length badge (derived, not authored):
          Green  : < 3 min (180s)
          Orange : 3-8 min (180s - 480s)
          Red    : > 8 min (480s+)
        """
        if total_seconds < 180:
            return "Green (< 3 min)"
        elif total_seconds <= 480:
            return "Orange (3-8 min)"
        else:
            return "Red (> 8 min)"

    @staticmethod
    def estimate_batch_schedule(nodes: List[Any], template_registry: Dict[str, Any], quality: str = "draft") -> Dict[str, Any]:
        """
        Calculates estimated batch rendering time and disk requirements,
        accounting for 2D vs 3D render_time_multiplier.
        """
        # Baseline render seconds per node
        base_render_sec = 30.0 if quality == "draft" else 90.0

        total_nodes = len(nodes)
        count_2d = 0
        count_3d = 0
        total_render_seconds = 0.0

        for node in nodes:
            if isinstance(node, dict):
                template_name = node.get("templateName", "")
            else:
                template_name = getattr(node, "templateName", "")
            reg_entry = template_registry.get(template_name, {})
            dimension = reg_entry.get("dimension", "2d")
            multiplier = float(reg_entry.get("render_time_multiplier", 3.5 if dimension == "3d" else 1.0))

            if dimension == "3d":
                count_3d += 1
            else:
                count_2d += 1

            total_render_seconds += base_render_sec * multiplier

        # Disk estimates (MB)
        # 2D: ~35 MB per node (raw + audio + muxed)
        # 3D: ~80 MB per node
        est_disk_mb = (count_2d * 35.0) + (count_3d * 80.0)

        return {
            "total_nodes": total_nodes,
            "count_2d": count_2d,
            "count_3d": count_3d,
            "estimated_render_seconds": total_render_seconds,
            "estimated_render_hours": total_render_seconds / 3600.0,
            "estimated_disk_mb": est_disk_mb,
            "estimated_disk_gb": est_disk_mb / 1024.0
        }
