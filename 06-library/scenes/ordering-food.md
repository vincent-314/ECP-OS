---
type: scene
created: 2026-10-18
sample: true
title_zh: 点餐
title_en: Ordering food
category: food
objectives: ["[[2026-10-O1]]"]
status: learning
difficulty: 1
patterns: ["[[我要…]]", "[[有没有…？]]", "[[不要…]]", "[[可以…吗？]]", "[[…多少钱？]]"]
words: ["[[菜单]]", "[[服务员]]", "[[点菜]]", "[[辣]]", "[[米饭]]", "[[打包]]", "[[买单]]", "[[扫码]]", "[[份]]", "[[堂食]]"]
practice_count: 1
best_rounds: 5
accuracy: 0.8
last_practiced: 2026-10-18
passed_on:
box: 1
next_review: 2026-10-19
---
# 点餐 Ordering food

## Goal
Order a meal in a casual restaurant: say how many people, order food, say how spicy you want it,
ask to take leftovers, and pay.

## What I say
| Chinese | Pinyin | English |
|---|---|---|
| 我要一份米饭。 | Wǒ yào yí fèn mǐfàn. | I'll have a portion of rice. |
| 有没有英文菜单？ | Yǒu méiyǒu Yīngwén càidān? | Do you have an English menu? |
| 不要辣。 | Bú yào là. | Not spicy, please. |
| 可以打包吗？ | Kěyǐ dǎbāo ma? | Can I get this to go? |
| 一共多少钱？ | Yígòng duōshao qián? | How much is it altogether? |
| 服务员，买单！ | Fúwùyuán, mǎidān! | Excuse me, the bill please! |

## What I might hear
| Chinese | Pinyin | English |
|---|---|---|
| 几位？ | Jǐ wèi? | How many people? |
| 现在点菜吗？ | Xiànzài diǎncài ma? | Ready to order? |
| 要辣的吗？ | Yào là de ma? | Do you want it spicy? |
| 喝点什么？ | Hē diǎn shénme? | Anything to drink? |
| 还要别的吗？ | Hái yào bié de ma? | Anything else? |
| 堂食还是打包？ | Tángshí háishi dǎbāo? | For here or to go? |
| 扫码还是现金？ | Sǎomǎ háishi xiànjīn? | QR code or cash? |

## Culture & etiquette
- Many restaurants let you order by scanning a QR code on the table (扫码点餐).
- Calling out 服务员 or 你好 to get attention is normal. Tipping is not expected.
- Taking leftovers home (打包) is common.
- Paying by QR code is the default.

## Curveballs
- Sold out: 这个卖完了。 Zhège màiwán le. → 那我要这个。 Nà wǒ yào zhège. (Then I'll have this one.)
- Wrong dish: 这不是我点的。 Zhè bú shì wǒ diǎn de. (This isn't what I ordered.)

## Pass criteria
- [ ] A role-play of at least 6 turns with the agent as the waiter, without switching to English
- [ ] Handle one curveball chosen by the agent
- [ ] Key information (what, how many, spicy or not, paying) at least 90% accurate
- [ ] Understand every line in "What I might hear" at normal speed

## Practice log

```base
filters:
  and:
    - file.inFolder("08-output")
    - file.hasLink(this.file)
views:
  - type: table
    name: Practice log
    order:
      - date
      - output_type
      - rounds
      - accuracy
      - error_types
    sort:
      - property: date
        direction: DESC
```
