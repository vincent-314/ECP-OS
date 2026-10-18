---
type: objective
created: "{{date}}"
cycle:
month:
start:
end:
code:
title:
area:
priority:
status: active
score:
---
# {{title}}

## Why this matters

## Key results

```base
filters:
  and:
    - file.inFolder("02-okr")
    - 'type == "key-result"'
    - file.hasLink(this.file)
views:
  - type: table
    name: Key results
    order:
      - code
      - title
      - kind
      - current
      - target
      - unit
      - due
      - score
    sort:
      - property: code
        direction: ASC
```

## Tasks

```base
filters:
  and:
    - file.inFolder("03-tasks")
    - file.hasLink(this.file)
views:
  - type: table
    name: Tasks
    order:
      - file.name
      - done
      - due
      - task_type
      - kr
    sort:
      - property: due
        direction: ASC
```
