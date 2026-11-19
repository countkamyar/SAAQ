# Québec Class 5 practice question bank

This is an independently authored bilingual starter bank for passenger-vehicle learners, not an official SAAQ exam or a complete representation of its questions. English and French records share stable IDs and choice IDs. All correct answers currently use choice `a`; shuffle choices when presenting them. Each record links to an entry in `sources.json` and records the source review date. Image fields link to locally created illustrations or are null. No external question text or images are included.

The source links support the underlying facts; they do not certify that the SAAQ endorsed, wrote, translated, or approved these questions. French text is independently written for this project, not an official translation. Each question needs independent legal, factual, language, accessibility and editorial review before use; rules and official guidance can change. In particular, general rules may have exceptions and source pages can differ in wording. Recheck the current Highway Safety Code and applicable regulations against each item before release.

## Files and fields

- `en/questions.json` and `fr/questions.json`: parallel arrays with matching IDs, choice IDs, answer keys and source IDs.
- `sources.json`: source inventory, access date and rights notes.
- `images/manifest.json`: original illustration provenance, licence, alternative text and references. Image paths resolve from the `question-bank` directory.
- `RIGHTS_AND_COVERAGE.md`: reuse and coverage limitations.
- `validate.py`: checks structural and bilingual consistency; it cannot verify legal accuracy or rights.

Records use `image: null` when no image is provided. Future images should include an asset path or URL, creator, licence or written permission, attribution, and source; do not add an image merely because it is publicly visible. Question authorship is `original_practice_question`; neither review status is legal approval. The parking-law source was consolidated in September 2025, so those records are explicitly flagged `current_law_check_required`.
