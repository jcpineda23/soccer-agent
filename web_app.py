import streamlit as st
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
        plan = self.planner.generate_plan(goal)
        results = []
        for step in plan:
            result = self.executor.run(step)
            self.memory.save(step, result)
            results.append(result)
        return self.formatter.format(goal, results)

# UI
st.set_page_config(page_title="ScoutLite", layout="centered")
st.title("⚽️ ScoutLite: Soccer Scouting Agent")

goal = st.text_input("Enter your scouting goal:", "Find U21 midfielders in La Liga with high xG per 90")

if st.button("Run Agent"):
    agent = ScoutLiteAgent(
        planner=LLaMAPlanner(),
        executor=Executor(),
        memory=Memory(),
        formatter=Formatter()
    )
    output = agent.handle_goal(goal)

    st.subheader("✅ Summary")
    st.write(output["summary"])

    st.subheader("📋 Top Players")
    for player in output["top_players"]:
        st.write(f"- {player['name']} | Age: {player['age']} | xG/90: {player.get('xG_per_90', 'N/A')}")

    st.subheader("💡 Next Suggestion")
    st.write(output["next"])