import html


def format_url(tweet):
    """Generate the URL for a tweet"""
    base_url = "https://twitter.com/"
    username = tweet.user.screen_name
    tweet_id = str(tweet.id)
    return base_url + username + "/status/" + tweet_id


def format_title(tweet, config):
    """Format a single tweet"""
    if hasattr(tweet, 'retweeted_status'):
        # Format for a retweet
        rt_author = tweet.retweeted_status.user.screen_name
        prefix = config["mention_rt"] + ' @' + rt_author + ': "'
        parsed_text = html.unescape(tweet.retweeted_status.full_text)
        suffix = '"'
    else:
        # Format for an original tweet
        prefix = config["mention_user"] + ': "'
        parsed_text = html.unescape(tweet.full_text)
        suffix = '"'
    formatted = prefix + parsed_text + suffix

    # Shorten text if too long
    if len(formatted) > 300:
        suffix = '..."'
        formatted = formatted[:300 - len(suffix)] + suffix
    return formatted


def format_tweets(tweets, config):
    return [(format_title(t, config), format_url(t)) for t in tweets]
