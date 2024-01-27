from datetime import datetime, timezone
from apscheduler.schedulers.background import BackgroundScheduler
from .schedule import scheduled_crawl

def start():
    # automated and scheduled crawling
    scheduler = BackgroundScheduler(timezone='UTC')
    # setting default time interval = 5y mins
    scheduler.add_job(scheduled_crawl, 'interval', minutes=2)
    scheduler.start()
