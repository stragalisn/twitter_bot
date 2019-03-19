
import tweepy

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

def like_my_mentions():
    mentions = api.mentions_timeline()
    for i in range(len(mentions)):
        mentions[i].__dict__.keys()
        id_of_tweet = mentions[i].id
        api.create_favorite(id_of_tweet)

def post_for_my_channel():
    api.update_status(status = "")

def like_and_retweet_other_posts(limit, date):
    try:
        for tweet in tweepy.Cursor(api.search, q = "", count = 15, lang = "en", since = date).items(limit):
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
    except tweepy.TweepError as e:
        print(e)

def follow_my_followers():
    ids = api.followers_ids()
    for i in range(len(ids)):
        api.create_friendship(ids[i])

