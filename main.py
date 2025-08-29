from agent.planner_llama import LLaMAPlanner
from agent.executor import Executor
from agent.memory import Memory
from agent.formatter import Formatter

class ScoutLiteAgent:
    def __init__(self, planner, executor, memory, formatter):
        self.planner = planner
        self.executor = executor
        self.memory = memory
        self.formatter = formatter

    def handle_goal(self, goal: str):
        print(f"\n🔍 Received goal: {goal}")
        plan = self.planner.generate_plan(goal)
        print(f"\n🧭 Generated plan:")
        for step in plan:
            print(f" - {step}")

        results = []
        for step in plan:
            result = self.executor.run(step)
            self.memory.save(step, result)
            results.append(result)

        response = self.formatter.format(goal, results)
        return response

if __name__ == "__main__":
    # Example goal — you can replace this with CLI input or a UI later
    goal = input() ##"Find U21 midfielders in La Liga with high xG per 90"

    agent = ScoutLiteAgent(
        planner=LLaMAPlanner(),
        executor=Executor(),
        memory=Memory(),
        formatter=Formatter()
    )

    output = agent.handle_goal(goal)

    print("\n✅ Summary:")
    print(output["summary"])

    print("\n📋 Top Players:")
    for player in output["top_players"]:
        print(f" - {player}")

    print("\n💡 Next Suggestion:")
    print(output["next"])