---
type: protocol
version: 0.2.0
updated: 2026-10-18
---
# Protocol: OKR Planning

**Runs when** onboarding Round 6, right after a monthly review, or the learner asks to plan the month.
**Reads** profile, vision, `calibration.md`, `scene-catalog.md`, the latest monthly review, library counts.
**Writes** objectives and key results in `02-okr/{cycle}/`; new scene notes with `status: planned`.
**Takes** 10–15 minutes with the learner.

## 1. Find the plan month

- Plan month n runs from `start_date` + (n − 1) months to `start_date` + n months − 1 day.
- `cycle` = `YYYY-MM` of its first day. Folder: `02-okr/{cycle}/`.
- Leftovers: any objective or key result from an earlier cycle that is still `active` should have been
  scored in the monthly review. If not, score it now (monthly-review step 3) and close it.

## 2. Get this month's volume targets

- Month 1: the month-1 row of `vision.md`.
- Later months: "Decisions for next month" in the latest monthly review (already recalibrated).
  If that is missing, take the vision row and apply calibration.md section 5 yourself.

## 3. Draft the objectives

Three to five objectives, in the order of `skill_priority`:

| Area | When | Typical objective |
|---|---|---|
| listening-speaking | every month | "Handle 6 new everyday scenes" |
| vocabulary-reading | every month | "Recognise 300 words and read short dialogues" |
| pronunciation | month 1 always; later when pronunciation errors were last month's top error type | "Hear and say the four tones reliably" |
| writing | from month 2, or from month 1 if `writing_mode` includes handwriting | "Write short messages about my day" |
| confidence-fun | every month, always last | "Enjoy it and use Chinese for real" |

**Choose the month's scenes:** first the learner's can-do situations from the vision, then
`scene-catalog.md` in order, preferring the learner's interests. Difficulty 1 in months 1–2,
difficulty 1–2 in months 3–4, difficulty 2–3 in months 5–6. Month 1 starts with
greetings-introductions and numbers-prices.

**Month 1 pronunciation:** the pronunciation objective follows `pronunciation-course.md`. Typical key results:
lessons done (pron-checks, 6–8) and the lesson-8 baseline check (pron-accuracy, 70–80).

## 4. Draft the key results

Two to four per objective, at least one `lag`. Every key result has a `metric_key` from this table,
so any agent computes `current` the same way. **Window** = the objective's `start` to `end`.

| metric_key | kind | `current` is | Typical target |
|---|---|---|---|
| scenes-toolkit | lead | scenes whose `objectives` include this objective, with status `learning` or `passed` | the month's scenes |
| roleplays | lead | outputs with `output_type: role-play` dated in the window | light 8 · steady 12 · committed 16 · intensive 20 |
| scenes-passed | lag | scenes whose `objectives` include this objective, with status `passed` | at least 60% of the month's scenes |
| words-added | lead | words with `created` in the window | the month's new words |
| words-recognized | lag | all words with `recognize: true` (running total) | about 85% of all words added by month end (new words need 4+ days to reach box 3) |
| words-pronounced | lag | all words with `recognize: true` and `pronounce_ok: true` (running total) | about 70% of words-recognized |
| characters-recognized | lag | distinct characters in words with `recognize: true` (running total) | the vision's character total; from plan month 3 only |
| input-minutes | lead | sum of `input_min` in daily logs in the window | light 200 · steady 400 · committed 700 · intensive 1000 |
| reading-check | lag | accuracy % of the month-end reading check | 80 |
| writing-pieces | lead | outputs with `output_type: writing` in the window | 4–8 |
| writing-check | lag | accuracy % of the month-end writing check | 80 |
| handwriting | lag | distinct characters in words with `handwrite: true` (running total) | the month's handwriting total |
| pron-checks | lead | outputs with `output_type: pronunciation-check` in the window | 4–8 |
| pron-accuracy | lag | accuracy % of the month-end pronunciation check | 80 |
| study-days | lead | daily logs in the window with `minutes` above 0 | study days per week × weeks |
| real-world | lead | outputs with `output_type: real-world` in the window | 2–4 |
| fun-avg | lag | mean `fun` in daily logs in the window | 3.5 |
| confidence-avg | lag | mean `confidence` in daily logs in the window | 3.5 |

Rules:
- Title every key result in plain words ("Do 16 role-plays with the agent"), so the learner understands it without this table.
- Rewrite vague aims as behaviour (schemas.md, key-result rules).
- Check every target against calibration.md section 6.

## 5. Agree with the learner

Show one compact table: each objective with its key results and targets. Ask "Anything to change?"
The learner decides. If a change goes past calibration, explain once, then record `calibration_note`.

## 6. Write the files

- `{cycle}-O{n}.md` from the objective template: `cycle`, `month`, `start`, `end`, `code`, `title`,
  `area`, `priority`, `status: active`; "Why this matters" in one or two sentences.
- `{cycle}-KR{n}-{m}.md` from the key-result template: `code: KR{n}.{m}`, `objective`, `kind`,
  `metric_key`, `metric`, `target`, `unit`, `measure_by`, `due` = the objective's `end`.
  Compute `current` now (running totals are rarely 0).
- Each scene of the month without a note: create it from the template in `06-library/scenes/` with
  `status: planned`, `objectives` = [this objective], titles, category and difficulty. Scenes that already exist
  (for example a scene to retest from last month) get this objective added to `objectives`; earlier
  objectives stay, so last month's key results don't change.
  The toolkit is built later (scene-practice, Learn).
- Profile: `current_month` = this plan month.

## Close

Hand over to `task-planning.md` for the first week of the month.
