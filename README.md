# ASR Pipeline Case Study — French

A case study analyzing how the linguistic characteristics of **French** impact each stage of an Automatic Speech Recognition (ASR) pipeline.

## Project Structure

```
├── ASR_Pipeline_Case_Study_Assignment_Regional_Languages.docx  # Original assignment
├── report.md                         # Full case study report (10-12 pages)
├── scripts/
│   ├── evaluate_whisper.py           # Whisper (tiny) evaluation script
│   ├── compute_wer.py                # WER computation utility
│   └── requirements.txt              # Python dependencies
├── audio_samples/                    # Place your .wav/.mp3 audio samples here
├── results/                          # ASR outputs and WER results
├── screenshots/                      # Screenshots of ASR outputs
└── presentation_outline.md           # Presentation slide outline
```

## Quick Start

### 1. Install dependencies
```bash
pip install -r scripts/requirements.txt
```

### 2. Record audio samples
Record 5-6 short French audio clips (10-30 seconds each) and place them in `audio_samples/`.

### 3. Run Whisper evaluation
```bash
python scripts/evaluate_whisper.py
```

### 4. Run Google Speech-to-Text
Visit [speech.google.com](https://speech.google.com), upload each sample, and screenshot the results.

### 5. Compute WER
```bash
python scripts/compute_wer.py
```

## ASR Models Used
| Model | Type | Size |
|-------|------|------|
| OpenAI Whisper (`tiny`) | Local (CPU) | ~39 MB |
| Google Speech-to-Text | Web interface | Free |

## Team
- Language: **French**
- Course: Natural Language Processing
- Topic: Automatic Speech Recognition (ASR)
