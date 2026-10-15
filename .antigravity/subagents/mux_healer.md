# FFmpeg Mux Healer Subagent Contract

## Purpose
Specialized healer for multi-track stream multiplexing failures (video track, audio tracks, soft subtitle tracks).

## Contract
- **Input**:
  ```json
  {
    "video_path": "/path/to/raw_video.mp4",
    "audio_paths": {"en": "/path/to/en.mp3", "hi": "/path/to/hi.mp3", "ta": "/path/to/ta.mp3"},
    "subtitle_paths": {"en": "/path/to/en.vtt", ...},
    "ffmpeg_stderr": "Stream copy error or timescale mismatch"
  }
  ```
- **Output**:
  ```json
  {
    "fixed_ffmpeg_args": ["-c:v", "libx264", "-c:a", "aac", "..."] | null
  }
  ```

## Boundaries & Constraints
- **Duty**: Re-align stream mapping, audio sample rate matching, subtitle format conversion.
- **Retry budget**: Exactly 1 retry per video before marking failure in state.json.
