---
type: protocol
version: 0.2.0
updated: 2026-10-18
---
# Protocol: Capture Source

**Runs when** the learner shares a link, file or text to keep ("Save this video"), or reports using a source.
**Writes** one note in `07-inbox/`; files in `09-attachments/` when the learner provides them.

## Save a new source

1. **Collect** the link, or the file (save it in `09-attachments/` and link it in `attachment`).
   Ask only for what you can't see yourself: what it's about, how long it is.
2. **Describe:** `topic` (one line), `media_type` (doc, video, audio, web), and 1–3 `tags`
   (food, travel, daily-life, culture, work, pronunciation, grammar, listening, reading, fun,
   or the learner's interests).
3. **Level:** if you can read the content or a transcript, estimate the share of words the learner knows
   (word bank, `recognize: true`): 95%+ → `easy`, 80–95% → `ok`, under 80% → `hard`.
   If you can't read it, use `ok` and ask the learner after they have tried it.
4. **Write** `07-inbox/{today}-{slug}.md` from the template with `status: new`. Body: a 2–3 line summary,
   and "Useful words and lines" if you could read it.
5. **Link** matching scenes in `related`. Offer to add up to 5 useful words (add-to-library).
6. Keep the link. Never download or copy copyrighted media for the learner.

## When the learner uses a source

Set `status` (`in-progress` or `done`), add the minutes to the source's `minutes` and to today's
`input_min`. If it turned out too hard, set `level: hard` and suggest an easier source.
