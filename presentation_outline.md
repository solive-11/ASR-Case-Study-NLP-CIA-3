# Presentation Outline — French ASR Pipeline Analysis (15 minutes)

## Slide 1: Title Slide (30s)
- **Title:** ASR Pipeline Analysis for French
- Course: Natural Language Processing
- Team members, date

## Slide 2: Agenda (30s)
- Language Profile → Pipeline Analysis → Practical Evaluation → Recommendations

---

## Slide 3: Why French is Interesting for ASR (1 min)
- 310M+ speakers across 5 continents
- Rich vowel system with nasal vowels
- Extreme homophony — a unique challenge
- Significant dialect diversity (European, Canadian, African)

## Slide 4: French Language Profile (1.5 min)
- Script: Latin + diacritics (é, è, ê, ç, etc.)
- Key dialects: Metropolitan, Québécois, African, Belgian, Swiss
- Phonetics: 13-16 vowels, 4 nasal vowels, uvular /ʁ/
- Morphology: Rich verb conjugation, many silent inflections

---

## Slide 5: ASR Pipeline Overview (30s)
- Diagram: Speech → Pre-processing → Feature Extraction → Acoustic Model → Language Model → Decoding → Text

## Slide 6: Stage 1 — Speech Acquisition & Pre-processing (1.5 min)
- **Key challenge:** Liaison blurs word boundaries
- Example: "les amis" → /le.za.mi/ — where does one word end?
- Dialect diversity in recording conditions
- Technique: Multi-dialect training data, robust VAD

## Slide 7: Stage 2 — Feature Extraction (1.5 min)
- **Key challenge:** 4 nasal vowels + fine vowel contrasts
- French is one of the fastest spoken languages (~7.2 syll/sec)
- No lexical stress → prosody doesn't help word identification
- Technique: Self-supervised features (wav2vec 2.0)

## Slide 8: Stage 3 — Acoustic Modeling (1.5 min)
- **Key challenge:** Liaison pronunciation variants, dialect variation
- Table: Metropolitan vs. Québécois vs. African French differences
- Code-switching: French-English, French-Arabic
- Technique: Multi-dialect fine-tuning, end-to-end models

## Slide 9: Stage 4 — Language Modeling (2 min)
- **Key challenge:** EXTREME HOMOPHONY — the #1 French ASR problem
- Example: /vɛʁ/ → vers, vert, verre, ver, vair (5 words!)
- Spoken vs. written gap: "J'sais pas" vs. "Je ne sais pas"
- Technique: Subword tokenization, spoken-language LM, context-aware disambiguation

## Slide 10: Stage 5 — Decoding & Post-processing (1 min)
- **Key challenge:** Diacritic restoration ("ou" vs. "où")
- French punctuation: guillemets «», spacing before :;!?
- Technique: Neural diacritic restoration, French NER

---

## Slide 11: Practical Evaluation — Setup (30s)
- 2 ASR systems: Whisper (tiny, local) vs. Google STT (web)
- 5-6 audio samples testing specific challenges
- Metrics: WER per sample, error type classification

## Slide 12: Evaluation Results — Error Table (1.5 min)
- Show filled error analysis table
- Highlight most interesting errors (homophones, diacritics, liaisons)

## Slide 13: WER Comparison (1 min)
- Bar chart: Whisper vs. Google WER per sample
- Which system handled which challenge better?

---

## Slide 14: Recommendations (1 min)
- Top 3 improvements:
  1. Homophone disambiguation (biggest impact)
  2. Diacritic restoration
  3. Multi-dialect training data
- Future directions: personalized ASR, code-switching models

## Slide 15: Conclusion & Q&A (30s)
- French is uniquely challenging due to homophony + liaison + diacritics
- Modern end-to-end models help but don't solve everything
- Thank you + Questions
