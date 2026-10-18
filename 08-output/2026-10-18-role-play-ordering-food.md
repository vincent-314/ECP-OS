---
type: output
created: 2026-10-18
sample: true
date: 2026-10-18
output_type: role-play
objective: "[[2026-10-O1]]"
scene: "[[ordering-food]]"
task: "[[2026-10-18-roleplay-ordering-food-x4]]"
audio:
feedback_by: agent
error_types: [word-order, tone, fluency]
rounds: 5
accuracy: 0.8
fixed_task: false
confidence: 3
fun: 4
---
# Role-play: ordering food (1)

## Task
The agent plays the waiter. Order rice and a dish that is not spicy, then pay.

## My output
| Turn | Waiter (agent) | Me |
|---|---|---|
| 1 | 你好，几位？ | 一个人。 |
| 2 | 现在点菜吗？ | 对，我要米饭一份。 |
| 3 | 要辣的吗？ | 不要辣。 |
| 4 | 还要别的吗？ | 不要了，谢谢。 |
| 5 | (I call the waiter) | 服务员，买单！ |
| 6 | 扫码还是现金？ | (switched to English) |

Pronunciation check for turn 5: I read the line into a Chinese voice-input keyboard. It typed 卖单 instead of 买单.

## Feedback
- **Word order.** Number + measure word go before the noun: 一份米饭, not 米饭一份.
- **Tone.** 买 is mǎi (third tone, "buy"); it came out as 卖 mài ("sell"). Practice the pair 买 mǎi / 卖 mài.
- **Listening.** 扫码还是现金？ means "QR code or cash?". It is now in the scene's "What I might hear".

## Corrected version
- 对，我要一份米饭。 Duì, wǒ yào yí fèn mǐfàn.
- 服务员，买单！ Fúwùyuán, mǎidān! (mǎi, third tone)
- 扫码。 Sǎomǎ. (QR code, please.)

## Next focus
买 / 卖 minimal pair; number + measure word + noun; listen for 扫码还是现金？
