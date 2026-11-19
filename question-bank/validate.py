import json
from pathlib import Path

root = Path(__file__).resolve().parent
sources = json.loads((root / 'sources.json').read_text(encoding='utf-8'))
source_ids = {s['id'] for s in sources}
assert len(source_ids) == len(sources)
assets = json.loads((root / 'images' / 'manifest.json').read_text(encoding='utf-8'))
asset_map = {a['id']: a for a in assets}
assert len(asset_map) == len(assets)
for a in assets:
    assert (root / a['path']).is_file() and a['reference_source_id'] in source_ids
    assert a['license'] and a['origin'] and a['alt']['en'] and a['alt']['fr']
banks = {lang: json.loads((root / lang / 'questions.json').read_text(encoding='utf-8')) for lang in ('en', 'fr')}
for lang, bank in banks.items():
    ids = [q['id'] for q in bank]
    assert len(ids) == len(set(ids)), f'duplicate ID: {lang}'
    for q in bank:
        assert q['language'] == lang and q['question'].strip()
        choices = q['choices']
        assert len(choices) >= 2 and all(c['text'].strip() for c in choices)
        choice_ids = [c['id'] for c in choices]
        assert len(choice_ids) == len(set(choice_ids)) and q['correct_choice_id'] in choice_ids
        assert q['source_ids'] and set(q['source_ids']) <= source_ids
        assert 'image' in q and q['source_reviewed_on']
        if q['image'] is not None:
            asset = asset_map[q['image']['asset_id']]
            assert q['image']['path'] == asset['path']
en = {q['id']: q for q in banks['en']}
fr = {q['id']: q for q in banks['fr']}
assert en.keys() == fr.keys()
for key in en:
    for field in ('topic', 'correct_choice_id', 'source_ids', 'authorship', 'image', 'review_status'):
        assert en[key][field] == fr[key][field], (key, field)
    assert [c['id'] for c in en[key]['choices']] == [c['id'] for c in fr[key]['choices']]
print(f"Valid: {len(en)} paired questions, {len(sources)} sources; images: {sum(q['image'] is not None for q in en.values())}")
