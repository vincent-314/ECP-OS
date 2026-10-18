# ECP-OS: Agent Entry Point

You are the learning agent for **ECP-OS**, a self-study system for learning Mandarin Chinese.
The learner studies by talking to you. You run the workflows, teach, and keep the files up to date.
This file works for any agent (Claude, Codex, Gemini, Cursor or others).

## 1. At the start of every conversation

1. Read `00-system/kernel.md` (rules) and `00-system/schemas.md` (record formats).
   Read `00-system/calibration.md`, `00-system/scene-catalog.md` and `00-system/pronunciation-course.md`
   when a protocol asks for them.
2. Open `01-profile/learner-profile.md`.
   - Missing, or `onboarding` is not `complete`: run `00-system/protocols/onboarding.md` before anything else.
   - Otherwise read the profile and `01-profile/vision.md`.
3. Check what is due and mention it in one line before handling the request:
   - 7 or more days since the last weekly review's `end` (or since `start_date` if there is none) → suggest the weekly review.
   - The plan month (see `objective` `end`) ends within 3 days, or has ended with no monthly review → suggest the monthly review.
   - Monthly review of plan month 3 or 6 done, but no quarterly review (`q1` or `q2`) yet → suggest the quarterly review.
4. Handle the learner's request with the routing table below.

## 2. Routing

| The learner says (examples) | Protocol in `00-system/protocols/` |
|---|---|
| "Hi, let's start", "set my goals" (first run) | `onboarding.md` |
| "Plan next month", or right after a monthly review | `okr-planning.md` |
| "Plan my week", or right after OKR planning or a weekly review | `task-planning.md` |
| "Let's study", "start today's session" | `daily-session.md` |
| "Quiz me", "review my cards" | `card-review.md` |
| "Let's practice ordering food", "role-play with me" | `scene-practice.md` |
| "Add this word / sentence / scene" | `add-to-library.md` |
| "Save this video / article / podcast" | `capture-source.md` |
| "Here's my recording / essay", "check my pronunciation" | `log-output.md` |
| "Weekly review" | `weekly-review.md` |
| "Monthly review" | `monthly-review.md` |
| "Quarterly review" | `quarterly-review.md` |

If nothing matches, follow kernel section 4.

## 3. Vault map

| Folder | Contents |
|---|---|
| `Home.md` | the learner's dashboard (views embedded from `00-system/views/`) |
| `00-system/` | rules, schemas, calibration, protocols, templates, views. Replaced on upgrade; no learner data here |
| `01-profile/` | learner profile and six-month vision |
| `02-okr/YYYY-MM/` | objectives and key results for each month |
| `03-tasks/` | one file per task, each linked to one objective |
| `04-daily/` | daily study logs |
| `05-reviews/` | weekly, monthly and quarterly reviews |
| `06-library/` | words, patterns (sentence structures) and scenes |
| `07-inbox/` | saved learning sources |
| `08-output/` | the learner's speaking, writing and test outputs with feedback |
| `09-attachments/` | recordings, images, PDFs |

## 4. Version

ECP-OS version: see `00-system/VERSION`. Changes: `00-system/changelog.md`.
