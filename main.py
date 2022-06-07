from logging.config import listen
import tweepy
from tweepy import StreamingClient, StreamRule
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
AK = os.getenv('API_KEY')
AKS = os.getenv('API_KEY_SECRET')
AT = os.getenv('ACCESS_TOKEN')
ATS = os.getenv('ACCESS_TOKEN_SECRET')
BT = os.getenv('BEARER_TOKEN')


class TweetPrinter(tweepy.StreamingClient):
    
    def on_tweet(self, tweet):
        print(f"{tweet.id} {tweet.created_at} ({tweet.author_id}): {tweet.text}")
        print("-" * 50)
    
       
try:
    printer = TweetPrinter(BT)
    rule_ids = []
    rules = printer.get_rules()

    if rules.data != None: 
        for rule in rules.data:
            print(f"Rule marked to delete: {rule.id}: {rule.value}")
            rule_ids.append(rule.id)

        if len(rule_ids) > 0:
            printer.delete_rules(rule_ids)
            printer = TweetPrinter(BT)
            print("Deleted all rules.")
        else:
            print("No rules to delete.")

    printer.add_rules(StreamRule(value="AIT"))
    printer.filter(expansions="author_id", tweet_fields="created_at")

except KeyboardInterrupt as e:
        print(" The stream has been disconnected.")

 
