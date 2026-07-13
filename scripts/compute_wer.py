"""
Word Error Rate (WER) Computation Script
==========================================
Computes WER between expected (reference) transcripts and ASR outputs.

Usage:
    1. Edit the SAMPLES list below with your reference and ASR transcripts
    2. Run: python compute_wer.py

Requirements:
    pip install jiwer
"""

import os
import sys
import json

try:
    from jiwer import wer, cer
except ImportError:
    print("ERROR: jiwer not installed.")
    print("Run: pip install jiwer")
    sys.exit(1)


# ── Edit These With Your Actual Transcripts ────────────────────────────────────
#
# After running Whisper and Google Speech-to-Text, fill in the transcripts below.
# The reference is what was actually said (ground truth).
# The hypothesis is what the ASR system output.

SAMPLES = [
    {
        "name": "Sample 1 - News reading",
        "reference":  "salut mon frère j'espère que vous allez bien bienvenue dans notre classe de science des données",
        "whisper":    "salut mon frere, j'espere que vous allez bien. Bienvenue dans notre classe de science des donnees.",
        "google":     "salut mon frère j'espère que vous allez bien bienvenue dans notre classe de science de données",
    },
    {
        "name": "Sample 2 - Casual speech",
        "reference":  "ici on apprend le langage naturel en apprenant les données vocales et on les convertit en texte",
        "whisper":    "Ici, on apprend le langage naturel en apprenant les données vocales et on les converti en texte.",
        "google":     "ici on apprend le langage naturel en apprennant les données vocales et on les convertit en texte",
    },
    {
        "name": "Sample 3 - Liaisons",
        "reference":  "on sait que la langue française a des problèmes de liaisons et d'accords et ça peut causer des problèmes à notre modèle d'apprentissage automatique",
        "whisper":    "On sait que la langue francaise a des problem des liasons et d'accord et ca peut causer des problem a notres model de l'apprentissage de machine.",
        "google":     "on sait que la langue française a des problèmes de liaisons et d'accord et ça peut causer des problèmes à notre modèle de l'apprentissage de machine",
    },
    {
        "name": "Sample 4 - Numbers/names",
        "reference":  "j'espère que cette explication va vous donner des clarifications sur le projet en cours et que vous comprenez les difficultés de convertir les audios en texte",
        "whisper":    "j'espere que cette explication va vous donner des clarifications sur le projet en main et que vous comprenez les difficultes de converture les audio en text.",
        "google":     "j'espère que cette explication va vous donner des clarifications sur le projet en main et que vous comprenez les difficultés de convertir les audios en texte",
    },
    {
        "name": "Sample 5 - Noisy speech",
        "reference":  "merci pour votre attention ici le groupe numéro cinq et j'espère que le message est utile",
        "whisper":    "Merci pour votre attention, ici group numero 5 et j'espere que le message est utile.",
        "google":     "merci pour votre attention ici le groupe numéro 5 et j'espère que le message est utile",
    },
]


# ── WER Computation ───────────────────────────────────────────────────────────

def compute_wer_results():
    results_dir = os.path.join(os.path.dirname(__file__), "..", "results")
    os.makedirs(results_dir, exist_ok=True)

    print("=" * 70)
    print("Word Error Rate (WER) Analysis — French ASR")
    print("=" * 70)

    whisper_wers = []
    google_wers = []
    all_results = []

    for sample in SAMPLES:
        name = sample["name"]
        ref = sample["reference"].strip()
        hyp_w = sample["whisper"].strip()
        hyp_g = sample["google"].strip()

        # Skip empty entries
        if not ref:
            print(f"\n⚠  {name}: No reference transcript provided, skipping.")
            continue

        print(f"\n{'─' * 70}")
        print(f"  {name}")
        print(f"{'─' * 70}")
        print(f"  Reference: {ref}")

        result_entry = {"name": name, "reference": ref}

        # Whisper WER
        if hyp_w:
            w_wer = wer(ref.lower(), hyp_w.lower())
            w_cer_val = cer(ref.lower(), hyp_w.lower())
            whisper_wers.append(w_wer)
            print(f"  Whisper:   {hyp_w}")
            print(f"  → WER: {w_wer:.1%}  |  CER: {w_cer_val:.1%}")
            result_entry["whisper_output"] = hyp_w
            result_entry["whisper_wer"] = round(w_wer * 100, 1)
            result_entry["whisper_cer"] = round(w_cer_val * 100, 1)
        else:
            print(f"  Whisper:   (no output provided)")

        # Google WER
        if hyp_g:
            g_wer = wer(ref.lower(), hyp_g.lower())
            g_cer_val = cer(ref.lower(), hyp_g.lower())
            google_wers.append(g_wer)
            print(f"  Google:    {hyp_g}")
            print(f"  → WER: {g_wer:.1%}  |  CER: {g_cer_val:.1%}")
            result_entry["google_output"] = hyp_g
            result_entry["google_wer"] = round(g_wer * 100, 1)
            result_entry["google_cer"] = round(g_cer_val * 100, 1)
        else:
            print(f"  Google:    (no output provided)")

        all_results.append(result_entry)

    # Summary
    print(f"\n{'=' * 70}")
    print("SUMMARY")
    print(f"{'=' * 70}")

    if whisper_wers:
        avg_w = sum(whisper_wers) / len(whisper_wers)
        print(f"  Whisper Average WER: {avg_w:.1%}  ({len(whisper_wers)} samples)")
    else:
        print("  Whisper: No results to compute.")

    if google_wers:
        avg_g = sum(google_wers) / len(google_wers)
        print(f"  Google  Average WER: {avg_g:.1%}  ({len(google_wers)} samples)")
    else:
        print("  Google: No results to compute.")

    if whisper_wers and google_wers:
        if avg_w < avg_g:
            print(f"\n  → Whisper performed better by {(avg_g - avg_w):.1%} WER")
        elif avg_g < avg_w:
            print(f"\n  → Google performed better by {(avg_w - avg_g):.1%} WER")
        else:
            print(f"\n  → Both systems performed equally")

    # Save results
    json_path = os.path.join(results_dir, "wer_results.json")
    summary = {
        "samples": all_results,
        "whisper_avg_wer": round(sum(whisper_wers) / len(whisper_wers) * 100, 1) if whisper_wers else None,
        "google_avg_wer": round(sum(google_wers) / len(google_wers) * 100, 1) if google_wers else None,
    }
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"\n  Results saved to: {json_path}")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    # Check if any samples have data
    has_data = any(s["reference"].strip() for s in SAMPLES)
    if not has_data:
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║  No transcript data filled in yet!                         ║")
        print("║                                                            ║")
        print("║  To use this script:                                       ║")
        print("║  1. Record your French audio samples                       ║")
        print("║  2. Run evaluate_whisper.py to get Whisper transcripts      ║")
        print("║  3. Run Google Speech-to-Text on the same samples          ║")
        print("║  4. Edit the SAMPLES list in this file with:               ║")
        print("║     - reference (what was actually said)                    ║")
        print("║     - whisper (Whisper output)                             ║")
        print("║     - google (Google output)                               ║")
        print("║  5. Run this script again                                  ║")
        print("╚══════════════════════════════════════════════════════════════╝")
    else:
        compute_wer_results()
