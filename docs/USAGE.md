# Usage Guide

This guide shows how to use the skills after installation.

## Basic Pattern

Use natural language. You do not need to remember exact commands.

```text
I want to learn <topic>.
My background is <what I know>.
My time budget is <time>.
Use the learning system to make a path and today's task.
```

## Which Skill To Ask For

### $learning-compass

Use when you do not know where to start.

```text
$learning-compass I want to learn embodied AI. I know Python and basic ML.
Give me a 30-day path and today's first task.
```

### $field-primer

Use when the field feels like jargon.

```text
$field-primer Explain embodied AI from zero with a beginner map and the first three concept cards.
```

### $socratic-tutor

Use when you want active checking.

```text
$socratic-tutor Teach me the difference between observation, state, action, and policy. Ask me questions one at a time.
```

### $paper-to-practice

Use when you have a paper, article, lecture, or repository.

```text
$paper-to-practice Use this paper. Extract the task setup, method cards, and a 2-hour toy reproduction.
```

### $project-lab

Use when you want to build something.

```text
$project-lab Give me a 2-hour embodied AI project that does not require hardware.
```

### $reflection-memory

Use when a session ends.

```text
$reflection-memory I learned observation, action, and policy today, but state is still fuzzy. Make a log and tomorrow's task.
```

## Full Learning Loop Example

Day 1:

```text
$learning-compass embodied AI. I know Python and basic ML. I can spend one hour a day.
```

Day 2:

```text
$field-primer Build me a beginner map of observation, action, policy, reward, environment, and simulation.
```

Day 3:

```text
$socratic-tutor Quiz me on observation versus state.
```

Day 4:

```text
$project-lab Give me a 2-hour gridworld project.
```

Day 5:

```text
$reflection-memory Turn what I did this week into review cards and next week's plan.
```

## How To Get Better Results

Tell the agent:

- what you already know
- what you want to be able to do
- how much time you have
- whether you prefer papers, projects, or conversation
- what confused you last time

Bad request:

```text
Teach me robotics.
```

Better request:

```text
I know Python and linear algebra, but I have never built a robot project.
I want to understand embodied AI papers enough to build toy reproductions.
I can spend 45 minutes a day.
Use the learning system and start with today's task.
```
