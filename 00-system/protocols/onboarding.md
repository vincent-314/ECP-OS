---
type: protocol
version: 0.2.0
updated: 2026-10-18
---
# Protocol: Onboarding

**Runs when** `01-profile/learner-profile.md` is missing, or its `onboarding` is not `complete`.
**Reads** `kernel.md`, `schemas.md`, `calibration.md`, `scene-catalog.md`.
**Writes** `01-profile/learner-profile.md` and `01-profile/vision.md`; then hands over to okr-planning and task-planning.
**Takes** 20–30 minutes. The learner can stop at any time; `onboarding_round` records where to resume.

## How to talk during onboarding

- Ask two or three questions at a time, never a long questionnaire.
- Plain words: say "goals for this month", not "OKR", until you show the plan.
- Save what you learned at the end of every round before moving on.
- Resuming: say which round you are continuing from and summarise what you already know in one line.

## Round 0 · Welcome

1. Explain in three sentences: they study by talking to you; you keep all the records; today you will agree
   on a six-month goal and plan the first week together.
2. If the profile is missing, create it from `templates/profile.md` with `created` = today,
   `onboarding: in-progress`, `onboarding_round: 1`.
3. Search for records with `sample: true`. If there are any, say they are demo records the learner can look at
   in Obsidian now, and that they will be removed before the real plan is created (their file names would
   clash with real records).

## Round 1 · Background

Ask:
- What should I call you? What's your first language? Do you speak other languages?
- Have you learned any Chinese before? (none, a little, some, and what)
- Why Chinese? Is there a date that matters, such as a trip, a move or an exam?

Save `name`, `native_language`, `other_languages`, `prior_chinese`, `goal_reason`, `deadline`,
and the sections "About me" and "Why I'm learning Chinese". If the learner reads Japanese kanji or
Korean hanja, write it in "Placement notes". Set `onboarding_round: 2`.

## Round 2 · Time

Ask:
- In a normal week (not a good one), how many hours can you study?
- When do you usually have time?
- Can you switch on Chinese (Mandarin, Simplified) voice input on your phone or computer?
  It is used for pronunciation checks. If not, offer to help set it up during the first session.

Pick `tier` from calibration.md section 2. Under 3 hours a week: say progress will be slow, suggest 3 hours,
accept their answer, use `light`. Save `hours_per_week`, `tier`, `study_slots`, and the voice-input
status in "Placement notes". Set `onboarding_round: 3`.

## Round 3 · Preferences

Ask:
- The default focus order is listening, speaking, reading, writing. Keep it or change it?
- Writing: type with a pinyin keyboard, handwrite characters, or both? Explain that learners recognise
  far more characters than they write, and that typing is recommended unless they have a reason to handwrite.
- What are you interested in? (to choose material and scenes)
- If you tried before: what got in the way?
- Do you have a teacher or a Chinese-speaking friend who could give feedback sometimes?

Save `skill_priority`, `writing_mode`, `interests`, `past_obstacles`, `teacher`, and the section
"What got in the way before". Set `onboarding_round: 4`.

## Round 4 · Quick placement (5–10 minutes)

- `prior_chinese: none`: no tests. Show the four tones with mā má mǎ mà and say that month 1 starts
  with sounds. Write "complete beginner" in "Placement notes".
- Otherwise:
  1. **Word check.** Show these 20 words in characters only. The learner names the ones they can read and understand.
     你 我 好 是 不 人 吃 喝 水 钱 多少 今天 明天 喜欢 学习 朋友 时间 买 去 中国
  2. **Pronunciation check**, only if voice input works: log-output section 4 with 5 items from the list.
  3. If they know 10 or more of the 20, add the known words to the word bank (add-to-library,
     placement exception).
- Write the results in "Placement notes". Set `onboarding_round: 5`.

## Round 5 · The six-month vision

1. Ask: "Imagine six months from now. Name three to five situations where you'd love to manage in Chinese."
   Turn each into a can-do statement ("I can order a meal and ask for it not spicy").
2. Propose targets from the tier (calibration.md section 2), split per month with the ramp (section 3),
   plus the pinyin plan (section 4). Show one table: month × scenes, words, characters, handwriting,
   reading, writing. Kanji or hanja readers: character targets can be up to 1.5× the tier.
3. Check the red flags (section 6). If the learner wants more, show what it means per day
   ("that is 25 new words every day"), then let them decide and record `calibration_note`.
4. Adjust until the learner says yes.
5. `start_date` = today; if today is the 29th, 30th or 31st, use the 1st of next month and treat the days
   before as warm-up. Set `plan_months: 6`, `current_month: 1`.
6. Create `01-profile/vision.md` from the template: targets, can-do statements, milestone table,
   calibration section. `end_date` = `start_date` + 6 months − 1 day. Set `onboarding_round: 6`.

## Round 6 · First month and first week

1. Sample data: say how many `sample: true` records there are, then delete them. They are demo records,
   not the learner's data.
2. Run `okr-planning.md` for plan month 1.
3. Run `task-planning.md` for the first week.
4. Set `onboarding: complete`.
5. Explain the daily loop in three lines and point to `Home.md` in Obsidian.
   Offer a first 15-minute session now (`daily-session.md`).

## Close

Tell the learner what was set up (profile, vision, number of objectives and tasks) and what to say
next time: "Let's study".
