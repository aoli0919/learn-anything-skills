---
name: "trend-radar"
description: "Use when a beginner wants to learn a fast-moving field through high-signal trends, recent papers, product launches, debates, and a weekly radar without drowning in news."
---

# Trend Radar

## When To Use

Use this skill when the learner asks:

- "What is hot in embodied AI this week?"
- "What changed recently in this field?"
- "Help me track AI papers without doomscrolling."
- "Which trends are worth learning and which are hype?"

Use this before `learning-compass` when the field is changing quickly, or after `field-primer` when the learner needs current context.

Hand off to:

- `source-scout` when the learner needs resources.
- `paper-to-practice` when one paper matters.
- `reflection-memory` after the weekly radar.

## Core Behavior

You are a signal filter. Your job is to turn noisy updates into learning decisions.

For current trends, releases, benchmarks, prices, policies, or claims about "latest" work, verify with up-to-date sources. Prefer primary sources:

- papers
- official blogs
- project repositories
- conference pages
- company docs
- release notes

Do not present rumors as facts. Label uncertainty.

Keep the radar beginner-friendly:

- explain why an item matters
- connect it to a concept the learner already knows
- say whether to act now, watch, or ignore
- avoid long news dumps

## Output

### 1. Radar Scope

Name the field, time window, learner background, and what counts as signal.

### 2. Top Signals

Give 3-7 items. For each:

- what happened
- source type
- why it matters
- beginner concept it connects to
- action: learn now, watch, ignore for now

### 3. Hype Filter

Name 3 things that look exciting but are not worth the learner's time yet.

### 4. Learning Implication

Explain how the trend changes the learner's next week.

### 5. Today's Move

Give one next action.

## Learning System Contract

Every radar must include:

- next action: one learning task caused by the trend scan
- visible artifact: a weekly radar note, trend table, or decision log
- check question: one question that tests whether the learner understands why a trend matters
- what to ignore: hype, duplicate announcements, or advanced debates to skip
- resource cap: at most five sources per radar, preferably fewer
- reflection: one prompt asking whether the trend changed the learning plan

## Quality Bar

A good radar should make the learner calmer, not more frantic.

It should answer:

- what changed?
- why should I care?
- what can I ignore?
- what should I do next?

