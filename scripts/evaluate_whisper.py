"""
Whisper ASR Evaluation Script for French
=========================================
Runs OpenAI Whisper (tiny model, ~39MB) on all audio files in ../audio_samples/
Outputs transcriptions to ../results/

Usage:
    python evaluate_whisper.py

Requirements:
    pip install openai-whisper
    ffmpeg must be installed and in PATH
"""

import os
import sys
import json
import glob
import time

# Check for whisper availability
try:
    import whisper
except ImportError:
    print("ERROR: openai-whisper not installed.")
    print("Run: pip install openai-whisper")
    sys.exit(1)


# ── Configuration ──────────────────────────────────────────────────────────────

MODEL_NAME = "tiny"          # ~39MB, fast on CPU
LANGUAGE = "fr"              # French
AUDIO_DIR = os.path.join(os.path.dirname(__file__), "..", "audio_samples")
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "..", "results")
SUPPORTED_EXTENSIONS = (".wav", ".mp3", ".m4a", ".flac", ".ogg", ".webm", ".mp4")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    # Resolve paths
    audio_dir = os.path.abspath(AUDIO_DIR)
    results_dir = os.path.abspath(RESULTS_DIR)
    os.makedirs(results_dir, exist_ok=True)

    # Find audio files
    audio_files = []
    for ext in SUPPORTED_EXTENSIONS:
        audio_files.extend(glob.glob(os.path.join(audio_dir, f"*{ext}")))
    audio_files.sort()

    if not audio_files:
        print(f"No audio files found in: {audio_dir}")
        print(f"Supported formats: {', '.join(SUPPORTED_EXTENSIONS)}")
        print("\nPlease record 5-6 short French audio clips (10-30 seconds each)")
        print("and place them in the audio_samples/ directory.")
        sys.exit(1)

    print(f"Found {len(audio_files)} audio file(s) in {audio_dir}")
    print(f"Model: Whisper {MODEL_NAME}")
    print(f"Language: {LANGUAGE}")
    print("-" * 60)

    # Load model (downloads ~39MB on first run)
    print(f"\nLoading Whisper '{MODEL_NAME}' model...")
    model = whisper.load_model(MODEL_NAME)
    print("Model loaded successfully.\n")

    # Process each audio file
    all_results = []

    for i, audio_path in enumerate(audio_files, 1):
        filename = os.path.basename(audio_path)
        print(f"[{i}/{len(audio_files)}] Transcribing: {filename}")

        start_time = time.time()

        # Run Whisper
        result = model.transcribe(
            audio_path,
            language=LANGUAGE,
            fp16=False,         # CPU mode — must be False
            verbose=False
        )

        elapsed = time.time() - start_time

        transcript = result["text"].strip()
        print(f"  → Transcript: {transcript}")
        print(f"  → Time: {elapsed:.1f}s")
        print()

        # Store result
        entry = {
            "file": filename,
            "transcript": transcript,
            "language": result.get("language", LANGUAGE),
            "duration_seconds": elapsed,
            "segments": [
                {
                    "start": seg["start"],
                    "end": seg["end"],
                    "text": seg["text"]
                }
                for seg in result.get("segments", [])
            ]
        }
        all_results.append(entry)

        # Save individual transcript
        txt_path = os.path.join(results_dir, f"{os.path.splitext(filename)[0]}_whisper.txt")
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(transcript)

    # Save all results as JSON
    json_path = os.path.join(results_dir, "whisper_results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    print("=" * 60)
    print(f"All transcriptions saved to: {results_dir}")
    print(f"Combined results: {json_path}")
    print(f"Total files processed: {len(all_results)}")
    print("\nNext steps:")
    print("  1. Also run these samples through Google Speech-to-Text at:")
    print("     https://speech.google.com")
    print("  2. Screenshot the Google results and save to screenshots/")
    print("  3. Run compute_wer.py to calculate Word Error Rates")


if __name__ == "__main__":
    main()
