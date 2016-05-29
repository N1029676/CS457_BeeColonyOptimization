# CS457_BeeColonyOptimization

This project is a group assignment for CS457 meant to simulate a bee colony algorithm to solve multi-objective optimization problem. We have decided to attempt to find the most optimal course schedule for a prospective computer science student given weights for what they deem most desireable.

## Group members
- Drew Hall

- Jon Hammond

- Peyton Radford

- Tim Tasse

- Shane Thompson

## Project design

- `Professor.py`: Create professors to be used by other classes

- `Class.py`: Create the classes, sessions, and lists pre-reqs and their associated professor

- `Schedule.py`: Holds the list of sessions (derived from classes) and checks for validity and fitness

- `EliteBee.py`: Creates the initial list of classes a student may take, not sessions!

- `ScoutBee.py`: Starts creating schedules of sessions, based on lists produced by elite bees

- `BeeColony.py`: Kicks off all of the processes

This project will be multi-threaded to ensure the highest efficiency since this problem will quickly escalate beyond a reasonable time during runtime.
