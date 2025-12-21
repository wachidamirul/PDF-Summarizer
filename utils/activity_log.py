import os
from datetime import datetime

from config.settings import LOG_PATH

os.makedirs("data/logs", exist_ok=True)

def log_activity(event: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a") as f:
        f.write(f"[{timestamp}] {event}\n")
