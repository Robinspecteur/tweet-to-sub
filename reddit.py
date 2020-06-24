import praw


def reddit_api(config):
    """Create a connexion to Twitter API"""
    reddit = praw.Reddit(client_id=config['client_id'],
                         client_secret=config['client_secret'],
                         user_agent=config['user_agent'],
                         username=config['username'],
                         password=config['password'])
    reddit.validate_on_submit = True
    return reddit


def submit(api, config, titles_urls):
    """
    Submit all the titles_urls in the subreddit in order of titles_urls array
    """
    permalinks = []
    for title, url in titles_urls:
        sub = api.subreddit(config["subreddit"]).submit(title=title,
                                                        url=url,
                                                        send_replies=False)
        permalinks.append(sub.permalink)
    return permalinks
