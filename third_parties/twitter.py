import os

from dotenv import load_dotenv
import tweepy
import requests

load_dotenv()

twitter_client = tweepy.Client(
    bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_SECRET_KEY"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET"),
)


def scrape_user_tweets(username, num_tweets=5, mock=True):
    """
    Scrape tweets from a user's Twitter profile.
    """
    tweet_list = []

    if mock:
        EDEN_TWITTER_GIST = "https://gist.githubusercontent.com/NhanNguyen001/bbedf88686d750df0fb6fd6f475ecd37/raw/f495e028dc9ca9afc9832c2470003ceff62bbc3f/eden-marco-tweets.json"
        tweets = requests.get(EDEN_TWITTER_GIST, timeout=5).json()
    else:
        user_id = twitter_client.get_user(username=username).data.id
        tweets = twitter_client.get_users_tweets(
            id=user_id,
            max_results=num_tweets,
            exclude=["retweets", "replies"],
        )
    for tweet in tweets:
        tweet_dict = {}
        tweet_dict["text"] = tweet["text"]
        tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet['id']}"
        tweet_list.append(tweet_dict)

    return tweet_list


if __name__ == "__main__":
    tweets = scrape_user_tweets(username="EdenEmarco177")
    print(tweets)
