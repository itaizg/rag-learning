---
description: Work a task in a loop until a goal check passes
argument-hint: <task>
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Task
model: sonnet
---

Work this task in a loop: $ARGUMENTS

1. Establish the goal check. Ask me what "done" means if it
   isn't obvious: tests green, benchmark under X, no lint errors.
   For this repo the default check is a notebook executing clean —
   `.claude/checks/notebooks.sh <path>` (see `.claude/checks/`).
2. Do the work toward the goal.
3. Run the goal check. Record the result.
4. Met: stop and show me the result with proof.
   Not met: use the check's output to decide the next change,
   then go back to step 2.
5. Cap at 5 cycles. Announce the cycle number each round.

The check is the truth, not your opinion. Never declare done
without running it. Never weaken the check to pass it.
