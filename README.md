# Project Picker

The goal of this project is to allow the automated selection of a project based on a list of available tech stacks. 
The end result should give the user an ability to add constraints and modifiers to a given tech stack result
This project will output this in a text format

## MVP

- [x] Selects an Objective
- [x] Can optionally select additional constraints/modifiers
- [x] Outputs the result

## Bonus Points

- [x] Intelligent recommendation system
- [ ] Interactive view/UI
- [ ] Save output of results

## Alloted Time

|Phase|Allowed Time|
|---|:---:|
|Planning|00:20:00|
|Build|04:00:00|

---
## Approach

### Design

![Alt text](/docs/whiteboard.jpg?raw=true "whiteboard planning")

*Whiteboard showing design planning*

In tackling this challenge, I initially set my sights on a modest intuitive
workflow for picking a base challenge at random, and giving the user the 
ability to add additional modifiers if the challenge is too easy.

In a basic sense, this meant having a perceived difficulty attached to each
task, and some way of intelligently modifying the difficulty of the task
based on additional modifiers. Whilst a challenge can be difficult or easy
in a vacuum - additional modifiers like tech stacks and platforms are specific
to the individual. Due to this I wanted to use someone's own perceived 
familiarity with a stack in order to derive a difficulty modifier to use.

As a stretch I wanted to implement a better combinatorics-based approach to
picking tasks optimally.

### Implementation

![Alt text](/docs/output.png?raw=true "program output")

*Showing the program's console output*

Within the implementation of the task, I took the following basic steps:

- Create a demonstrative dataset
- Create a basic CLI to issue user commands into the domain logic
- Create a test harness using the IDE to issue a specific set of CLI commands
- Form the generator framework
  - Parsing of raw data into a usable format
  - Interchangable pattern for challenge generation strategies
- Actual generator logic
  - Start with naive approach, where challenges are constructure intuitively (as per the whiteboard)
  - If time allows, look at smarter ways of optimising the problem and apply a separate generator or two

In the end, I formed two distinct generation strategies:

#### Intuitive

This is basically an intuitive approach I thought would be a good easy
implementation to include that isn't a direct optimisation formula. There
are weightings and logic specifically designed to include some randomness
and some specific modifier selection.

This more commonly tries to build a challenge from stacks and platform
(as these are the driving force of SHC), but will continue to add these if
it's not hard enough. There's a smaller chance to receive a higher-weight
non stack/platform modifier (like coding one-handed), but this allows for
these to sometimes show up.

Pseudocode:

```
Randomly pick a challenge if one is not given

If it's less than the target difficulty
    If <variable: 80%> chance to pick either a stack or a platform
        pick a random modifier
            add to the challenge difficulty
            If it's still below target difficulty
                add the opposing modifier
                If it's still below target difficulty
                    add an exotic modifier
    Else
        add an exotic modifier

If there's still remaining space, option to fill it with
the best matching random modifier.      

Submit challenge with 0-n modifiers
```

#### Knapsack

This is a pseudo knapsack generation strategy, a known dynamic programming problem
where you try to optimise putting objects in a bag where each object has an
associated value and weight.

We don't have an associated value with challenges, only a weight (difficulty), so
this problem more closely resembles the subset-sum problem (give me a set from a
larger set where the `sum = x`).

This strategy uses subset sums to optimally select `n` modifiers where `n` is
configurable. If there is no suitable set that satisfies `n`, `n` is diminished
until the closest set is found.

For example, if you ask for 3 modifiers, but you only have 5 remaining points of
capacity to fill (difficulty delta). If there are no combinations of 3 modifiers
from the pool which add up to 5 or less, this process is repeated to find 2 modifiers,
and so on.

---
## Evaluation

Overall I think this challenge went OK. I lost a lot of time initially to boilerplate
and data-wrangling (around half of the alloted time) which sucks. On the other hand,
the generated ideas turned it pretty nice, and the user experience is good.

The user can generate one or more easy, medium or hard challenges with modifiers
tailored to their experience as augmenting an existing challenge with modifiers
if the challenge is picked ahead of time.

If I had more time I'd like to hook this up to Trello to pull the tasks automatically
(which I started doing in the first instance but ditched due to time). Implementing
a proper optimisation algorithm would also be a fun addition.

- Good
  - Variable strategies for generation is nice
  - Ability to pre-pick a challenge and have it be modified
  - Difficulty sensivie to the participant
  - Code relatively clean
  - UI is straight forward and flexible
  - Interesting options surfaced in config

- Not so good
  - Domain logic needs comments in places
  - Some semi-redundant code due to time pressure
  - No tests per se
  - Doesn't automatically output to a file (no time) but can be piped to do so
  - Some generator logic not in main config
  - Didn't hit bonnus points for an interactive view/UI

### Timings

|Objective|Split|
|---|---|
|Planning|00:20:00|
|API Implentation|01:40:00|

### Lessons Learned

- awdawdawd
- awd awdawd

---
## Acknowledgements 

|Type|Author|Description|Link|
|---|---|---|:---:|
|Documentation|Various (wikipedia)|Subset Sum Problem|[Link](https://en.wikipedia.org/wiki/Subset_sum_problem)|
|Documentation|Various (wikipedia)|Knapsack Problem|[Link](https://en.wikipedia.org/wiki/Knapsack_problem)|