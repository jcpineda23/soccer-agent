class ScoutLiteAgent:
    def __init__(self, planner, executor, memory, formatter):
        self.planner = planner
        self.executor = executor
        self.memory = memory
        self.formatter = formatter

    def handle_goal(self, goal: str):
        plan = self.planner.generate_plan(goal)
        results = []
        for step in plan:
            result = self.executor.run(step)
            self.memory.save(step, result)
            results.append(result)
        return self.formatter.format(goal, results)