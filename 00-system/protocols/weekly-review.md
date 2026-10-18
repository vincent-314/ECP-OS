---
type: protocol
version: 0.2.0
updated: 2026-10-18
---
# Protocol: Weekly Review

**Runs when** the learner says "Weekly review", or 7+ days have passed since the last one (AGENTS.md suggests it).
**Reads** daily logs, tasks, outputs, library, active key results, the last weekly review.
**Writes** `05-reviews/weekly/{YYYY-Www}.md`, key-result `current`; then task-planning.
**Takes** 10–15 minutes.

## 1. Period

`start` = the day after the last weekly review's `end` (first review: `start_date`). `end` = today.
`cycle` = the ISO week of `end`.

## 2. Gather the numbers

From files in the period:
- Daily logs: total `minutes`, `cards_reviewed`, `cards_correct`, `input_min`, `output_count`;
  mean `confidence` and `fun`; number of study days.
- Tasks with `due` in the period: done vs. not done.
- Outputs: count by `output_type`; every `error_types` value counted, most frequent first.
- Library: words and patterns created; change in words with `recognize: true`; scenes that changed status.

## 3. Key results

Recompute `current` for every active key result (metric_key table in `okr-planning.md`) and save it.
**On track** = `current` ≥ 0.8 × target × (days elapsed in the plan month ÷ days in the plan month).
For accuracy and average key results that are only measured at month end, write "measured at month end".

## 4. Talk it through

Show the numbers and the key-result table first, briefly. Then ask, two questions at a time,
offering what the data suggests:
1. What improved?
2. What fell behind?
3. What needs adjusting?
4. What should be celebrated?

Then the top 1–3 mistake types: for each, agree on one small fix for next week (a 10–15 minute drill).
If the week was thin (few study days), ask why without judging, and lighten next week instead of piling up tasks.

## 5. Write

The review from `templates/review-weekly.md`: numbers, key-result table, the learner's answers
in their own words, the mistakes, the decisions. Properties: `period: weekly`, `cycle`, `start`, `end`,
`minutes`, `confidence_avg`, `fun_avg`.

## 6. Next week

Run task-planning, including the agreed fixes. If the plan month ends within 7 days, say that the month-end
tests and the monthly review are coming.

## Close

Name one concrete win from the week.
