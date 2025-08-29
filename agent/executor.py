import json
from pathlib import Path

class Executor:
    def __init__(self, data_path="data/players.json"):
        self.players = self._load_data(data_path)

    def _load_data(self, path):
        with open(Path(path), "r") as f:
            return json.load(f)

    def run(self, step: dict):
        action = step["action"]
        params = step["params"]

        if action == "fetch_players":
            return self._fetch_players(params)
        elif action == "filter":
            return self._filter_players(params)
        elif action == "rank":
            return self._rank_players(params)
        else:
            raise ValueError(f"Unknown action: {action}")

    def _fetch_players(self, params):
        position = params.get("position", None)
        league = params.get("league", None)
        age = params.get("age", None)

        results = self.players

        if position and position != "ANY":
            results = [p for p in results if p["position"] == position]

        if league:
            results = [p for p in results if p["league"] == league]

        if age and age.upper() == "U21":
            results = [p for p in results if p["age"] < 21]

        return results

    def _filter_players(self, params):
        metric = params.get("metric")
        threshold = params.get("threshold")

        if not metric or not threshold:
            return self.players

        # Normalize metric name
        metric = metric.replace(" ", "_")

        # Parse threshold
        if threshold.startswith(">"):
            value = float(threshold[1:])
            return [p for p in self.players if p.get(metric, 0) > value]
        elif threshold.startswith("<"):
            value = float(threshold[1:])
            return [p for p in self.players if p.get(metric, 0) < value]
        else:
            return self.players

    def _rank_players(self, params):
        metric = params.get("metric", "goals").replace(" ", "_")
        return sorted(self.players, key=lambda p: p.get(metric, 0), reverse=True)