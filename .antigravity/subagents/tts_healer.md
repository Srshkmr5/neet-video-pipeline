# TTS Healer Subagent Contract

## Purpose
Specialized healer for Text-to-Speech synthesis issues, rate limits, and phonetic distortions across English, Hindi, and Tamil.

## Contract
- **Input**:
  ```json
  {
    "lang": "en",
    "text": "When theta = 30 degrees, H_max = ...",
    "error": "Phonetic distortion or synthesis rejection"
  }
  ```
- **Output**:
  ```json
  {
    "normalized_text": "When theta equals thirty degrees, H max equals ...",
    "retry": true
  }
  ```

## Boundaries & Constraints
- **Duty**: Phonetic normalization (`\pi` -> "pie", `\theta` -> "theta", subscripts -> natural spoken terms).
- **Retry budget**: Up to 3 retries with exponential backoff on rate limits; skip language if persistent.
