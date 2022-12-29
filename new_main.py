import os
import uuid
import tempfile
import tweepy
from dotenv import load_dotenv
from temp import download_temp_media

def upload_repost_dm(api: tweepy.API):
    dms = api.get_direct_messages()

    # begin dm checking process
    for dm in dms:
        sender_id = int(dm._json["message_create"]["sender_id"])
        message_data = dm._json["message_create"]["message_data"]

        # if watched twitter user send a message with urls
        if sender_id == twitter_id and message_data["entities"]["urls"]:
            # get twitter id
            url_types = message_data["entities"]["urls"][0]
            tweet_id = url_types["expanded_url"].split("/")[-1]

            # get tweet
            tweet = api.get_status(id=tweet_id)
            # if there are media files get them
            if "media" in tweet._json["entities"].keys():

                # create temp directory
                with tempfile.TemporaryDirectory() as temp_dir:
                    # create array of media files
                    media_files = []
                    tweet_media_list = tweet._json["extended_entities"]["media"]

                    for media in tweet_media_list:
                        url = media["media_url_https"]
                        f = download_temp_media(temp_dir, url)
                        media_files.append(f)
                    # see media files
                    # print(media_files)

                    # create list for tweet media ids
                    tweet_media_ids = []
                    for file in media_files:
                        # make random file name
                        # filename = str(uuid.uuid4())
                        response = api.media_upload(filename=file.name)
                        tweet_media_ids.append(response.media_id)
                        file.close()
                    # print(tweet_media_ids)
                    status = api.update_status(status="", media_ids=tweet_media_ids)
                    print(status)




def print_dms(api: tweepy.API):
    dms = api.get_direct_messages()

    # begin dm checking process
    for dm in dms:
        sender_id = int(dm._json["message_create"]["sender_id"])
        message_data = dm._json["message_create"]["message_data"]

        # if watched twitter user send a message with urls
        if sender_id == twitter_id and message_data["entities"]["urls"]:
            # get twitter id
            url_types = message_data["entities"]["urls"][0]
            tweet_id = url_types["expanded_url"].split("/")[-1]

            # get tweet
            tweet = api.get_status(id=tweet_id)
            # if there are media files get them
            if "media" in tweet._json["entities"].keys():
                    tweet_media_list = tweet._json["extended_entities"]["media"]
                    media_urls = []
                    for media in tweet_media_list:
                        url = media["media_url_https"]
                        media_urls.append(url)
                    print(media_urls)
                    



if __name__ == "__main__":
    load_dotenv("./.env")
    twitter_id = int(os.getenv("TWITTER_ID"))

    BEARER_TOKEN = os.getenv("BEARER_TOKEN")
    CONSUMER_KEY = os.getenv("API_KEY")
    CONSUMER_SECRET = os.getenv("API_SECRET")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuth1UserHandler(
        consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET
    )

    api = tweepy.API(auth)
    upload_repost_dm(api=api)
        