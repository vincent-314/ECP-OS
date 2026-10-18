---
type: protocol
version: 0.2.0
updated: 2026-10-18
---
# Protocol: Task Planning

**Runs when** after OKR planning, after a weekly review, or the learner asks to plan the week.
**Reads** active objectives and key results, open tasks, profile, the latest weekly review.
**Writes** task files in `03-tasks/`.
**Takes** about 5 minutes with the learner.

## 1. Set the week

- The week = the next 7 days starting today (or next Monday if the learner prefers).
  Each task's `week` = the ISO week of its `due` date.
- Weekly minutes = `hours_per_week` × 60. Half is for the daily routine (cards, input, logging);
  the other half is the **task budget**.

## 2. Carry over open tasks

List open tasks that are due or overdue. For each: keep it with a new `due`, or drop it
(delete only with the learner's OK). If more than two carry over, ask whether the weeks are too full.

## 3. Draft new tasks from the key results

For each active key result, decide what work this week moves it. Then:

- 15–60 minutes per task. Title = verb + object ("Learn the toolkit for asking directions").
- "Done when" is checkable ("4 role-play outputs logged").
- `objective`: exactly one. `kr`: the key result it moves.
- Spread `due` over the learner's study days. Order by `skill_priority`.
- Keep total `effort_min` within the task budget. If it doesn't fit, drop lead work before lag tests,
  and tell the learner what was left out.
- Scenes: learn a scene early in the week; role-play it at least twice later in the week.
- Weekly review fixes: each agreed fix becomes a 10–15 minute task.
- **Last week of the plan month:** add the month-end tests the active key results need (scene test,
  reading check, writing check, pronunciation check) and the monthly fixed recording.
  They run inside the monthly review; the tasks reserve the time.
- **Plan month 1:** spread the 8 lessons of `pronunciation-course.md` over weeks 1–2 (one per study day),
  alongside the first scenes. Lesson 1 comes first.

The daily routine (card review, daily input) is not a task.

## 4. Agree with the learner

Show the week as a table: day, task, minutes, objective. Apply the learner's changes.
Tasks the learner adds get `origin: learner`; if it's unclear which objective a task supports, ask.

## 5. Write

One file per task from the template, `origin: agent` for yours.
File name: `YYYY-MM-DD-short-slug.md` with today's date.

## Close

"Your week is planned: N tasks, about X minutes. Say 'Let's study' to start."
