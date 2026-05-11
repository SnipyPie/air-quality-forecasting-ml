from apscheduler.schedulers.blocking import BlockingScheduler
from app.ingestion.logger import log_pollution

scheduler = BlockingScheduler()

scheduler.add_job(log_pollution, 'interval', minutes=15)

try:
    print("Scheduler started...")
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    print("Scheduler stopped cleanly.")