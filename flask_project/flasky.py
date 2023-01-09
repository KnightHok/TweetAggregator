import os
from new_main import createTwitterApiConnection, print_dms
from flask import Flask, json
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv

app = Flask(__name__)
scheduler = BackgroundScheduler()

load_dotenv("../.env")

api = createTwitterApiConnection(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
) 

is_On = False

@app.route("/")
def hello_world():
    return "<h1>Hello niggas</h1>"

@app.route("/start-watching")
def start_watching_dms():
    return "<h1>Started watching dms</h1>"

@app.route("/bot_status")
def status_of_bot():
    global is_On
    return f"{is_On}"

@app.route("/start_bot")
def start_bot():
    twitter_id = int(os.getenv("TWITTER_ID"))

    BEARER_TOKEN = os.getenv("BEARER_TOKEN")
    CONSUMER_KEY = os.getenv("API_KEY")
    CONSUMER_SECRET = os.getenv("API_SECRET")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

    global is_On, api
    if is_On == False:
        is_On = True
        scheduler.add_job(func=lambda: print_dms(api=api, twitter_id=twitter_id), trigger="interval", minutes=3)
        scheduler.start()
        return "Bot has started"
    else:
        return "Bot is already on"

@app.route("/stop_bot")
def stop_bot():
    global is_On
    if is_On:
        is_On = False
        scheduler.shutdown()
        return "Bot has Stopped"
    else:
        return "Bot is not running"

if __name__ == "__main__":
    
    # twitter_id = int(os.getenv("TWITTER_ID"))

    # BEARER_TOKEN = os.getenv("BEARER_TOKEN")
    # CONSUMER_KEY = os.getenv("API_KEY")
    # CONSUMER_SECRET = os.getenv("API_SECRET")
    # ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    # # ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

    # api = createTwitterApiConnection(
    #     consumer_key=CONSUMER_KEY,
    #     consumer_secret=CONSUMER_SECRET,
    #     access_token=ACCESS_TOKEN,
    #     access_token_secret=ACCESS_TOKEN_SECRET
    # ) 

    app.run()