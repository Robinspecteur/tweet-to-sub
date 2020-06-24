import tweepy


def twitter_api(keys):
    """Create a connection to Twitter API"""
    auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])
    twitter = tweepy.API(auth, wait_on_rate_limit=True)
    return twitter


def last_tweet_id(api, config):
    """Get ID from the most recent tweet"""
    tweet = api.user_timeline(config["user_id"])[0]
    return tweet.id


def last_tweets(api, settings, since):
    tweets = api.user_timeline(settings["user_id"],
                               tweet_mode="extended",
                               since_id=since)
    if not tweets:
        return [], since
    return tweets, tweets[0].id
