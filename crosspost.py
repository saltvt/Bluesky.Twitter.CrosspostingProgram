import sys
import tweepy
import atproto
import json
import cryptography.fernet
import base64
import os 
import hashlib
from atproto import Client
from datetime import datetime
from atproto.exceptions import (
    LoginRequiredError,
    BadRequestError,
    ModelError,
    NetworkError,
    InvalidAtUriError,
)


def load_decrypted_data():
    key_file = "encryptionKey.key"
    data_file = "encryptedData.dat"
    
    with open(key_file, "rb") as kf:
        key = kf.read()
        
    with open(data_file, "rb") as df:
        encrypted_data = df.read()
        
    f = cryptography.fernet.Fernet(key)
    decrypted_data = json.loads(f.decrypt(encrypted_data).decode())
    
    return decrypted_data

Key = load_decrypted_data() #loads the encrypted json file and all the data

API_KEY= Key["API_KEY"]
API_SECRET= Key["API_Secret"]
ACCESS_TOKEN=Key["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET=Key["ACCESS_TOKEN_SECRET"]

bskylogin =Key["bskylogin"]
bskypw =Key["bskypw"]   

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



# 11.15.24 Looking to create a UI for image upload, reposting, pulling tweets etc.
# Work in progress. Basic functionality for advanced users done
#version 0.0.2