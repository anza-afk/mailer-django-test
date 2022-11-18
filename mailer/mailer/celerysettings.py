from datetime import timedelta

BROKER_URL = "redis://localhost:6379/0"
CELERYBEAT_SCHEDULE = {
    "runs-every-60-seconds": {
        "task": "send_db_emails",
        "schedule": timedelta(seconds=60)
    },
}