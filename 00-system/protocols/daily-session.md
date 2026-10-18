---
type: protocol
version: 0.2.0
updated: 2026-10-18
---
# Protocol: Daily Session

**Runs when** the learner says "Let's study" or similar.
**Reads** profile, vision (pinyin plan), today's daily log, due items, open tasks.
**Writes** today's daily log, review fields, outputs, task `done`, key-result `current`.
**Takes** the time the learner has (default from `study_slots`).

## 1. Open (1 minute)

- Create `04-daily/{today}.md` from the template if it doesn't exist.
- Count: words and patterns due (`next_review` ≤ today), scenes due, tasks due today or overdue.
- Ask: "How much time do you have today?" Show the plan as one short list. Default split:

| Time | Cards | Main block | Input | Close |
|---|---|---|---|---|
| 15 min | 7 | — | 5 | 3 |
| 30 min | 10 | 12 | 5 | 3 |
| 60 min | 15 | 30 | 12 | 3 |

Scale for other lengths. If a scene is due and no task covers it, the main block is a role-play of that scene.

## 2. Cards

Run `card-review.md` within its time box.
New items today = (this month's new-word target − words added so far this month) ÷ study days left
this month, rounded up, at most 20.

## 3. Main block

Take the first open task by `due` (overdue first; ties by `skill_priority`) and follow its protocol:
- learn, practise or test a scene → `scene-practice.md`
- speaking or writing → `log-output.md`
- input → section 4 below
- anything else → do it, guided by its "Done when"

When "Done when" is met, set `done: true`. If time runs out, say what is left; the task stays open.

## 4. Input

Choose one:
- an `easy` or `ok` source from the Inbox with status `new` or `in-progress`, or
- a short text you write now: 80–150 characters (40–80 in months 1–2), a dialogue or mini story on the
  current scene or the learner's interests. Use known words; at most 1 new word in 20, in **bold** with a gloss.
  Pinyin follows the pinyin plan. Then ask three comprehension questions in English.

With fewer than 50 known words there is too little to build a text from. Instead: the learner plays the current
scene's dialogue lines with text-to-speech while reading the pinyin, then listens to a beginner source from the Inbox.

Add the minutes to `input_min`. If a source was used, update its `status` and `minutes` (capture-source).

## 5. Close (2–3 minutes)

1. Ask: "Confidence today, 1 to 5? Fun, 1 to 5?" and "What was one win today?"
2. Update the daily log: `minutes`, `cards_reviewed`, `cards_correct`, `input_min`, `output_count`,
   `confidence`, `fun`, and the body sections (what we did, new words, mistakes to remember, the win).
3. Recompute `current` for key results that moved (metric_key table in `okr-planning.md`).
4. End on a success: repeat one thing they got right. Say what's next ("Tomorrow: role-play asking directions").
5. If a review is due (AGENTS.md section 1), suggest it.
