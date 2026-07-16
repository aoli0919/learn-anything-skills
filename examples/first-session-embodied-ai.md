# Example: First Session Transcript

This is a sample response from the skill system.

## Learner

```text
I want to learn embodied AI. I know Python and a bit of ML, but robotics feels huge.
```

## Agent

You do not need to start with a robot or ten papers.

Start with one loop:

```text
the agent observes something -> chooses an action -> the world changes -> the agent gets feedback
```

For a robot arm picking up a cup:

- observation: camera image, gripper position, cup position
- action: move left, move down, close gripper
- policy: the rule or model choosing those actions
- feedback: did the cup move, did it slip, did the task succeed

Your first task is to draw this loop, not code it.

## Check Question

If the camera cannot see the cup handle, what part of the loop becomes unreliable?

## Expected Beginner Answer

The observation is incomplete, so the policy may choose a bad action.

## Follow-Up

Good. Now make it slightly more real:

What if the robot closes the gripper, but the cup slips? What feedback could tell the robot that something went wrong?

