---
type: system
updated: 2026-10-18
---
# Changelog

## 0.2.0 (2026-10-18)
- All 12 protocols written: onboarding, okr-planning, task-planning, daily-session, card-review,
  scene-practice, add-to-library, capture-source, log-output, weekly-review, monthly-review, quarterly-review.
- New `scene-catalog.md`: 40 default scenes in three difficulty levels.
- New `pronunciation-course.md`: 8 lessons for plan month 1, with text-only listening checks.
- New optional `tools/ecp.py`: validates records and computes key-result progress (Python 3, no packages).
- Output property `check` marks month-end checks.
- Scenes use `objectives` (a list): a scene carried into a new month keeps its earlier objectives,
  so closed key results never change.
- Task `week` = ISO week of its `due` date. Recalibration scales next month's *planned* target.
- Kernel: sound comes from the learner's device (text-to-speech) when the agent can't produce audio.
- Plan months now start on the learner's `start_date` (not calendar months); objectives have `start` and `end`.
- Key results have `metric_key`, so every agent computes progress the same way.
- Profile has `onboarding_round`, so onboarding can resume.
- `recognize` is true exactly when `box` ≥ 3. New output type `real-world`.

## 0.1.0 (2026-10-18)
- Vault skeleton: folders, kernel, schemas, calibration, templates, Bases views, Home dashboard.
- Sample data (flagged `sample: true`): one scene, ten words, five patterns, one month of OKR.
- Protocols: not yet written.
