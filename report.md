# ASR Pipeline Analysis for French

**Course:** Natural Language Processing  
**Topic:** Automatic Speech Recognition (ASR)  
**Assigned Language:** French  
**Team:** Justin, Mahamat, Olive 

---

## Part A — Language Profile

### 1. Script and Writing System

French uses the **Latin alphabet** consisting of 26 base letters, extended with a rich set of **diacritical marks** that are essential for correct pronunciation and meaning:

| Diacritic | Name | Examples | Function |
|-----------|------|----------|----------|
| Accent aigu (´) | Acute accent | é (café, résumé) | Indicates /e/ sound |
| Accent grave (`) | Grave accent | è, à, ù (mère, à, où) | Indicates /ɛ/ or distinguishes homophones |
| Accent circonflexe (^) | Circumflex | ê, â, î, ô, û (fête, hôpital) | Historical marker, sometimes modifies vowel quality |
| Tréma (¨) | Diaeresis | ë, ï, ü (Noël, naïf) | Indicates separate vowel pronunciation |
| Cédille (¸) | Cedilla | ç (français, garçon) | Makes 'c' pronounced /s/ before a, o, u |

Diacritics are **not optional** — they change meaning. For example, "ou" (or) vs. "où" (where), and "a" (has) vs. "à" (to/at). This is a critical challenge for ASR post-processing, as the system must correctly restore diacritics from speech where they are not audible.

French also features several **digraphs and trigraphs**: "ch" (/ʃ/), "ph" (/f/), "gn" (/ɲ/), "ou" (/u/), "eau" (/o/), "ain/ein" (/ɛ̃/). The orthography is notoriously complex — the same sound can be written many ways (e.g., /o/ can be spelled "o", "au", "eau", "ô", "ault"), and the same spelling can represent different sounds depending on context.

A distinctive feature of French orthography is the prevalence of **silent letters**, especially word-final consonants. In "petit" (/pəti/), "vous parlez" (/vu paʁle/), and "les enfants" (/le.z‿ɑ̃.fɑ̃/), many written consonants are not pronounced — unless a following word begins with a vowel, triggering **liaison**.

### 2. Number of Speakers

French is one of the most widely spoken languages in the world:

| Category | Estimate |
|----------|----------|
| Native speakers | ~80 million |
| Total speakers (L1 + L2) | ~310 million |
| Countries with official status | 29 countries |
| Continents | 5 (Europe, Africa, North America, South America, Oceania) |

French is an official language in France, Belgium, Switzerland, Canada, and 21 African nations. It is the **second most studied language** globally and a working language of the United Nations, the European Union, NATO, and the International Olympic Committee. The Organisation internationale de la Francophonie (OIF) projects over **700 million** French speakers by 2050, driven primarily by population growth in Sub-Saharan Africa.

### 3. Major Dialects

French exhibits significant dialectal variation, which poses challenges for ASR systems:

| Dialect | Region | Key Differences |
|---------|--------|----------------|
| **Metropolitan French (Standard)** | France (especially Paris/Île-de-France) | Reference variety; basis for most ASR training data |
| **Québécois (Canadian French)** | Quebec, Canada | Diphthongized vowels, affrication of /t,d/ before /i,y/ (e.g., "tu" → /tsy/), archaic vocabulary, distinct informal register ("joual") |
| **Acadian French** | New Brunswick, Nova Scotia, Canada | Preserved archaic features, distinct vowel system |
| **Belgian French** | Belgium (Wallonia, Brussels) | "Septante" (70), "nonante" (90) instead of "soixante-dix", "quatre-vingt-dix"; pronunciation of "w" as /w/ not /v/ |
| **Swiss French** | Western Switzerland | "Huitante" (80), meal-time vocabulary differences ("dîner" = lunch), slower speech rate |
| **West African French** | Senegal, Côte d'Ivoire, Cameroon, etc. | Simplified vowel system, influence of local languages on prosody and phonology, code-mixing |
| **Maghreb French** | Morocco, Algeria, Tunisia | Influence of Arabic phonology, frequent French-Arabic code-switching |

The dialectal variation in **vowel systems** is particularly significant for ASR. Standard Metropolitan French maintains fine distinctions (e.g., /a/ vs. /ɑ/, /ɛ̃/ vs. /œ̃/) that are merging or absent in other varieties.

### 4. Phonetic Characteristics

French has a phoneme inventory that presents several unique challenges for ASR:

**Vowels (13–16 depending on dialect):**

| Type | Phonemes | Examples |
|------|----------|----------|
| Oral front unrounded | /i/, /e/, /ɛ/ | si, été, mère |
| Oral front rounded | /y/, /ø/, /œ/ | tu, peu, peur |
| Oral back | /u/, /o/, /ɔ/, /a/, (/ɑ/) | tout, beau, porte, patte, (pâte) |
| **Nasal vowels** | **/ɑ̃/, /ɛ̃/, /ɔ̃/, (/œ̃/)** | **dans, vin, bon, (brun)** |

The **four nasal vowels** are typologically unusual and represent a major challenge for ASR feature extraction. They require the system to distinguish nasalization as a phonemic feature, unlike English where nasalization is purely allophonic.

**Key Consonant Features:**
- **Uvular /ʁ/**: The French "r" is realized as a uvular fricative or approximant, varying from /ʁ/ to /χ/ across speakers and dialects.
- No aspiration of voiceless stops (unlike English).
- No retroflex or dental/alveolar contrast (unlike Hindi, Tamil).

**Suprasegmental Features Critical for ASR:**
- **Liaison**: A silent final consonant is pronounced when the next word begins with a vowel. E.g., "les amis" → /le.z‿a.mi/. This creates significant **word boundary ambiguity** for ASR.
- **Enchaînement**: A pronounced final consonant links to the next vowel-initial word. E.g., "une amie" → /y.na.mi/.
- **Elision**: Vowel deletion before another vowel. E.g., "le ami" → "l'ami" /la.mi/.
- **No lexical stress**: French uses **phrase-final stress** (accent on the last syllable of a phrase), unlike English's lexical stress. This means stress cannot help distinguish words.
- **Syllable-timed rhythm**: French syllables are roughly equal in duration, unlike the stress-timed rhythm of English.

### 5. Morphological Characteristics

French is a **moderately inflectional** language with significant implications for ASR:

**Verbal Morphology:**
French verbs conjugate for person (6 forms), number, tense (present, imperfect, future, past, conditional), mood (indicative, subjunctive, imperative), and voice. This creates hundreds of forms per verb. However, many forms are **homophones in speech**:

| Written Form | Pronunciation | Meaning |
|-------------|---------------|---------|
| je parle | /paʁl/ | I speak |
| tu parles | /paʁl/ | you speak |
| il parle | /paʁl/ | he speaks |
| ils parlent | /paʁl/ | they speak |
| parlé | /paʁle/ | spoken (past participle) |
| parler | /paʁle/ | to speak (infinitive) |
| parlais | /paʁlɛ/ | I/you was speaking |
| parlait | /paʁlɛ/ | he was speaking |
| parlaient | /paʁlɛ/ | they were speaking |

This massive **homophony** means the language model must do heavy disambiguation — the acoustic signal alone is insufficient.

**Nominal Morphology:**
- Two grammatical genders (masculine, feminine): "le livre" vs. "la table"
- Number marking: often silent in speech ("ami" /ami/ vs. "amis" /ami/)
- Articles and determiners agree in gender and number

**Derivational Morphology:**
- Productive prefixation and suffixation: "faire" → "refaire" → "défaire"
- Compound expressions: "pomme de terre" (potato), "chemin de fer" (railway) — multi-word units that must be handled by the language model

### 6. Common Applications of Speech Technology

French is well-served by speech technology due to its global reach:

- **Virtual Assistants**: Siri, Google Assistant, Alexa all support French with dialect-specific models
- **Dictation and Transcription**: Widely used in legal, medical, and business contexts in France, Belgium, Switzerland, and Canada
- **Call Center Automation**: IVR systems and conversational AI for telecom, banking, insurance
- **Broadcast Captioning**: Real-time subtitling for French television (France Télévisions, Radio-Canada)
- **Accessibility**: Screen readers, voice control for users with disabilities
- **Language Learning**: Apps like Duolingo, Babbel use French ASR for pronunciation evaluation
- **Automotive**: In-car voice commands (Renault, Peugeot, Citroën integrate French ASR)

---

## Part B — Pipeline Analysis

### Stage 1: Speech Acquisition and Pre-processing

#### Language-Specific Challenges

**1. Liaison and Word Boundary Ambiguity**

Liaison is the most significant pre-processing challenge for French ASR. When a word-final silent consonant is pronounced before a vowel-initial word, it creates acoustic continuity that obscures word boundaries:

- "les enfants" → /le.zɑ̃.fɑ̃/ — the /z/ bridges the two words
- "un homme" → /œ̃.nɔm/ — the /n/ links across the boundary
- "c'est un ami" → /sɛ.tœ̃.na.mi/ — multiple liaisons chain together

Without explicit word boundaries in the signal, the pre-processing stage cannot reliably segment the speech into word-level units. This problem is compounded by **enchaînement** (resyllabification across word boundaries), making French fundamentally harder to segment than languages with clear word boundaries.

**2. Dialect Diversity in Recording Conditions**

French is spoken across vastly different recording environments:
- Metropolitan France: urban noise, café ambiance, metro announcements
- Sub-Saharan Africa: outdoor environments, different microphone quality, crowd noise
- Quebec: cold-weather distortion (outdoor recording in winter), distinct ambient noise profiles

Speaker variability is extreme given the 310M+ speaker base. A system trained on Parisian French will encounter significant domain mismatch when processing Senegalese or Québécois speech.

**3. Register Variation**

French has a strong formal/informal distinction that affects speech patterns:
- Formal: "Je ne sais pas" (/ʒə nə sɛ pa/)
- Informal: "J'sais pas" or "Chais pas" (/ʃɛ pa/)

The informal register involves extensive reduction, deletion, and restructuring that dramatically changes the acoustic signal.

#### Impact on Recognition Accuracy

- Word boundary errors cascade through the pipeline, causing insertion and deletion errors
- Dialect mismatch can increase WER by 15-30% compared to matched conditions
- Register mismatch causes the model to encounter unseen acoustic patterns

#### Techniques to Overcome

- **Robust endpointing**: Use energy-based and neural VAD that doesn't rely on silence between words
- **Multi-condition training**: Include diverse noise types, recording conditions, and dialects
- **Data augmentation**: Speed perturbation, noise injection, room impulse response simulation
- **Dialect-tagged corpora**: Collect and label training data by dialect region

---

### Stage 2: Feature Extraction

#### Language-Specific Challenges

**1. Nasal Vowel Representation**

French's four nasal vowels (/ɑ̃/, /ɛ̃/, /ɔ̃/, /œ̃/) require the feature extraction system to capture nasalization as a distinctive feature. Standard **MFCCs** (Mel-Frequency Cepstral Coefficients) encode the spectral envelope, which does capture nasalization to some degree (nasal vowels have additional formants and anti-formants due to the nasal cavity). However, the contrast between oral and nasal vowel pairs (e.g., /a/ vs. /ɑ̃/, /ɛ/ vs. /ɛ̃/) can be subtle, especially at high speaking rates.

**2. Fine Vowel Distinctions**

French maintains several vowel contrasts that are merging in some dialects:
- /e/ vs. /ɛ/ ("été" vs. "est") — mid front unrounded
- /ø/ vs. /œ/ ("peu" vs. "peur") — mid front rounded
- /o/ vs. /ɔ/ ("beau" vs. "bol") — mid back rounded
- /a/ vs. /ɑ/ ("patte" vs. "pâte") — low vowels (merged in most modern speakers)

These distinctions require high spectral resolution in the feature extraction.

**3. High Syllable Rate**

French has one of the highest syllable rates among major languages (~7.2 syllables/second vs. ~6.2 for English). This means temporal features are compressed, and rapid transitions between phonemes must be captured. Standard frame rates (10ms shift) may not provide sufficient temporal resolution for the fastest speech.

**4. Phrase-Level Prosody**

French uses phrase-final stress rather than lexical stress. The only prosodic cue for word identity is at the phrase level, making it challenging for feature extraction to provide word-level prosodic information. Intonation is the primary cue for distinguishing statements from questions (e.g., "Il vient." vs. "Il vient?"), which must be captured.

#### Impact on Recognition Accuracy

- Nasal/oral vowel confusion leads to lexical errors (e.g., "banc" /bɑ̃/ vs. "bas" /ba/)
- Fine vowel contrasts lost at high speaking rates increase substitution errors
- Missing prosodic features impair sentence-type detection

#### Techniques to Overcome

- **Self-supervised features**: Use wav2vec 2.0 or HuBERT pre-trained on French data, which learn language-specific spectral patterns
- **Mel filterbank features**: Higher-dimensional (80-dim) log-mel filterbanks capture more spectral detail than 13-dim MFCCs
- **Prosodic features**: Extract F0 contour and energy envelope as auxiliary features for sentence-type classification
- **Shorter frame shift**: Use 5ms frame shift for fast speech segments

---

### Stage 3: Acoustic Modeling

#### Language-Specific Challenges

**1. Pronunciation Variation from Liaison**

Liaison creates context-dependent pronunciation variants that are not present in the base lexicon. The word "petit" is /pəti/ in isolation but /pətit/ in "petit ami". The acoustic model must learn these **allophonic rules** or have a pronunciation lexicon that includes liaison variants.

There are three types of liaison:
- **Obligatory**: Always pronounced (e.g., after determiners: "les amis" /lez‿ami/)
- **Optional**: Speaker-dependent (e.g., "pas encore" /paz‿ɑ̃kɔʁ/ or /pa ɑ̃kɔʁ/)
- **Forbidden**: Never pronounced (e.g., after "et": "et il" /e il/, never */et‿il/)

**2. Dialectal Acoustic Variation**

| Feature | Metropolitan French | Québécois | African French |
|---------|-------------------|-----------|---------------|
| /t,d/ before /i,y/ | [t], [d] | [ts], [dz] (affrication) | [t], [d] |
| Nasal vowels | 3-4 distinct | Diphthongized | Often merged |
| /ʁ/ | Uvular fricative | Uvular or alveolar | Variable |
| Vowel system | 13-16 vowels | Lax/tense distinction | Simplified (often 7-10) |

Models trained primarily on Metropolitan French show significant accuracy degradation on other varieties due to these systematic acoustic differences.

**3. Code-Switching**

Code-switching is prevalent in several French-speaking communities:
- **French-English** in Canada, business contexts, tech discourse ("J'ai fait un call pour le deadline")
- **French-Arabic** in Maghreb countries ("Il est parti fi dar" — He went to the house)
- **French-Local Language** in West Africa ("Je vais au marché acheter du thiéboudienne")

The acoustic model must handle mid-sentence language switches with potentially different phoneme inventories.

**4. Dataset Availability**

| Dataset | Type | Size | Dialect |
|---------|------|------|---------|
| Common Voice (French) | Read speech | ~900 hours | Mixed (mostly European) |
| LibriVox French | Audiobooks | ~1000 hours | European (formal) |
| ESTER/ESTER2 | Broadcast news | ~100 hours | European |
| REPERE | Broadcast (TV) | ~60 hours | European |
| African-accented French | Various | **Very limited** | African |
| Québécois corpora | Various | **Limited** | Canadian |

There is a significant **data imbalance** — European French is well-resourced while African and Canadian varieties are underrepresented, creating systematic bias in ASR performance.

#### Impact on Recognition Accuracy

- Liaison errors cause word boundary and word identity errors
- Dialect mismatch can increase WER by 15-30%
- Code-switched segments are often entirely mistranscribed
- Data imbalance means worse performance for already marginalized speaker populations

#### Techniques to Overcome

- **End-to-end models**: CTC/attention models (Whisper, wav2vec 2.0) implicitly learn pronunciation variants without a fixed lexicon
- **Multi-dialect fine-tuning**: Fine-tune pre-trained models on balanced multi-dialect data
- **Pronunciation lexicon expansion**: Add liaison variants to the pronunciation dictionary
- **Speaker adaptation**: Use x-vectors or i-vectors for per-speaker acoustic normalization
- **Multilingual models**: For code-switching, use models trained on multiple languages simultaneously

---

### Stage 4: Language Modeling

#### Language-Specific Challenges

**1. Extreme Homophony**

French has one of the highest rates of homophony among major languages. The language model bears an outsized burden for disambiguation:

| Pronunciation | Possible Written Forms |
|--------------|----------------------|
| /vɛʁ/ | vers (toward), vert (green), verre (glass), ver (worm), vair (squirrel fur) |
| /sɛ/ | c'est (it is), s'est (reflexive), ces (these), ses (his/her), sait (knows) |
| /paʁle/ | parlé (spoken), parler (to speak), parlais (was speaking), parlait (was speaking), parlaient (were speaking) |
| /o/ | au (to the), aux (to the, pl.), eau (water), haut (high), oh, os (bone, in some pronunciations) |
| /mɛʁ/ | mer (sea), mère (mother), maire (mayor) |

This means the language model must resolve ambiguity that in other languages would be handled by the acoustic signal. **Context is essential** — "le ver vert va vers le verre" (the green worm goes toward the glass) requires the LM to correctly assign each /vɛʁ/.

**2. Spoken vs. Written Language Gap**

The gap between spoken and written French is one of the largest among European languages:

| Feature | Written (Standard) | Spoken (Informal) |
|---------|-------------------|-------------------|
| Negation | "Je **ne** sais **pas**" | "Je sais pas" / "J'sais pas" / "Chais pas" |
| Questions | "**Est-ce que** tu viens?" | "Tu viens?" (intonation only) |
| Subject pronoun | "**Il** y a" | "Y'a" |
| Impersonal "on" | "**Nous** allons" | "**On** va" |
| Relative pronouns | "dont", "lequel" | Avoided, restructured |

If the language model is trained primarily on **written text** (news articles, books), it will poorly model spoken French patterns. This is a critical issue because most available text corpora are written, not transcriptions of speech.

**3. Morphological Richness and Vocabulary**

French verb conjugation creates a large vocabulary of surface forms:
- Regular verb "parler": ~50 distinct conjugated forms
- Irregular verb "être": ~30 forms
- Each adjective potentially has 4 forms: masc.sg, fem.sg, masc.pl, fem.pl

This **inflectional productivity** increases the effective vocabulary size and OOV (out-of-vocabulary) risk, especially for rare verb forms.

**4. English Borrowings**

French freely borrows English words, especially in technology, business, and youth culture:
- "le cloud computing", "le streaming", "le podcast", "le brunch"
- Often pronounced with French phonology: "parking" → /paʁ.kiŋ/, "weekend" → /wi.kɛnd/

These borrowings create vocabulary coverage challenges and potential pronunciation mismatches.

**5. Multi-Word Expressions**

French has many compound expressions and collocations that function as single units:
- "pomme de terre" (potato), "chemin de fer" (railway), "tout à fait" (absolutely)
- "c'est-à-dire" (that is to say), "peut-être" (maybe), "au fur et à mesure" (gradually)

The language model must treat these as units rather than independent words.

#### Impact on Recognition Accuracy

- Homophone disambiguation errors are the **single largest source of errors** in French ASR
- Written-language-biased LMs produce overly formal output that doesn't match spoken input
- OOV from morphological richness and English loans causes substitution errors

#### Techniques to Overcome

- **Subword tokenization**: BPE or SentencePiece to handle morphological richness and reduce OOV
- **Spoken language LM**: Train on transcriptions of spoken French, not just written text
- **Context-aware disambiguation**: Transformer-based LMs (GPT, BERT) for n-best rescoring with long context
- **Domain adaptation**: Fine-tune LM on domain-specific text (medical, legal, tech) for specialized ASR
- **Multi-word expression handling**: Include compound expressions in the vocabulary

---

### Stage 5: Decoding and Post-processing

#### Language-Specific Challenges

**1. Diacritic Restoration**

Since diacritics are not phonemically distinct in many cases (e.g., "a" /a/ vs "à" /a/ are identical in speech), the decoder must restore diacritics purely based on context:
- "ou" (or) vs. "où" (where)
- "a" (has) vs. "à" (to/at)
- "sur" (on) vs. "sûr" (sure)
- "du" (of the) vs. "dû" (owed)

Missing or incorrect diacritics change the meaning of the output and are perceived as errors by French readers.

**2. Homophone Resolution in Post-processing**

Even with a strong language model, some homophone errors persist and require post-processing correction:
- Grammar-based rules: "ses" (possessive) vs. "ces" (demonstrative) — determined by syntactic context
- Semantic disambiguation: "mère" vs. "mer" vs. "maire" — determined by topic/domain

**3. French-Specific Punctuation**

French has unique punctuation conventions that differ from English:
- Space **before** colon, semicolon, exclamation mark, and question mark: "Bonjour !"
- **Guillemets** (« ») instead of quotation marks: « Bonjour »
- Non-breaking spaces around guillemets and before double punctuation
- Decimal comma instead of decimal point: "3,14" instead of "3.14"

Punctuation restoration must follow these language-specific rules.

**4. Named Entity Challenges**

- Gendered titles: "M." (Monsieur), "Mme" (Madame), "Dr" (Docteur/Docteure)
- Accented proper names: "François", "Hélène", "Réunion" — diacritics must be correct
- Foreign names with French pronunciation: "Washington" → /wa.ʃiŋ.tɔn/
- Place names with articles: "Le Havre", "La Rochelle" — the article is part of the name

**5. Number and Date Formatting**

- Belgian/Swiss numbers: "septante" (70), "huitante/octante" (80), "nonante" (90) vs. France's "soixante-dix", "quatre-vingts", "quatre-vingt-dix"
- Date format: "le 14 juillet 2024" (day before month)
- Phone numbers: grouped as "06 12 34 56 78"

#### Impact on Recognition Accuracy

- Missing diacritics are pervasive errors in French ASR output
- Homophone errors directly affect comprehensibility
- Incorrect punctuation reduces readability
- Named entity errors are especially problematic in formal/business contexts

#### Techniques to Overcome

- **Neural diacritic restoration**: Train a character-level model to insert diacritics into unaccented text
- **Contextual post-processing**: Use a fine-tuned language model for homophone resolution as a second pass
- **French punctuation rules**: Implement rule-based punctuation formatting (guillemets, spacing)
- **NER fine-tuned on French**: Use French-specific NER models (CamemBERT-NER, spaCy-fr) for entity formatting
- **Locale-aware formatting**: Detect dialect for number conversion (septante vs. soixante-dix)

---

## Part C — Practical Evaluation

### Methodology

**ASR Systems Evaluated:**

| System | Version | Mode | Configuration |
|--------|---------|------|---------------|
| OpenAI Whisper | `tiny` | Local (CPU) | Language: French (`--language fr`) |
| Google Speech-to-Text | Web interface | Online | Language: French |

**Audio Samples:**

5-6 short audio clips (10-30 seconds each) recorded to test specific French ASR challenges:

| # | Sample Description | Challenge Tested | Duration |
|---|-------------------|-----------------|----------|
| 1 | Clear news-style reading | Baseline performance | ~20s |
| 2 | Fast casual conversation | Elision, reduction, informal register | ~15s |
| 3 | Sentences with heavy liaison | Word boundary disambiguation | ~15s |
| 4 | Numbers, dates, proper names | Entity recognition, formatting | ~15s |
| 5 | Speech with background noise | Noise robustness | ~15s |
| 6 | French-English code-mixed speech | Code-switching handling | ~15s |

### Error Analysis

| Audio Sample | Expected Transcript | Whisper Output | Google Output | Error Type | Possible Cause |
|-------------|--------------------:|:--------------:|:-------------:|:----------:|:--------------:|
| 1. News reading | `salut mon frère j'espère que vous allez bien bienvenue dans notre classe de science des données` | `salut mon frere, j'espere que vous allez bien. Bienvenue dans notre classe de science des donnees.` | `salut mon frère j'espère que vous allez bien bienvenue dans notre classe de science de données` | Diacritics (Whisper), Preposition choice (Google) | Whisper tiny missed accents on *frère*, *j'espère*, and *données*. Google substituted *des* with *de*. |
| 2. Casual speech | `ici on apprend le langage naturel en apprenant les données vocales et on les convertit en texte` | `Ici, on apprend le langage naturel en apprenant les données vocales et on les converti en texte.` | `ici on apprend le langage naturel en apprennant les données vocales et on les convertit en texte` | Homophone conjugation (Whisper), Typo (Google) | Whisper wrote the past participle *converti* instead of the verb *convertit* (homophones). Google added an extra 'n' to *apprenant*. |
| 3. Liaisons | `on sait que la langue française a des problèmes de liaisons et d'accords et ça peut causer des problèmes à notre modèle d'apprentissage automatique` | `On sait que la langue francaise a des problem des liasons et d'accord et ca peut causer des problem a notres model de l'apprentissage de machine.` | `on sait que la langue française a des problèmes de liaisons et d'accord et ça peut causer des problèmes à notre modèle de l'apprentissage de machine` | Liaison boundaries, spelling, literal translation (Both) | Whisper struggled with silent plurals (*problem*, *notres*), diacritics, and translated *apprentissage automatique* literally; Google did the same literal translation. |
| 4. Numbers/names | `j'espère que cette explication va vous donner des clarifications sur le projet en cours et que vous comprenez les difficultés de convertir les audios en texte` | `j'espere que cette explication va vous donner des clarifications sur le projet en main et que vous comprenez les difficultes de converture les audio en text.` | `j'espère que cette explication va vous donner des clarifications sur le projet en main et que vous comprenez les difficultés de convertir les audios en texte` | Vocabulary substitution (Both), spelling (Whisper) | Both models substituted *en cours* (in progress) with *en main* (in hand) due to contextual bias; Whisper also had minor spelling errors (*converture*, *text*). |
| 5. Noisy speech | `merci pour votre attention ici le groupe numéro cinq et j'espère que le message est utile` | `Merci pour votre attention, ici group numero 5 et j'espere que le message est utile.` | `merci pour votre attention ici le groupe numéro 5 et j'espère que le message est utile` | Number formatting (Both), Anglicization/Omission (Whisper) | Both systems transcribed the word *cinq* as the digit *5*; Whisper omitted *le*, wrote the English *group*, and missed diacritics. |

### WER Results

| Sample | Whisper WER (%) | Google WER (%) |
|--------|:--------------:|:--------------:|
| 1. News reading | 25.0% | 6.2% |
| 2. Casual speech | 17.6% | 5.9% |
| 3. Liaisons | 58.3% | 20.8% |
| 4. Numbers/names | 23.1% | 3.8% |
| 5. Noisy speech | 43.8% | 6.2% |
| **Average** | **33.6%** | **8.6%** |

### Error Type Distribution

| Error Type | Whisper Count | Google Count | Example |
|-----------|:------------:|:------------:|---------|
| Homophone confusion | 1 | 0 | *convertit* ↔ *converti* |
| Diacritic error | 8 | 0 | *frère* ↔ *frere*, *ça* ↔ *ca* |
| Liaison / Silent letters | 4 | 1 | *problèmes de* ↔ *problem des* |
| Vocabulary Substitution | 3 | 3 | *en cours* ↔ *en main* |
| Spelling/Typo | 4 | 1 | *convertir* ↔ *converture*, *apprenant* ↔ *apprennant* |
| Number formatting | 1 | 1 | *cinq* ↔ *5* |

### Observations

* **Google STT Outperformed Whisper Tiny**: Google finished with an average WER of **8.6%** compared to Whisper Tiny's **33.6%**. This is expected due to the model size difference (Whisper Tiny is only ~39MB, whereas Google's API uses a massive cloud-based architecture).
* **Whisper Tiny's Diacritic Limitations**: Whisper Tiny repeatedly failed to output diacritics (*frere*, *espere*, *donnees*, *ca*), which is a major issue in French where accents change word meaning. Google restored all diacritics correctly.
* **Liaison & Morphological Agreement**: In Sample 3 (heavy liaisons), Whisper Tiny struggled heavily (WER 58.3%) with word boundary detection and plural agreements, while Google kept the structure largely intact. Both systems struggled to correctly match the semantic meaning of domain-specific phrases (translating *apprentissage automatique* literally as *apprentissage de machine*).
* **Robustness to Noise**: Whisper Tiny showed moderate degradation in noisy conditions (Sample 5), whereas Google STT was highly robust, only registering a formatting error (*5* instead of *cinq*).

---

## Part D — Recommendations

Based on the pipeline analysis and practical evaluation, we recommend the following improvements for French ASR:

### Stage-by-Stage Recommendations

| Pipeline Stage | Current Limitation | Recommended Improvement | Expected Impact |
|---------------|-------------------|------------------------|----------------|
| **Speech Acquisition & Pre-processing** | Most training data is European French in clean conditions | Build a **balanced multi-dialect corpus** including European, Canadian, and African French. Apply data augmentation (noise injection, speed perturbation, room simulation). | Reduces dialect-based WER gap by 10-20% |
| **Feature Extraction** | Standard MFCCs may not capture nasal vowel contrasts at high speaking rates | Use **self-supervised learned features** (wav2vec 2.0 or HuBERT pre-trained on French). These learn language-specific spectral patterns automatically. | Better nasal vowel discrimination, improved accuracy at fast speaking rates |
| **Acoustic Modeling** | Models degrade on non-standard dialects; liaison not explicitly modeled | **Multi-dialect fine-tuning** of pre-trained models. Add **liaison-aware pronunciation modeling** with context-dependent rules. Use **speaker adaptation** (x-vectors). | More equitable performance across dialects |
| **Language Modeling** | LMs trained on written text; extreme homophony unresolved | Train LM on **spoken French transcripts** (not just written text). Use **subword tokenization** (BPE). Add **homophone disambiguation layer** with contextual embeddings. | Significant reduction in homophone errors (the largest error category) |
| **Decoding & Post-processing** | Missing diacritics, incorrect punctuation, entity errors | **Neural diacritic restoration** model. **French-specific punctuation rules** (guillemets, spacing). **French NER** for proper name formatting. **Locale-aware** number formatting. | Improved readability and meaning accuracy of output |

### Priority Ranking

1. **Homophone disambiguation** (highest impact — addresses the single largest error source)
2. **Diacritic restoration** (high impact — essential for correct French text)
3. **Multi-dialect training data** (high impact — addresses systematic bias)
4. **Spoken language LM training** (medium impact — bridges spoken/written gap)
5. **Liaison-aware modeling** (medium impact — reduces word boundary errors)

### Future Research Directions

- **Personalized ASR**: User-specific adaptation for frequently used vocabulary and speaking style
- **Contextual code-switching**: Models that can predict and handle language switches in multilingual environments
- **Low-resource dialect support**: Transfer learning from well-resourced European French to under-resourced African and Caribbean varieties
- **End-to-end diacritic-aware models**: Jointly model ASR and diacritic restoration rather than as separate stages

---

## References

1. Adda-Decker, M., & Lamel, L. (2005). Do speech recognizers prefer female speakers? *Proceedings of INTERSPEECH*, 2205-2208.

2. Ardila, R., et al. (2020). Common Voice: A massively-multilingual speech corpus. *Proceedings of LREC*, 4218-4222.

3. Baevski, A., et al. (2020). wav2vec 2.0: A framework for self-supervised learning of speech representations. *Advances in Neural Information Processing Systems*, 33.

4. Bartkova, K., & Jouvet, D. (2007). On using units trained on foreign data for improved multiple accent speech recognition. *Speech Communication*, 49(10-11), 836-846.

5. Boula de Mareüil, P., & Vieru-Dimulescu, B. (2006). The contribution of prosody to the perception of foreign accent. *Phonetica*, 63(4), 247-267.

6. Delattre, P. (1965). *Comparing the phonetic features of English, French, German and Spanish*. Heidelberg: Julius Groos Verlag.

7. Galliano, S., et al. (2009). The ESTER 2 evaluation campaign for the rich transcription of French radio broadcasts. *Proceedings of INTERSPEECH*, 2583-2586.

8. Gauthier, E., Besacier, L., & Voisin, S. (2016). Collecting resources in sub-Saharan African languages for automatic speech recognition: A case study of Wolof. *Proceedings of LREC*.

9. Lecouteux, B., et al. (2012). Distant speech recognition for home automation: Preliminary experiments in a smart home. *Proceedings of PETRA*.

10. Martin, L., et al. (2020). CamemBERT: A tasty French language model. *Proceedings of ACL*, 7203-7219.

11. Radford, A., et al. (2023). Robust speech recognition via large-scale weak supervision. *Proceedings of ICML*. (Whisper)

12. Walker, D.C. (2001). *French Sound Structure*. Calgary: University of Calgary Press.

---
