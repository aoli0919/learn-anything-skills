# Contributing

Thank you for improving Learn Anything Skills.

The best contributions make the system more useful for real beginners.

## What To Contribute

Good pull requests usually do one of these:

- add a domain example, such as embodied AI, robotics, neuroscience, finance, or systems programming
- improve a skill prompt with clearer beginner behavior
- add a validation rule
- add a project template
- rewrite vague learning advice into concrete actions
- add a realistic learning log

## Content Standards

Please keep contributions:

- concrete
- beginner-friendly
- honest about difficulty
- free of fake guarantees
- light on jargon unless the jargon is explained

Avoid:

- huge resource dumps
- motivational filler
- "just read these 50 papers"
- pretending every learner has the same background
- claiming a topic can be mastered in a few days

## Skill Format

Each skill lives in:

```text
skills/<skill-name>/SKILL.md
```

Every `SKILL.md` needs YAML frontmatter:

```yaml
---
name: "skill-name"
description: "When to use this skill."
---
```

Run validation before submitting:

```bash
python3 scripts/validate_skills.py
```

## Pull Request Checklist

- [ ] The skill has a clear trigger.
- [ ] The output tells the learner what to do next.
- [ ] The advice is specific enough for a beginner.
- [ ] No TODO placeholders remain.
- [ ] `python3 scripts/validate_skills.py` passes.

