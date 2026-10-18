---
type: protocol
version: 0.2.0
updated: 2026-10-18
---
# Protocol: Log Output

**Runs when** the learner shares something they said or wrote, asks for a pronunciation check, reports
using Chinese in real life, or another protocol needs to log practice.
**Writes** one note in `08-output/`; mastery flags; today's daily log.

## 1. Identify

`output_type`: speaking, writing, role-play, test, pronunciation-check, reflection, real-world.
Link `objective`, `scene` and `task` when they apply.

## 2. Get the content

- **Writing:** the text.
- **Speaking:** a transcript. If the learner sends audio and you can transcribe it, do so. If you can't,
  say so and ask them to read it again into Chinese voice input and paste the text, or to add a teacher's notes.
  Save audio in `09-attachments/` as `{date}-{slug}.{ext}` and link it in `audio`.
- **Real-world:** what happened, in their own words (English is fine), and what they said in Chinese if they remember.

## 3. Feedback

- `feedback_by: agent`. If the learner pastes a teacher's notes, use them and set `feedback_by: teacher`;
  self-assessment only → `self`.
- At most 3 corrections, the most important first: what was wrong, the right form, a one-line reason.
- Then the full corrected version, with pinyin.
- `error_types`: every type that occurred (schemas.md section 4).
- `accuracy` for role-plays, tests and pronunciation checks.
- Praise one specific thing that was right.
- Real-world attempts: praise the attempt first; feedback is optional and short.

## 4. Pronunciation check (speech-to-text method)

Use this whenever the learner wants pronunciation feedback and no teacher is involved.

1. Choose 5–10 items: lines from the current scene or recently learned words, plus one or two
   minimal-pair sentences. In a minimal pair both versions make sense, so the recogniser can't guess
   the right one from context:

| Sentence A | Sentence B | Contrast |
|---|---|---|
| 我想买这个。 Wǒ xiǎng mǎi zhège. | 我想卖这个。 Wǒ xiǎng mài zhège. | tone: mǎi / mài |
| 我要汤。 Wǒ yào tāng. | 我要糖。 Wǒ yào táng. | tone: tāng / táng |
| 我要睡觉。 Wǒ yào shuìjiào. | 我要水饺。 Wǒ yào shuǐjiǎo. | tones |
| 他的肚子很大。 Tā de dùzi hěn dà. | 他的兔子很大。 Tā de tùzi hěn dà. | aspiration: d / t |
| 我有四十块。 Wǒ yǒu sìshí kuài. | 我有十四块。 Wǒ yǒu shísì kuài. | s / sh |

2. The learner switches on Mandarin (Simplified Chinese) voice input, reads each item once at normal
   speed, and pastes exactly what was typed. For a minimal pair, tell them which sentence to read.
3. Compare character by character. Same = pass. Different: compare the pinyin of the intended text with the
   recognised text and name the likely problem (tone, initial, final, aspiration, retroflex).
4. Be honest about the method: a pass means the recogniser understood them, not that the pronunciation is
   perfect. A mismatch is a reliable sign of a problem.
5. `accuracy` = passed ÷ total. For the target word or pattern of each item: passed → `pronounce_ok: true`,
   failed → `pronounce_ok: false`.
6. For each problem give one concrete drill: the minimal pair said slowly, then inside a sentence.

## 5. Update the library

- `can_use: true` for words and patterns the learner used correctly in this output.
- Words the learner needed but didn't know: offer to add them (add-to-library).

## 6. Write

`08-output/{date}-{output_type}-{slug}.md` from the template, with the sections Task, My output, Feedback,
Corrected version, Next focus. Add `confidence` and `fun` if the learner gives them.
Add 1 to today's `output_count`, and recompute `current` on key results this output affects.
