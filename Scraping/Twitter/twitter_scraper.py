import tweepy
import urllib.request
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys


auth = tweepy.OAuthHandler(consumer_key='JKUtoGY0YWfoSe8KIVng8xfdP', consumer_secret='7j2AdZyj8TlR8c87YyVggLpdJZ9EF1luIcot0CWnQXyW5EDZHx')
auth.set_access_token('942388760121171968-FJoYMWB7o3qWSxcSI9h8aIFxMiNWgKw', 'Fxh2fRsXZbvtJtwdo3h4XKccdp0my0bniXls6kbeEND1A')
api = tweepy.API(auth)



def get_user_handle(tweet_id):
    user_handle = api.get_status(tweet_id).author.screen_name
    return user_handle

def get_user_data(user_handle):
    user_friends_screen_name=[]
    user = api.get_user(user_handle)
    user_name = user.name
    user_screen_name = user.screen_name
    user_description = user.description
    user_location = user.location

    # for follower in user.followers():
    #     print(follower.name)



    # print(user.followers_count)
    # for friend in user.friends():
    #     user_friends_screen_name.append(friend.screen_name)

    #get user tweets:
    hashtags = []
    mentions = []
    user_tweets=[]
    tweet_count = 0
    end_date = datetime.utcnow() - timedelta(days=1)
    for status in Cursor(api.user_timeline, id=user_handle).items():
        tweet_count += 1
        if hasattr(status, "entities"):
            entities = status.entities
            if "hashtags" in entities:
                for ent in entities["hashtags"]:
                    if ent is not None:
                        if "text" in ent:
                            hashtag = ent["text"]
                            if hashtag is not None:
                                hashtags.append(hashtag)
            if "user_mentions" in entities:
                for ent in entities["user_mentions"]:
                    if ent is not None:
                        if "screen_name" in ent:
                            name = ent["screen_name"]
                            if name is not None:
                                mentions.append(name)

        user_tweets.append(status.text)

        if status.created_at < end_date:
            break
    print(user_tweets)




    return user_name ,user_screen_name, user_description, user_location, user_friends_screen_name, user_tweets

def scrape_user(tweet_id):
    user_handle = get_user_handle(tweet_id)
    user_name ,user_screen_name, user_description, user_location, user_friends_screen_name, user_tweets = get_user_data(user_handle)
    return user_name ,user_screen_name, user_description, user_location, user_friends_screen_name, user_tweets


# scrape_user('552767187694661632')