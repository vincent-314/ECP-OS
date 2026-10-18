---
type: scene
created: "{{date}}"
title_zh:
title_en:
category:
objectives: []
status: planned
difficulty: 1
patterns: []
words: []
practice_count: 0
best_rounds: 0
accuracy:
last_practiced:
passed_on:
box: 1
next_review:
---
# {{title}}

## Goal
<!-- What the learner must get done in this situation. -->

## What I say
| Chinese | Pinyin | English |
|---|---|---|
| | | |

## What I might hear
<!-- At least 5 things the other person may say. This is the listening half of the scene. -->
| Chinese | Pinyin | English |
|---|---|---|
| | | |

## Culture & etiquette

## Curveballs
<!-- Things that can go wrong, and what to say. -->

## Pass criteria
- [ ] 

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
