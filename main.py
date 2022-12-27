import os
from dotenv import load_dotenv
import tweepy

load_dotenv("./.env")

# auth = tweepy.OAuth2BearerHandler(os.getenv("BEARER_TOKEN"))
# api = tweepy.API(auth)

twitter_id = int(os.getenv("TWITTER_ID"))

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
CONSUMER_KEY = os.getenv("API_KEY")
CONSUMER_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

def newClient():
    client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )
    return client


def print_repost_dms_from_user(client):
    dms = client.get_direct_message_events(expansions=['sender_id', 'referenced_tweets.id'])

    # see if user has sent any thing

    # if there are referenced tweets
    data = dms[0]
    for message in data:
        if message.sender_id == twitter_id and message.referenced_tweets is not None:
            print(message)
            id = message.referenced_tweets[0].id
            tweet = client.get_tweet(id=id, media_fields=['url'], expansions=['attachments.media_keys'], tweet_fields=['entities', 'attachments'])
            # if there are media files get those
            if tweet.includes:
                tweet_media_list = tweet.includes["media"]
                for media in tweet_media_list:
                    print(media.url)
        
    # print(type(twitter_id))

if __name__ == "__main__":
    client = newClient()
    print_repost_dms_from_user(client)

