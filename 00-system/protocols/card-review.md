---
type: protocol
version: 0.2.0
updated: 2026-10-18
---
# Protocol: Card Review

**Runs when** inside a daily session, or the learner says "Quiz me".
**Reads** words and patterns with `next_review` ≤ today; vision (pinyin plan); profile.
**Writes** review fields on every item asked; counts in today's daily log.

Scenes are not reviewed here; due scenes are role-played (scene-practice).

## 1. Build the queue

1. Due items: `type: word` or `pattern` with `next_review` ≤ today, oldest `next_review` first, then lowest `box`.
2. New items (empty `last_review`) go last, up to today's new-item limit (daily-session step 2).
3. Stop at the time box or 30 cards, whichever comes first. The rest stay due.

## 2. Introduce new items first

For each new item show the characters, pinyin, meaning and example sentence. For words, add what each
character means ("打 hit + 包 wrap → pack up"). The learner types it once (characters, or pinyin with tones).
Don't grade yet; test new items at the end of the queue.

## 3. Ask

The card gets harder as the box rises:

| Box | Card | The learner gives |
|---|---|---|
| 1–2 | Chinese → English (pinyin shown according to the pinyin plan) | the meaning |
| 3 | English → Chinese | the word, typed in characters or in pinyin with tones |
| 4–5 | Situation → Chinese ("You want your food to go. What do you say?") | a sentence using the item |

Patterns always use the situation card. Accept tone numbers (`mai3dan1`) or tone marks.
On English → Chinese cards the tones must be right; allow one retry for a typo.

## 4. Grade and save

- Only correct or wrong. Then show the right answer with pinyin, in one line.
- Apply schemas.md section 5: correct → `box` + 1 (max 5); wrong → `box: 1`, `lapses` + 1;
  `next_review` from the new box; `last_review` = today.
- `recognize` = true when `box` is 3 or higher, false when it is lower.
- Save after every 10 cards and at the end, so nothing is lost if the session stops.

## 5. Close

Add `cards_reviewed` and `cards_correct` to today's daily log. Give the score, and name the one item
to watch (the one with the most lapses).
