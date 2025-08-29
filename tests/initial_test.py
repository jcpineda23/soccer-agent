from agent.planner_llama import LLaMAPlanner

planner = LLaMAPlanner()
goal = "Find U21 midfielders in La Liga with high xG per 90"
plan = planner.generate_plan(goal)

for step in plan:
    print(step)