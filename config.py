from os import environ as env
from dotenv import load_dotenv


def load_config():
    load_dotenv()  # Overwite environment variables if defined in .env
    config = dict()

    twitter = config["twitter"] = dict()
    twitter["consumer_key"] = env["TWITTER_CONSUMER_KEY"]
    twitter["consumer_secret"] = env["TWITTER_CONSUMER_SECRET"]
    twitter["access_token"] = env["TWITTER_ACCESS_TOKEN"]
    twitter["access_token_secret"] = env["TWITTER_ACCESS_TOKEN_SECRET"]
    twitter["user_id"] = env["TWITTER_USER"]

    format = config["format"] = dict()
    format["mention_user"] = env["MENTION_USER"]
    format["mention_rt"] = env["MENTION_RT"]

    reddit = config["reddit"] = dict()
    reddit["client_id"] = env["REDDIT_CLIENT_ID"]
    reddit["client_secret"] = env["REDDIT_CLIENT_SECRET"]
    reddit["user_agent"] = env["REDDIT_USER_AGENT"]
    reddit["username"] = env["REDDIT_USERNAME"]
    reddit["password"] = env["REDDIT_PASSWORD"]
    reddit["subreddit"] = env["REDDIT_SUBREDDIT"]

    return config
