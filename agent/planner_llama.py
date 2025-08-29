import json
from models.llama3 import call_llama
from models.prompts import build_planner_prompt

class LLaMAPlanner:
    def generate_plan(self, goal: str) -> list:
        """
        Uses LLaMA 3 to generate a structured plan from a user goal.
        Returns a list of steps like:
        [
            {"action": "fetch_players", "params": {"position": "MF"}},
            {"action": "filter", "params": {"age": "<21"}},
            {"action": "rank", "params": {"metric": "assists"}}
        ]
        """
        prompt = build_planner_prompt(goal)
        raw_output = call_llama(prompt)
        print("Raw LLaMA Output:", raw_output)  # Debugging line
        print("-------")
        try:
            plan = json.loads(raw_output)
            self._validate_plan(plan)
            return plan
        except json.JSONDecodeError:
            raise ValueError("Planner output is not valid JSON.")
        except Exception as e:
            raise ValueError(f"Planner failed: {e}")

    def _validate_plan(self, plan: list):
        """
        Basic validation to ensure each step has 'action' and 'params'.
        """
        for step in plan:
            if not isinstance(step, dict):
                raise ValueError("Each step must be a dictionary.")
            if "action" not in step or "params" not in step:
                raise ValueError("Each step must include 'action' and 'params'.")