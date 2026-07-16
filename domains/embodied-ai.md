# Domain Pack: Embodied AI

This domain pack gives the learning system a strong default path for embodied AI beginners.

## Beginner Assumptions

Default learner:

- knows basic Python
- has seen basic machine learning
- has not studied robotics deeply
- does not own robot hardware
- can spend 45-90 minutes a day

## Learner Tracks

### Track A: No Python Yet

Goal for month one:

- understand the perception-action loop through drawings and paper simulations
- learn enough Python control flow to write a tiny gridworld later

First tasks:

- draw three agent loops
- make paper concept cards
- write pseudocode before code

Avoid:

- installing simulators
- reading papers before core vocabulary
- copying large notebooks

### Track B: Python, No Machine Learning

Goal for month one:

- build a tiny gridworld with hand-coded policies
- understand observation, action, policy, reward, and environment

First tasks:

- implement a pure Python gridworld with lists and dictionaries
- compare two hand-coded policies
- add a simple reward

Avoid:

- deep RL libraries
- GPU setup
- robotics hardware

### Track C: Python And Basic Machine Learning, No Robotics

Goal for month one:

- connect ML concepts to embodied tasks
- build a small simulated agent
- read one paper by extracting task setup and method cards

First tasks:

- draw observation-action-policy-feedback loops
- implement or run a simple environment
- compare rule-based behavior and a learned policy at a high level

Avoid:

- foundation robotics model training
- sim-to-real engineering
- leaderboards

## First Month Outcome

The learner can:

- explain the perception-action loop
- distinguish observation, state, action, policy, reward, and environment
- build or sketch a tiny gridworld agent
- read one paper by identifying task setup and method components
- explain what would fail when moving from simulation to real-world robots

## Concept Order

1. Agent, environment, observation, action
2. Policy and feedback
3. Reward, demonstrations, and supervision
4. Simulation and real-world constraints
5. Hand-coded rules versus learned policies
6. Imitation learning at a high level
7. Reinforcement learning at a high level
8. Data collection and evaluation
9. Sim-to-real gap
10. Large robotics models and grounding

## First Projects

### 2-Hour Project

Paper gridworld plus pseudocode policy.

The learner draws a grid, goal, obstacle, and agent. They write a policy and test it by hand.

### 1-Day Project

Simple Python gridworld.

The learner implements:

- position
- observation
- actions
- reward
- terminal state
- one rule-based policy

### 1-Week Project

Toy embodied agent report.

The learner builds a tiny environment, compares two policies, writes a short report, and connects the project to one paper or lecture.

## Fallback Rules

- If installation fails for more than 30 minutes, switch to paper gridworld.
- If Python code blocks progress, write pseudocode and one worked example.
- If a paper feels unreadable, extract only observation, action, policy, data, and evaluation.
- If the learner cannot answer a check question, use Socratic Tutor before adding new material.

## First Papers Or Resources

Do not start with a long reading list. Pick one resource only after the learner has the core loop.

Good first reading goals:

- identify observation/action/reward in a paper
- draw the task setup
- extract one reproducible idea

Avoid first-week goals:

- reading a survey end to end
- training large models
- chasing benchmark leaderboards
- installing a complex simulator before understanding the loop

## Good Check Questions

- What does the agent observe?
- What action choices does it have?
- What policy chooses the action?
- What feedback tells it whether it is doing well?
- What would break if the observation were noisy?
- Is the system using simulation, real data, or both?
