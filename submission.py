import collections, sys, os
from logic import *
from planning import *

############################################################
# Problem: Planning 

# Blocks world modification
def blocksWorldModPlan():
    # BEGIN_YOUR_CODE (make modifications to the initial and goal states)
    initial_state = 'On(C, D) & Clear(C) & OnTable(D) & On(A, B) & Clear(A) & OnTable(B)'
    goal_state = 'On(D, C) & On(C, B) & On(B, A) & OnTable(A) & Clear(D)'
    # END_YOUR_CODE

    planning_problem = \
    PlanningProblem(initial=initial_state,
                    goals=goal_state,
                    actions=[Action('ToTable(x, y)',
                                    precond='On(x, y) & Clear(x)',
                                    effect='~On(x, y) & Clear(y) & OnTable(x)'),
                             Action('FromTable(y, x)',
                                    precond='OnTable(y) & Clear(y) & Clear(x)',
                                    effect='~OnTable(y) & ~Clear(x) & On(y, x)'),
                             Action('Move(x, y, z)',
                                    precond='On(x, y) & Clear(x) & Clear(z)',
                                    effect='~On(x, y) & Clear(y) & On(x, z) & ~Clear(z)')])
    
    return linearize(GraphPlan(planning_problem).execute())

# Execute Blocks World Plan
a = blocksWorldModPlan()
print("Blocks World Plan Solution:", a)
