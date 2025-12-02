import json
import time
from plyer import notification
from datetime import datetime

def load_config():
    """Reads config.json and return the settings."""
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    except Exception as e:
        print("Error reading config file:", e)
        return {
            "title": "Notifier",
            "message": "Default notification"
            "interval": 60
        }

def send_notification(title, message):
    """Displays a desktop notification."""
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

def log_event(title, message):
    """Logs each notification."""
    with open("notifier.log", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {title} - {message}\n")

def main():
    print("Desktop Notifier started... press CTRL+C to stop.")
    cfg =  load_config()

    title = cfg.get("title")
    message = cfg.get("message")
    interval = int(cfg.get("interval"))

    while True:
        send_notification(title, message)
        log_event(title, message)
        time.sleep(interval * 60)

if __name__ == "__main__":
    main()