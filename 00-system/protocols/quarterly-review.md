---
type: protocol
version: 0.2.0
updated: 2026-10-18
---
# Protocol: Quarterly Review

**Runs when** right after the monthly review of plan month 3 (`q1`) and plan month 6 (`q2`).
**Reads** vision, the quarter's monthly reviews, the fixed recordings, library totals.
**Writes** `05-reviews/quarterly/q{n}.md`; changes to `vision.md` when agreed.
**Takes** about 20 minutes.

## 1. Totals vs. vision

Scenes passed, words recognised, characters recognised, handwriting: compare each with the vision targets
and with the milestone rows up to this month. On track = at least 80% of the milestone total so far.

## 2. Then and now

Put the month-1 fixed recording transcript next to this month's. Ask the learner to listen to both recordings.
What do they notice? Add your own observations: length, variety of words, errors, fluency.

## 3. Is the vision still right?

Re-read the can-do statements together. Are they still what the learner wants? Are the hours realistic?
Ask; don't assume.

## 4. Changes (q1)

If needed, update the targets and the milestone rows for months 4–6 in `vision.md`, with a
`calibration_note`, and record each change in the review.

## 5. End of the plan (q2)

Celebrate concretely: numbers, the recording comparison, the can-do statements now met. Then offer what's next:
- **A new six-month plan:** move the old vision to `01-profile/archive/vision-{start YYYY-MM}.md`; set a new
  `start_date` (tomorrow), `current_month: 1`; run onboarding Round 5 with the updated profile, then Round 6.
- **Maintenance:** card review plus one role-play a week, no monthly OKR. The learner can restart a plan any time.

## 6. Write

The review from `templates/review-quarterly.md`. Properties: `period: quarterly`, `cycle` (q1 or q2),
`start`, `end`, `score` = mean of the quarter's monthly review scores.
