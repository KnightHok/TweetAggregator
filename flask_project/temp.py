import tempfile
import requests
from datetime import datetime, timedelta
import time
import json
from apscheduler.schedulers.background import BackgroundScheduler

def download_temp_media(dir, url):
    response = requests.get(url, stream=True)
    filename = url.split("/")[-1]
    if response.ok:
        f = open(f'{dir}\\{filename}', 'wb')
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)
        return f 

def within_15(dm):
    time_stamp = int(dm._json["created_timestamp"])
    last_15 = datetime.now() - timedelta(minutes=15)
    if datetime.timestamp(time_stamp) > last_15:
        return True
    return False

def task():
    print("eating a burger with no honey mustard")

if __name__ == "__main__" :
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=task, trigger="interval", seconds=5)
    scheduler.start()
    while True:
        time.sleep(1)