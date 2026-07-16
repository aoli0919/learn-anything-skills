# Example: 30-Day Embodied AI Starter Plan

This example shows what the learning system should produce for a beginner.

## Input

```text
I want to learn embodied AI. I know basic Python and a little machine learning,
but I have not studied robotics. I can spend about one hour a day.
Give me a 30-day self-learning plan and tell me what to do today.
```

## Learner Snapshot

You are not starting from zero, but you are probably missing the bridge between machine learning words and embodied systems.

Your advantage:

- you can write basic code
- you have seen ML ideas before
- you can learn through small experiments

Your likely gaps:

- robotics vocabulary
- control and feedback intuition
- how observations become actions
- why simulation is useful but limited

Risk:

- reading too many robotics papers before seeing a tiny agent move

## North Star

In 30 days, build a tiny simulated agent, explain its observation-action-policy loop, and write a one-page note comparing hand-coded behavior, imitation learning, and reinforcement learning at a beginner level.

## Field Map

### Embodiment

The agent has a body or body-like constraints. It cannot just "think"; it has sensors, actions, delays, and limits.

### Observation

What the agent can sense. A camera image, a joint angle, a distance reading, or a grid position.

### Action

What the agent can do. Move left, rotate a joint, open a gripper, choose a velocity.

### Policy

The rule or model that maps observations to actions.

### Environment

The world the agent acts in. It can be simulated or real.

### Feedback

The signal that tells the agent whether it is doing well. It might be a reward, a human demonstration, a success label, or physical contact.

### Simulation

A safe, cheap place to test ideas before touching hardware.

### Sim-to-real gap

The difference between a clean simulated world and messy reality.

## What To Ignore In Month One

- buying robot hardware
- large robot foundation models
- advanced control theory
- training from scratch on big datasets
- collecting real robot data

## Week 1: Orientation

Goal: understand the core loop: observation -> policy -> action -> feedback.

Tasks:

- draw the loop for a vacuum robot, a robot arm, and a game agent
- learn the terms observation, action, state, policy, reward
- write three concept cards
- run or sketch one toy gridworld

Visible artifact:

- one page explaining the perception-action loop with a diagram

Check question:

- If the observation changes but the policy is the same, what might happen?

## Week 2: Core Concepts

Goal: understand how simple agents choose actions.

Tasks:

- compare hand-coded rules and learned policies
- implement a tiny pure Python gridworld first; use Gymnasium only if setup takes under 30 minutes
- record what the agent observes each step
- change the reward and notice behavior changes

Visible artifact:

- a small script or notebook where an agent moves in a toy environment

Check question:

- Why can a reward that looks reasonable still produce strange behavior?

Fallback:

- If environment installation blocks you, keep going with a paper gridworld or pure Python lists.

## Week 3: Practice

Goal: connect papers and projects.

Tasks:

- choose one beginner-friendly embodied AI or robotics paper using this rule: if you cannot identify the task setup in 20 minutes, pick a simpler source
- identify observation, action, policy, data, and evaluation
- reproduce a toy version of one idea
- write a method card

Visible artifact:

- a 2-hour toy reproduction or diagram

Check question:

- What is the smallest part of the paper you can reproduce without copying the whole system?

Resource cap:

- Use one paper, one lecture or blog post, and your own toy project. Stop searching after 90 minutes.

## Week 4: Integration

Goal: explain and extend.

Tasks:

- compare simulation and reality
- write a one-page "what I now understand" note
- improve the toy project
- list three next directions

Visible artifact:

- a short README for your toy project

Check question:

- What would break first if your agent moved from simulation to a real robot?

## First 7 Days

### Day 1

Draw three perception-action loops:

- robot vacuum
- robot arm picking a cup
- game agent moving in a grid

Write one sentence for observation, action, policy, and feedback in each example.

Done when:

- each loop labels observation, action, policy, and feedback
- each loop includes one failure case
- you can explain one loop without notes

### Day 2

Create three concept cards:

- observation
- action
- policy

Done when:

- each card has a plain meaning, concrete example, and check question

### Day 3

Make a tiny gridworld on paper. The agent can move up, down, left, right. Mark a goal and one obstacle.

Done when:

- you can name the observation, action space, and goal

### Day 4

Write pseudocode for a hand-coded policy:

```text
if goal is to the right, move right
if obstacle blocks the way, move up
otherwise move toward goal
```

Done when:

- the policy makes a decision for at least three different positions

### Day 5

Change the environment. Add a second obstacle. Notice where the hand-coded policy breaks.

Done when:

- you can write one sentence explaining why the policy failed

### Day 6

Read one short introduction to reinforcement learning or watch one lecture section. Only extract the terms agent, environment, reward, policy.

Stop rule:

- Stop after 45 minutes. Do not open a second resource today.

Done when:

- you can explain reward without using the word "score"

### Day 7

Write a learning log:

- what makes sense now
- what is still fuzzy
- what you want to build next week

Done when:

- the log names one concept to review tomorrow and one task to try next

## Today's First Move

Draw the perception-action loop for a robot arm picking up a mug. Label:

- observation
- action
- policy
- feedback
- one thing that could go wrong

Do not read a paper yet.
