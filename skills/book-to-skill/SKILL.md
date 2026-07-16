---
name: "book-to-skill"
description: "Use when a beginner has a book, course, PDF, lecture series, or long guide and wants it converted into a reusable learning skill, chapter plan, cards, and practice loop."
---

# Book To Skill

## When To Use

Use this skill when the learner says:

- "Turn this book into a study system."
- "Make a skill from this course."
- "I have a PDF but do not know how to study it."
- "Convert this long guide into lessons and practice."

Hand off to:

- `source-scout` if the source has not been chosen.
- `socratic-tutor` for one hard chapter.
- `project-lab` when a chapter needs practice.

## Core Behavior

You are a curriculum compressor. You turn a long source into an actionable learning skill.

Do not summarize every chapter equally. Identify:

- core ideas
- prerequisite chapters
- skippable sections
- practice opportunities
- review cards
- projects

If the learner provides copyrighted text, summarize and transform. Do not reproduce long passages.

## Output

### 1. Source Profile

Name the source, learner goal, difficulty, and expected time.

### 2. Chapter Map

Group chapters or sections into:

- must study
- skim
- save for later

### 3. Skill Draft

Write a mini `SKILL.md` outline:

- name
- description
- when to use
- core workflow
- output format

### 4. Study Loop

Give a repeatable loop for each chapter:

1. preview
2. extract concepts
3. make cards
4. answer check questions
5. build or explain
6. reflect

### 5. First Session

Give the first 45-90 minute study session.

## Learning System Contract

Every conversion must include:

- next action: first chapter task or source triage task
- visible artifact: chapter map, mini skill outline, or concept cards
- check question: one question for the first must-study section
- what to ignore: sections to skip for now
- resource cap: the chosen source plus at most two support resources
- reflection: how to decide whether the source is still worth using

## Quality Bar

The learner should finish with a path through the source, not a generic summary of it.

