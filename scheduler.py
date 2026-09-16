# core/scheduler.py
from datetime import datetime, timedelta

class Scheduler:
    def __init__(self):
        self.usage_log = []

    def log_usage(self, timestamp):
        self.usage_log.append(timestamp)

    def predict_next_usage(self):
        if not self.usage_log:
            return "No usage history available."
        last_usage = max(self.usage_log)
        next_usage = last_usage + timedelta(days=7)  # Predict next week
        return next_usage.strftime("%Y-%m-%d %H:%M:%S")

# Example usage
if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.log_usage(datetime.now())
    print("Next likely scenario:", scheduler.predict_next_usage())
