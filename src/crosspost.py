import sys
import tweepy
import atproto
from atproto import Client
from datetime import datetime
from atproto.exceptions import (
    LoginRequiredError,
    BadRequestError,
    ModelError,
    NetworkError,
    InvalidAtUriError,
)
    
API_KEY="" #Consumer Key
API_SECRET=""#Consumer Secret
ACCESS_TOKEN=""#Authentication Token
ACCESS_TOKEN_SECRET=""#Authentication Secret Token

bskylogin =""
bskypw =""   

if not all([API_KEY, API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET,bskylogin,bskypw]):
    print(f"1 or more data fields were empty. Run config.py")
    sys.exit(1)

if len(sys.argv) < 2:
    print("Python(ver) xpost.py <Your post here>")
    sys.exit(1)

tweet =" ".join(sys.argv[1:])

if len(tweet) > 280:
    print("length exceeds the maximum character length")
    sys.exit(1)


bskyclient= Client()

try:
    bskyclient.login(bskylogin, bskypw)
except LoginRequiredError as e:
    print("login failed {e}")

try:
    api = tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )

    response = api.create_tweet(text=tweet)
    print(f"successfully sent{response.data['id']}")
except tweepy.TweepyException as e:
    print(f"Error Check Settings and rerun script! {e}")

post = bskyclient.send_post(tweet)
print(post.uri)

print("successful bsky post")