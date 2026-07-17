# Learn Anything Skills

[![Validate](https://github.com/aoli0919/learn-anything-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/aoli0919/learn-anything-skills/actions/workflows/validate.yml)
![MIT](https://img.shields.io/badge/license-MIT-green)
![Skills](https://img.shields.io/badge/skills-100-blue)
![Beginner First](https://img.shields.io/badge/beginner--first-yes-orange)

A beginner-first agent skill pack that turns "I want to learn X" into a 30-day path, tutor loop, projects, and learning memory.

![Terminal demo](assets/demo-terminal.svg)

## At A Glance

![Learning loop](assets/learning-loop.svg)

![100 skill map](assets/skill-map.svg)

## You Bring

- a topic you want to learn
- your current background
- your time budget
- what confused you last time

## The Skills Return

- a 30-day learning path
- today's first task
- beginner concept maps
- active check questions
- small project cards
- paper-to-practice notes
- reflection memory for tomorrow
- 100 specialized learning operators for papers, codebases, math, robotics, research, writing, verification, and metacognition

## Mini Demo

Input:

```text
$learning-compass I want to learn embodied AI.
I know Python and basic ML. I can spend one hour a day.
```

Output:

```text
North Star:
In 30 days, build a tiny simulated agent and explain its perception-action loop.

Today:
Draw a robot arm picking up a mug. Label observation, action, policy,
feedback, and one failure case.

Done when:
You can explain why incomplete observation can cause a bad action.

Reflection:
Log what stayed fuzzy. If state vs observation is still unclear tomorrow,
slow down and use $socratic-tutor before starting a project.
```

## Start Today: 45 Minutes

Copy this:

```text
$learning-compass I want to learn embodied AI.
My background: basic Python and a little machine learning.
Time budget: 45 minutes a day.
Give me today's first task, completion standard, check question, and reflection prompt.
```

Your first artifact should be small: one diagram, one concept card, one toy script, or one learning log.

## Why Star This

Star this if you want:

- AI learning help that produces artifacts, not just answers
- reusable learning loops for hard technical fields
- beginner-friendly domain packs, starting with embodied AI
- skills you can install, validate, remix, and contribute to

This repo ships skills, templates, examples, validation, install scripts, and domain defaults. It is meant to be a usable learning system, not only a prompt collection.

## Why This Exists

Most beginners do not fail because they are lazy. They fail because the first week of a new field is noisy:

- too many resources
- too many unexplained words
- no sense of what matters first
- no feedback after reading
- no small project to make the knowledge stick
- no memory of what they tried last time

Learn Anything Skills turns that mess into a repeatable loop:

```text
Goal -> Map -> Learn -> Test -> Build -> Reflect -> Next Step
```

The point is not to make learning look impressive. The point is to make the next action obvious.

## Quick Start

Clone the repository:

```bash
git clone https://github.com/aoli0919/learn-anything-skills.git
cd learn-anything-skills
```

Install the skills into your Codex skills folder:

```bash
python3 scripts/install.py
```

Check that every skill is valid:

```bash
python3 scripts/validate_skills.py
```

Read the usage guide:

- [Usage Guide](docs/USAGE.md)
- [Embodied AI Domain Pack](domains/embodied-ai.md)
- [Project Pitch](docs/PITCH.md)
- [Launch Kit](docs/LAUNCH.md)
- [100 Skill Index](docs/SKILL_INDEX.md)
- [100 Skills Launch Note](docs/100_SKILLS_LAUNCH.md)

Then ask your agent something like:

```text
I am new to embodied AI. I know basic Python and a little machine learning.
Use the learning system to give me a 30-day plan and today's first task.
```

## The 100 Skills

The library is grouped by what the learner is trying to do. Start with the core loop, then pull in specialist skills only when needed.

| Area | Count | Use it for |
| --- | ---: | --- |
| Core loop + hot extensions | 14 | planning, concept maps, tutoring, projects, reflection, source scouting |
| AI research and papers | 10 | arXiv, literature review, benchmarks, datasets, reproductions |
| Embodied AI and robotics | 11 | simulation, RL intuition, robot policies, tactile sensing, VLA papers |
| Foundations | 11 | math gaps, Python drills, algorithms, probability, ML concepts |
| Learning operations | 10 | daily plans, spaced review, flashcards, focus, deliberate practice |
| Communication | 10 | teaching, blog posts, XHS notes, portfolios, presentations |
| Career and research | 12 | PhD workflows, internships, market research, product judgment |
| Tools and data | 12 | docs, APIs, notebooks, data analysis, debugging, tests |
| Trust and metacognition | 10 | claim checks, source audits, privacy, safety, decision journals |

Browse the full table: [100 Skill Index](docs/SKILL_INDEX.md).

Recommended first path:

```text
$learning-compass -> $field-primer -> $socratic-tutor -> $project-lab -> $reflection-memory
```

When you get stuck, use `$stuck-debugger`. When the field is moving fast, use `$trend-radar`. When you want proof that you understand, use `$exam-simulator`.

## Example: Embodied AI

See [examples/embodied-ai-30-day-plan.md](examples/embodied-ai-30-day-plan.md).
For reusable domain defaults, see [domains/embodied-ai.md](domains/embodied-ai.md).

A beginner does not need to start by reading every robotics paper. A better first month is:

- understand the perception-action loop
- learn what policies, observations, actions, rewards, simulation, and embodiment mean
- reproduce one toy environment
- read one paper slowly
- build one tiny agent
- keep a daily log of what was confusing

More examples:

- [AI paper reading loop](examples/ai-paper-reading.md)
- [Investing thesis learning loop](examples/investing-thesis-log.md)
- [Hot skill extensions gallery](examples/hot-skill-extensions-gallery.md)
- [Hot skill design notes](docs/HOT_SKILL_NOTES.md)
- [100 skills launch note](docs/100_SKILLS_LAUNCH.md)

## Installation Details

By default, `scripts/install.py` copies every folder under `skills/` into:

```text
~/.codex/skills/
```

You can override the target:

```bash
python3 scripts/install.py --target /path/to/skills
```

Dry run:

```bash
python3 scripts/install.py --dry-run
```

## Repository Structure

```text
learn-anything-skills/
  skills/
    learning-compass/
    field-primer/
    ...
    curiosity-engine/
    100 skill folders total
  assets/
    learning-loop.svg
    skill-map.svg
  examples/
  docs/
  templates/
  scripts/
```

## Design Principles

- Start from the learner's current state, not an ideal syllabus.
- Use concrete examples before abstract definitions.
- Prefer one useful next action over a huge resource list.
- Make confusion visible instead of treating it as failure.
- Turn reading into cards, cards into checks, checks into projects.
- Keep a learning memory so every session compounds.

## Who This Is For

This project is for:

- beginners entering a technical field
- students who read a lot but build little
- researchers crossing into a new domain
- self-learners who want an AI tutor with structure
- people who need a daily feedback loop, not another bookmark folder

## Not A Promise

This does not magically make hard fields easy. It makes the next learning move smaller, clearer, and less lonely.

## Contributing

Contributions are welcome. Good contributions usually add:

- a better beginner path for a specific field
- a clearer example
- a stricter validation rule
- a project template
- a learning log format that helps people keep going

See [CONTRIBUTING.md](CONTRIBUTING.md).
