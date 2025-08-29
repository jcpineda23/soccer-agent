class Formatter:
    def format(self, goal, results):
        summary = f"Completed goal: {goal}"
        players = results[-1]  # Final ranked list
        return {
            "summary": summary,
            "top_players": players,
            "next": "Want to compare these players to last season’s top performers?"
        }