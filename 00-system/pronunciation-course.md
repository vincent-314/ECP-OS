---
type: system
version: 0.2.0
updated: 2026-10-18
---
# Pronunciation Course (plan month 1)

Eight short lessons (15–20 minutes each) for plan month 1, usually one per study day in weeks 1–2,
alongside the first scenes. okr-planning gives month 1 a pronunciation objective; task-planning turns
the lessons into tasks (`task_type: learn`). Each lesson: **listen → imitate → check**.

## Before lesson 1: set up sound

You may not be able to produce audio. The learner needs two things:
1. **Model sounds:** a pinyin chart with audio (the learner finds one they like; save it with capture-source),
   and text-to-speech on their phone or computer with a Chinese voice, to hear any Chinese line you write.
   If you have a voice mode, use it as well.
2. **Mandarin (Simplified Chinese) voice input**, for pronunciation checks (log-output section 4).

**Listening check that works in text:** give characters only. A beginner can't read them, so they play each one
with text-to-speech and write the pinyin with tone numbers. Then you check.

## Lessons

| # | Content | Imitate | Check |
|---|---|---|---|
| 1 | **The tones.** 1st high and level, 2nd rising, 3rd low (dips and rises when alone), 4th falling, neutral tone short and light. | mā má mǎ mà ma with a hand gesture for each tone; then bā bá bǎ bà | listening: 妈 麻 马 骂 八 拔 把 爸 汤 糖 → pinyin with tone numbers |
| 2 | **Simple finals and lip/tongue-tip initials.** a o e i u ü; b p m f d t n l. Aspiration: p and t release a puff of air (a paper in front of the mouth moves), b and d don't. | 爸 bà / 怕 pà; 肚子 dùzi / 兔子 tùzi | voice input: the two pairs |
| 3 | **g k h and j q x.** After j q x, ü is written u (ju qu xu). | 哥 gē / 科 kē; 鸡 jī / 七 qī / 西 xī | listening: 哥 科 喝 鸡 七 西 去 绿 |
| 4 | **zh ch sh r vs z c s.** Tongue tip curled back vs behind the teeth. | 是 shì / 四 sì; 十 shí; 吃 chī / 次 cì; 日 rì | voice input: 我有四十块。 / 我有十四块。 |
| 5 | **Compound finals and nasals.** ai ei ao ou; an en ang eng ong; -n (tongue touches behind the teeth) vs -ng (back of the tongue). | 三 sān / 桑 sāng; 陈 chén / 成 chéng | listening: 三 桑 陈 成 安 昂 |
| 6 | **Tone changes.** 3rd + 3rd → 2nd + 3rd (你好 sounds ní hǎo); a 3rd tone before other tones stays low. 不 → bú before a 4th tone (不是 bú shì). 一 → yí before a 4th tone (一个 yí gè), yì before others (一天 yì tiān). | 你好, 可以, 不是, 不要, 一个, 一天 | voice input: 你好！我不要这个。 |
| 7 | **Two-syllable tone pairs (20 combinations).** See the table below. | read each word twice, slowly then normally | voice input: 8 words from the table |
| 8 | **Putting it together.** Short sentences from the first scene. | the scene's "What I say" lines | full pronunciation check (log-output section 4), 10 items, `check: pron-accuracy`: the month-1 baseline |

## The 20 tone combinations

| 1st → | 2nd → | 3rd → | 4th → |
|---|---|---|---|
| 1-1 飞机 fēijī | 2-1 明天 míngtiān | 3-1 老师 lǎoshī | 4-1 汽车 qìchē |
| 1-2 中国 Zhōngguó | 2-2 学习 xuéxí | 3-2 美国 Měiguó | 4-2 问题 wèntí |
| 1-3 身体 shēntǐ | 2-3 苹果 píngguǒ | 3-3 你好 nǐ hǎo | 4-3 电脑 diànnǎo |
| 1-4 音乐 yīnyuè | 2-4 学校 xuéxiào | 3-4 可是 kěshì | 4-4 再见 zàijiàn |
| 1-0 妈妈 māma | 2-0 朋友 péngyou | 3-0 姐姐 jiějie | 4-0 爸爸 bàba |

Log each lesson's check with log-output (`output_type: pronunciation-check`, or `test` for listening checks)
and note problems in the daily log. Learners who aren't complete beginners (placement) skip lessons they pass.
