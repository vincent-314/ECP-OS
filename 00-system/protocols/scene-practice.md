---
type: protocol
version: 0.2.0
updated: 2026-10-18
---
# Protocol: Scene Practice

**Runs when** a task says learn, practise or test a scene; a scene is due; or the learner asks
("Let's role-play ordering food").
**Reads** the scene note, its words and patterns, profile, vision (pinyin plan).
**Writes** the scene note, new words and patterns, outputs, review fields.

Three modes: **Learn** (scene `planned`), **Role-play** (scene `learning` or `passed`),
**Test** (month end, or whenever a `scenes-passed` key result needs it).

## Learn

1. Build the toolkit in the scene note (every section of the template):
   - **What I say:** at least 5 lines, built on patterns.
   - **What I might hear:** at least 5 lines, including the question the other person asks most often.
   - **Culture & etiquette:** 2–4 practical points. **Curveballs:** 2 things that can go wrong, with a line for each.
   - **Pass criteria** (default): 6+ turns with the agent and no English; one curveball handled;
     key information at least 90% accurate; understands every "What I might hear" line.
   - Reuse known words. About 8–15 new words per scene (5–8 for the light tier).
2. Create notes for the new words and patterns (add-to-library), each linked to the scene.
   Fill the scene's `patterns` and `words`. They are taught in step 3, so set `last_review` = today and
   `next_review` = tomorrow (taught-item rule in add-to-library).
3. Teach it: go through "What I say" (meaning, pinyin; the learner types each line once), then
   "What I might hear" (the learner plays each line with text-to-speech before reading it, then says what it means).
4. If voice input is available, run a short pronunciation check on 3 key lines (log-output section 4).
5. Set `status: learning`, `box: 1`, `next_review` = tomorrow.

## Role-play

1. Set the scene in one English sentence ("You're in a noodle shop at lunchtime").
   You play the other person, in Chinese only, at the learner's level.
2. Use the "What I might hear" lines, varied naturally. Add one curveball after the third turn.
   Listening first: when `listening` is the top of `skill_priority`, ask the learner to play each of your lines
   with text-to-speech before reading it.
3. The learner answers in Chinese: characters, pinyin, or voice input. **Voice input is best:** if the
   recognised text doesn't match what they meant, ask what they meant and log a pronunciation error.
4. If the learner is stuck, give a hint (the first word, or an English cue). Two hints in a row, or
   switching to English, counts as a `fluency` error; the role-play continues.
5. Stop after 8 turns, or when the goal is reached. A **turn** = one learner reply in Chinese that moves the conversation on.
6. Feedback: at most 3 corrections, the most important first, then the corrected lines.
   `accuracy` = key facts said correctly ÷ key facts needed (what, how many, preferences, numbers, place, time).
   Log it with log-output (`output_type: role-play`, `rounds`, `accuracy`, `error_types`).
7. Update the scene: `practice_count` + 1, `best_rounds` = the higher of old and new, `accuracy`,
   `last_practiced`. Review fields: success (6+ turns and accuracy ≥ 0.8) → `box` + 1, otherwise `box: 1`;
   `next_review` per schemas.md section 5.
8. Lines the learner needed but didn't have go into the toolkit; new words via add-to-library.

## Test

1. How many: the `target` of the `scenes-passed` key result, minus scenes already passed.
   Which: random picks among the scenes whose `objectives` include the objective, with `status: learning`.
   No preview, no choice.
2. Run each as a role-play with no hints and one curveball. Don't mention the pass criteria during the test.
3. Judge against the scene's pass criteria. Pass → `status: passed`, `passed_on` = today.
   Fail → stays `learning`; name the gap. One retest per scene per month, after more practice.
4. Log each test with log-output (`output_type: test`) and update the scene as in Role-play step 7.
