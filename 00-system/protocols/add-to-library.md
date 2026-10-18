---
type: protocol
version: 0.2.0
updated: 2026-10-18
---
# Protocol: Add to Library

**Runs when** the learner asks to add a word, pattern or scene, or another protocol needs new library items.
**Writes** notes in `06-library/words/`, `06-library/patterns/`, `06-library/scenes/`.

## Before adding

- Check whether it exists (by file name; for patterns also by the `pattern` property).
  If it exists, add the new links (`scenes`, `patterns`, `words`) and stop. Never reset progress fields.
- More than 10 items at once: show the list and ask first.
- Words well above the learner's level (rare words, or HSK 4+ in months 1–3): add only if the learner wants them.

## Word

- File name: the word in Simplified characters. Same characters, different word: add the pinyin, as in `行 (háng).md`.
- `pinyin`: tone marks, syllables of the word joined (schemas.md section 1). Double-check every tone.
- `meaning`: short English, most common sense first. `pos`. `characters`: each character of the word.
- `hsk`: only if you are sure of the HSK 3.0 level; otherwise leave it empty.
- `example`: one short sentence at the learner's level, preferably from the scene's context,
  with `example_pinyin` and `example_en`.
- Links: `scenes`, `patterns`. `source`: where it came from (a scene, a source note, an output).
- Progress: all mastery flags false, `box: 1`, `next_review` = today, `lapses: 0`.
  **Taught-item rule:** items you teach right away (scene Learn) → `last_review` = today, `next_review` = tomorrow,
  so they are reviewed tomorrow, not introduced twice.
  **Placement exception:** words the learner already knows → `box: 3`, `recognize: true`,
  `next_review` = today + 7 days.
- Body, "Notes": what each character means, and one or two known words that share a character.

## Pattern

- File name and `pattern`: slots written as `…`, as in `可以…吗？`.
- `structure` with slot labels (`可以 + verb phrase + 吗？`). `function`: what it is for, in plain English.
  `grammar_point`: one line, only if useful.
- Example with pinyin and English; 2–3 more in the body table. "Watch out": the typical mistake.
- Progress fields as for words.

## Scene

- If it is in `scene-catalog.md`, use its slug, titles, category and difficulty.
- Otherwise: an English slug, `title_zh`, `title_en`, a category from schemas.md, difficulty 1–3.
- `status: planned`; `objectives` = [the active objective it belongs to], or `[]`.
  The toolkit is built later (scene-practice, Learn).
