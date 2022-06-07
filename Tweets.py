import tweepy
from tweepy import StreamingClient, StreamRule

class Tweets(tweepy.StreamingClient):
    
    def on_tweet(self, tweet):
        print(f"{tweet.id} {tweet.created_at} ({tweet.author_id}): {tweet.text}")
        print("-" * 50)
