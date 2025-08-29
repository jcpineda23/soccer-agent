def build_planner_prompt(goal: str) -> str:
    return f"""
You are a soccer scouting agent. Your job is to break down user goals into structured plans.

Goal: "{goal}"

Return ONLY a JSON list of steps. Do not include any explanation or extra text.

Each step must include:
- action: one of ["fetch_players", "filter", "rank"]
- params: dictionary of parameters

Example:
[
  {{ "action": "fetch_players", "params": {{ "position": "MF", "league": "La Liga" }} }},
  {{ "action": "filter", "params": {{ "age": "<21" }} }},
  {{ "action": "rank", "params": {{ "metric": "xG_per_90" }} }}
]
"""