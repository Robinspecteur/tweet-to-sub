import twitter
import reddit
from formatting import format_tweets
from config import load_config

# Initalization
config = load_config()
twitter_api = twitter.twitter_api(config["twitter"])
reddit_api = reddit.reddit_api(config["reddit"])
most_recent_id = twitter.last_tweet_id(twitter_api, config["twitter"])


def handler(event, context):
    global most_recent_id

    # In case of test, only get the lat tweet and display it, but don't submit
    if "test" in event:
        most_recent_id -= 1

    # Get new tweets and update id of the most recent tweet
    new_tweets, most_recent_id = twitter.last_tweets(twitter_api,
                                                     config["twitter"],
                                                     since=most_recent_id)
    if new_tweets:
        # Format title and URL for reddit
        titles_urls = format_tweets(new_tweets, config["format"])

        # Submit them on reddit, reversed to submit most recent one last
        permalinks = ["None"] * len(new_tweets)
        if "test" not in event:
            permalinks = reddit.submit(reddit_api, config["reddit"],
                                       reversed(titles_urls))

        # Display new uploads
        print("{} new tweet(s):".format(len(new_tweets)))
        for i in range(len(new_tweets)):
            print("Title: " + titles_urls[i][0])
            print("URL: " + titles_urls[i][1])
            print("Permalink: " + permalinks[i])


if __name__ == "__main__":
    handler(["test"], [])
