# core/ranking_engine.py
class RankingEngine:
    def __init__(self):
        self.excuse_log = []

    def log_excuse(self, excuse, outcome):
        self.excuse_log.append({'excuse': excuse, 'outcome': outcome})

    def rank_excuses(self):
        # Simple ranking based on success
        success_count = sum(1 for log in self.excuse_log if log['outcome'] == 'success')
        return success_count

# Example usage
if __name__ == "__main__":
    ranking = RankingEngine()
    ranking.log_excuse("I'm sorry, I can't make it.", "success")
    print("Success count:", ranking.rank_excuses())
