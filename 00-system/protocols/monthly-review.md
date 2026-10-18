---
type: protocol
version: 0.2.0
updated: 2026-10-18
---
# Protocol: Monthly Review

**Runs when** the plan month is in its last 3 days or has ended, or the learner asks.
**Reads** the month's objectives and key results, weekly reviews, outputs, daily logs, vision, `calibration.md`.
**Writes** test and recording outputs, scores, `05-reviews/monthly/{cycle}.md`, profile `current_month`;
then quarterly-review or okr-planning.
**Takes** 30–45 minutes. It can be split over two sessions: tests first, review second.

## 1. Month-end tests

Run only the tests the month's key results need, and skip any already done this week.
Log each one with log-output (`output_type: test`, or `pronunciation-check`). Set `check` to the key result's
`metric_key` (`reading-check`, `writing-check` or `pron-accuracy`) so its accuracy is counted.

| Key result | Test |
|---|---|
| scenes-passed | scene-practice, Test mode |
| reading-check | a 100–200 character text (60–100 in months 1–2) using known words only, then 5 questions; accuracy % |
| writing-check | a short piece on a familiar topic, length as in the vision's milestone row; accuracy % = 100 × (1 − sentences with errors ÷ sentences) |
| pron-accuracy | pronunciation check (log-output section 4) with 10 items, including 2 minimal pairs |
| words-recognized | optional spot check: 20 random words with `recognize: true`, Chinese → English, reported in the review |

## 2. Fixed recording (every month, the same three tasks)

1. Introduce yourself (30–60 seconds).
2. Describe your typical day.
3. Role-play the first scene of the plan with the agent.

The learner records on their phone (saved in `09-attachments/`) and gives a transcript through voice input.
Log one output: `output_type: speaking`, `fixed_task: true`. Compare it with last month's fixed recording:
length, words used, errors, how it felt.

## 3. Score

- Each key result: recompute `current`; `score` = min(`current` ÷ `target`, 1), rounded to 0.1.
  Accuracy and average targets use the same formula (82 against a target of 80 → 1.0).
- Each objective: `score` = mean of its key results' scores, rounded to 0.1.
- Set `status: closed` on all of the month's objectives and key results.
- Reading the scores: 0.7–1.0 good; 0.4–0.6 real progress, but the target was too big or time too short;
  under 0.4: rethink the plan, don't just push harder.

## 4. Pace and calibration

For each volume key result (words, characters, scenes) apply calibration.md section 5 to get next month's
target, and compare it with the vision's milestone row. If the real study time differs from
`hours_per_week` by more than 30%, discuss updating `hours_per_week` and `tier`.

## 5. Talk it through

Show the scores and the recording comparison. Ask: best moment this month? Hardest thing?
One thing to change next month? Is it fun? If mean `fun` is under 3, change something concrete:
material closer to their interests, more role-play, shorter sessions.

## 6. Write

The review from `templates/review-monthly.md`: key-result scores, objective scores, tests, recording
comparison, pace and calibration, confidence and fun, and **Decisions for next month** (targets per area,
focus, routine changes). Properties: `period: monthly`, `cycle`, `start`, `end`, `minutes`,
`confidence_avg`, `fun_avg`, `score` (mean objective score).
Profile: `current_month` + 1.

## 7. Next

- Plan month 3 or 6 just ended → `quarterly-review.md` first.
- Otherwise → `okr-planning.md` for the next month.
