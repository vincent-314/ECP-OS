---
type: system
version: 0.2.0
updated: 2026-10-18
---
# ECP-OS Schemas

The single source of truth for every record: where it lives, how the file is named,
which properties it has, and which values are allowed. Templates in `00-system/templates/`
mirror these schemas. Views in `00-system/views/` depend on them, so do not rename properties.

## 1. Conventions

- **Dates** `YYYY-MM-DD`. **Weeks** ISO `YYYY-Www` (`2026-W42`). **Calendar months** `YYYY-MM`.
- **Plan month** n runs from `start_date` + (n − 1) months to `start_date` + n months − 1 day.
  Its **cycle** id is `YYYY-MM` of its first day. OKR folders and monthly reviews use the cycle id.
- **Links in properties** are quoted wikilinks: `objective: "[[2026-11-O1]]"`.
  Lists of links: `scenes: ["[[ordering-food]]", "[[asking-directions]]"]`.
- **Chinese** in Simplified characters.
- **Pinyin** with tone marks. Syllables of one word are joined (`càidān`); words in a sentence are
  separated by spaces. Write the base tone (`kěyǐ`, not `kéyǐ`), except 一 and 不, which are written
  with their changed tone as in most textbooks (`yí fèn`, `bú yào`).
- Every record has `type` and `created`. Shipped demo records also have `sample: true`.

## 2. Record types

| type | Folder | File name | Example |
|---|---|---|---|
| profile | `01-profile/` | `learner-profile.md` | |
| vision | `01-profile/` | `vision.md` (earlier plans: `01-profile/archive/vision-{start YYYY-MM}.md`) | |
| objective | `02-okr/{cycle}/` | `{cycle}-O{n}.md` | `2026-11-O1.md` |
| key-result | `02-okr/{cycle}/` | `{cycle}-KR{n}-{m}.md` | `2026-11-KR1-2.md` (code `KR1.2`) |
| task | `03-tasks/` | `YYYY-MM-DD-short-slug.md` (creation date) | `2026-11-03-roleplay-ordering-food.md` |
| daily | `04-daily/` | `YYYY-MM-DD.md` | `2026-11-03.md` |
| review | `05-reviews/weekly/` · `monthly/` · `quarterly/` | `YYYY-Www.md` · `{cycle}.md` · `q{n}.md` | `2026-W45.md`, `2026-11.md`, `q1.md` |
| word | `06-library/words/` | the word in characters | `打包.md`; same characters, different word: `行 (háng).md` |
| pattern | `06-library/patterns/` | the pattern, slots written as `…` | `可以…吗？.md` |
| scene | `06-library/scenes/` | English slug | `ordering-food.md` |
| source | `07-inbox/` | `YYYY-MM-DD-short-slug.md` | `2026-11-03-restaurant-vlog.md` |
| output | `08-output/` | `YYYY-MM-DD-{output_type}-short-slug.md` | `2026-11-03-role-play-ordering-food.md` |

File names never contain `\ / : * ? " < > |`. Use full-width `？` and `：` in Chinese names.
Recordings, images and PDFs go in `09-attachments/`.

## 3. Properties by type

### profile

```yaml
type: profile
created: 2026-10-18
onboarding: not-started   # not-started | in-progress | complete
onboarding_round: 0       # last round started (0–6); used to resume
name:
native_language:
other_languages: []
prior_chinese: none       # none | a-little | some
goal_reason:              # why Chinese, in the learner's words
deadline:                 # date, optional (e.g. a trip)
hours_per_week:           # number, realistic
tier:                     # light | steady | committed | intensive (calibration.md)
study_slots:              # e.g. "weekday mornings 30 min, Sat 1 h"
skill_priority: [listening, speaking, reading, writing]
writing_mode: typing      # typing | handwriting | both
interests: []
past_obstacles:
teacher: false            # true if a human teacher gives feedback
start_date:               # day 1 of plan month 1 (never the 29th–31st)
plan_months: 6
current_month: 1          # plan month
ui_language: en
```

### vision

```yaml
type: vision
created:
start_date:
end_date:
tier:
hours_per_week:
target_scenes:            # number, end of plan
target_words:
target_characters:        # characters the learner can recognize
target_handwriting:       # 0 when writing_mode is typing
calibration_note:         # why targets differ from calibration.md, if they do
```

Body: can-do statements, monthly milestone table, pinyin plan.

### objective

```yaml
type: objective
created:
cycle: 2026-11            # id of the plan month (YYYY-MM of its first day)
month: 1                  # plan month number
start: 2026-11-03         # first day of the plan month
end: 2026-12-02           # last day of the plan month
code: O1
title:
area: listening-speaking  # listening-speaking | vocabulary-reading | writing | pronunciation | confidence-fun
priority: 1               # 1 = highest
status: active            # active | closed
score:                    # 0.0–1.0, set at monthly review (mean of its KR scores)
```

### key-result

```yaml
type: key-result
created:
cycle: 2026-11
code: KR1.2
objective: "[[2026-11-O1]]"
title:
kind: lead                # lead = process the learner controls | lag = outcome, tested
metric_key: roleplays     # how current is computed: see the table in protocols/okr-planning.md
metric:                   # what is counted, in plain words
target:                   # number
current: 0                # number, updated by protocols
unit:                     # scenes | sessions | words | characters | % | ...
measure_by:               # how and when it is measured
due:                      # = the objective's end
status: active            # active | closed
score:                    # 0.0–1.0, set at monthly review
calibration_note:
```

Rules: each objective has 2–4 key results and at least one `lag` key result tested at month end.
Every key result must be observable. Rewrite vague aims ("think like a native") as behaviour
("in role-plays, answer without switching to English in 80% of turns").

### task

```yaml
type: task
created:
objective: "[[2026-11-O1]]"   # REQUIRED, exactly one objective
kr: "[[2026-11-KR1-2]]"       # optional
done: false
due:
week: 2026-W45                # ISO week of `due`
effort_min: 30
task_type: practice           # learn | practice | test | input | output | review | setup
origin: agent                 # agent | learner
```

Daily routines (card review, daily input) are logged in the daily note, not created as tasks.

### daily

```yaml
type: daily
created:
date:
minutes: 0                # total study minutes
cards_reviewed: 0
cards_correct: 0
input_min: 0              # minutes of comprehensible input
output_count: 0
confidence:               # 1–5
fun:                      # 1–5
```

### review

```yaml
type: review
created:
period: weekly            # weekly | monthly | quarterly
cycle: 2026-W45           # weekly YYYY-Www | monthly: the plan month's cycle | quarterly q1, q2
start:
end:
minutes: 0                # total study minutes in the period
confidence_avg:
fun_avg:
score:                    # monthly and quarterly: mean objective score
```

### word

```yaml
type: word
created:
pinyin: dǎbāo
meaning: to pack food to go; takeaway
pos: verb                 # noun | verb | adj | adv | measure | pron | num | particle | conj | prep | phrase | other
characters: [打, 包]
hsk:                      # HSK 3.0 level 1–6; 7 = band 7–9; empty if unknown
scenes: ["[[ordering-food]]"]
patterns: []
example: 可以打包吗？
example_pinyin: Kěyǐ dǎbāo ma?
example_en: Can I get this to go?
recognize: false          # knows meaning when reading or hearing it
pronounce_ok: false       # passed a pronunciation check (agent or teacher)
can_use: false            # used correctly in the learner's own output
handwrite: false          # tracked only when writing_mode is handwriting or both
box: 1                    # review box 1–5
next_review:
last_review:
lapses: 0
source:
```

### pattern

```yaml
type: pattern
created:
pattern: 可以…吗？
pinyin: kěyǐ … ma?
meaning: Can I / may I …?
structure: 可以 + verb phrase + 吗？
function: asking permission
grammar_point:
hsk:
scenes: []
words: []
example: 可以打包吗？
example_pinyin: Kěyǐ dǎbāo ma?
example_en: Can I get this to go?
recognize: false
pronounce_ok: false
can_use: false
box: 1
next_review:
last_review:
lapses: 0
```

### scene

```yaml
type: scene
created:
title_zh: 点餐
title_en: Ordering food
category: food            # food | shopping | transport | directions | lodging | health | social | work | services | emergency | other
objectives: ["[[2026-11-O1]]"]  # every objective this scene served; add new ones, never remove
status: planned           # planned | learning | passed
difficulty: 1             # 1 basic | 2 standard | 3 complex
patterns: []              # at least 5: what the learner says
words: []
practice_count: 0
best_rounds: 0            # most dialogue turns completed in one role-play
accuracy:                 # 0–1, key-information accuracy in the latest test
last_practiced:
passed_on:
box: 1
next_review:
```

Body sections (required): Goal · What I say · What I might hear (at least 5 responses) ·
Culture & etiquette · Curveballs · Pass criteria · Practice log.

### source (Inbox)

```yaml
type: source
created:
topic:
media_type: video         # doc | video | audio | web
url:
attachment:               # "[[file.pdf]]" in 09-attachments
tags: []
level: ok                 # easy (understand 95%+) | ok (about 80–95%, good for study) | hard (under 80%, save for later)
status: new               # new | in-progress | done
minutes: 0                # minutes spent on it
related: []               # links to words, patterns, scenes
```

### output

```yaml
type: output
created:
date:
output_type: role-play    # speaking | writing | role-play | test | pronunciation-check | reflection | real-world
objective:
scene:
task:
audio:                    # "[[recording.m4a]]"
feedback_by:              # agent | teacher | self
error_types: []
rounds:                   # dialogue turns completed (role-play, test)
accuracy:                 # 0–1
fixed_task: false         # true for the monthly fixed recording
check:                    # month-end checks only: reading-check | writing-check | pron-accuracy
confidence:               # 1–5
fun:                      # 1–5
```

Body sections: Task · My output · Feedback · Corrected version · Next focus.

## 4. Error types

| Value | Meaning |
|---|---|
| `tone` | wrong tone, including tone sandhi |
| `aspiration` | b/p, d/t, g/k, j/q, zh/ch, z/c confused |
| `retroflex` | zh ch sh r confused with z c s or j q x |
| `initial` | other wrong initial consonant |
| `final` | wrong final, including -n/-ng and ü |
| `word-order` | for example time or place after the verb |
| `measure-word` | wrong or missing measure word |
| `le` | 了 missing or misused |
| `complement` | result, direction, degree or potential complement |
| `word-choice` | wrong word or collocation |
| `character` | wrong or miswritten character |
| `grammar-other` | any other grammar error |
| `pragmatics` | register, politeness, cultural fit |
| `fluency` | long pauses, restarts, switching to English |

## 5. Review scheduling (Leitner boxes)

Words, patterns and scenes share one rule, so every agent schedules the same way.

| Box | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Days until next review | 1 | 3 | 7 | 14 | 30 |

- **New item:** `box: 1`, `next_review:` today (it is studied today).
- **Correct:** `box` + 1 (max 5); `next_review` = today + days for the new box.
- **Wrong:** `box: 1`; `next_review` = tomorrow; `lapses` + 1.
- Always set `last_review` to today.

## 6. Mastery flags

| Flag | Set to true when |
|---|---|
| `recognize` | `box` is 3 or higher (two correct reviews in a row). It goes back to false when the item falls below box 3 |
| `pronounce_ok` | it passes a pronunciation check (agent speech-to-text check or teacher) |
| `can_use` | the learner uses it correctly in an output |
| `handwrite` | the learner writes it correctly from memory (checked from a photo or by a teacher) |

A word is **mastered** when `recognize`, `pronounce_ok` and `can_use` are all true
(plus `handwrite` when `writing_mode` is `handwriting` or `both`).
A scene is **passed** when its pass criteria are met in a test; set `status: passed` and `passed_on`.
