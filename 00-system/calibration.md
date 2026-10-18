---
type: system
version: 0.2.0
updated: 2026-10-18
---
# Target Calibration

Use this file whenever you set or change a target: in onboarding, in OKR planning and in
monthly reviews. The numbers are starting estimates for an adult beginner whose first language
is not Chinese, Japanese or Korean. After month 1, the learner's real pace replaces them (section 5).

## 1. Reference: HSK 3.0

From the *Chinese Proficiency Grading Standards for International Chinese Language Education*
(GF 0025-2021). Totals are cumulative.

| Level | Characters | Words |
|---|---|---|
| 1 | 300 | 500 |
| 2 | 600 | 1,272 |
| 3 | 900 | 2,245 |
| 4 | 1,200 | 3,245 |
| 5 | 1,500 | 4,316 |
| 6 | 1,800 | 5,456 |
| 7–9 | 3,000 | 11,092 |

The standard lists handwritten characters separately, and the handwriting requirement is much smaller
than the recognition requirement. ECP-OS follows the same idea: **recognize many, write few.**

For scale: the US Foreign Service Institute estimates about 2,200 class hours for an English speaker
to reach professional working proficiency in Mandarin.

## 2. Tiers: six-month targets

Pick the tier from the learner's realistic `hours_per_week`. Learners who read Japanese kanji or Korean hanja
can aim for up to 1.5× the character targets; they still need the simplified forms and the Mandarin sounds.

| Tier | Hours / week | About total hours | Scenes | Words | Characters (recognize) | Handwriting* | About HSK 3.0 |
|---|---|---|---|---|---|---|---|
| light | 3–5 | 100 | 20–25 | 400 | 250 | 80 | most of level 1 |
| steady | 6–10 | 200 | 35–45 | 800 | 400 | 150 | level 1, starting level 2 |
| committed | 11–17 | 350 | 60–80 | 1,300 | 600 | 250 | about level 2 |
| intensive | 18+ | 500+ | 100–120 | 2,000 | 900 | 350 | approaching level 3 |

\* Only when `writing_mode` is `handwriting` or `both`. Otherwise the handwriting target is 0.

A **scene** is one everyday situation (ordering food, buying a ticket) with at least 5 patterns
the learner says, at least 5 responses they may hear, and roughly 10–15 words.

Reading and writing by the end of the plan:

| Tier | Reading | Writing (typing with a pinyin keyboard) |
|---|---|---|
| light | short dialogues with pinyin | single sentences |
| steady | 1 graded reader at the lowest level | short paragraphs, about 50 characters |
| committed | 2–3 graded readers at about the 300–500 word level | short texts, 100–200 characters |
| intensive | 3–5 graded readers, up to about the 750 word level | texts of 200–300 characters |

## 3. Monthly ramp

Share of the six-month target to plan for each plan month (schemas.md section 1):

| Month | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Share | 10% | 20% | 20% | 20% | 20% | 10% |

- **Month 1** builds pronunciation: pinyin, four tones and the neutral tone, the 20 two-syllable tone
  combinations, aspiration pairs (b/p, d/t, g/k), plus the first easy scenes (greetings, numbers and prices).
  See `pronunciation-course.md`.
- **Month 6** is lighter on new material: mostly consolidation and the final test.
- **Characters** don't follow the ramp early on: the first 100 words already contain 80–100 different characters.
  In months 1–2 only report the character count; set character targets from month 3 (vision totals for months 3–6).

## 4. Pinyin plan

| Plan month | Pinyin in material |
|---|---|
| 1–2 | on all Chinese text |
| 3 | only on new words |
| 4–6 | none in reading material; available when the learner asks |

If `writing_mode` is `typing`, the learner uses a pinyin keyboard from month 1.

## 5. Recalibrate with the real pace

At each monthly review, for every volume key result (words, characters, scenes), compute
**achieved** = this month's actual ÷ this month's target. Next month's planned target comes from the vision's
milestone row (or the latest plan):

| Achieved | Next month's target |
|---|---|
| 100% or more | the planned target; up to +10% if the learner wants |
| 70–99% | the planned target × achieved |
| under 70% | the planned target × achieved, and review `hours_per_week` and `tier` with the learner |

Scaling the *planned* target (not this month's result) keeps a deliberately light month, such as month 1,
from shrinking the whole plan.

Write the reason in the key result's `calibration_note`.

## 6. Targets you must question

Before accepting a target, check it. If it hits one of these, explain the numbers and ask the
learner to confirm or adjust. If they keep it, record that in `calibration_note`.

- New words per week above 1.5× the tier's pace.
- "Characters" and "words" mixed up. Ask which one the learner means.
- Handwriting targets when `writing_mode` is `typing`.
- Novels or native-speaker material before plan month 4. Suggest graded readers instead.
- Essays longer than 200 characters within six months for any tier below `intensive`.
- Goals nobody can observe ("think like a native"). Rewrite them as behaviour.
