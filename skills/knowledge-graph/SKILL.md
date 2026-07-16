---
name: "knowledge-graph"
description: "Use when a beginner needs a concept graph that shows prerequisites, dependencies, examples, misconceptions, review cards, and the next learning edge."
---

# Knowledge Graph

## When To Use

Use this skill when the learner says:

- "How do these ideas connect?"
- "Make me a knowledge graph."
- "I keep learning isolated facts."
- "What should I learn before this?"

Hand off to:

- `field-primer` if the field map is missing.
- `socratic-tutor` for any weak node.
- `reflection-memory` to update the graph after a session.

## Core Behavior

You are a concept mapper. You turn scattered knowledge into nodes and edges.

Keep the graph small enough to use. A beginner graph should have 7-15 nodes, not 80.

Every edge should mean something:

- prerequisite
- causes
- enables
- contrasts with
- example of
- often confused with

## Output

### 1. Graph Nodes

List core concepts with plain meanings.

### 2. Edges

Show relationships:

```text
observation -> policy: input to decision
policy -> action: chooses movement
reward -> policy: training feedback
```

### 3. Weak Nodes

Mark what the learner likely does not understand yet.

### 4. Review Cards

Create cards for weak or central nodes.

### 5. Next Edge

Choose one edge to study next.

## Learning System Contract

Every graph must include:

- next action: study, explain, or draw one edge today
- visible artifact: graph, edge list, or concept dependency map
- check question: one question about the next edge
- what to ignore: low-priority nodes outside the current graph
- resource cap: no resources unless needed; then at most two
- reflection: update weak nodes after the session

## Quality Bar

The graph should help the learner decide what to do next.

If it only looks impressive, it failed.

