import sys
import json
import argparse


print("In order to run this program you need an API Key and Access Token from twitter")
print("Do you have this info ready?")
start = input("Y/n")

sys.exit(1) if start.upper()!= "Y" else None


API_KEY=input("Insert API_KEY")
API_SECRET=input("Insert API_SECRET")
ACCESS_TOKEN=input("Insert ACCESS_TOKEN")
ACCESS_TOKEN_SECRET=input("Insert ACCESS_TOKEN_SECRET")

bskylogin=input("Insert Bluesky Login")
bskypw=input("Insert Bluesky Password")


if not all([API_KEY,API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, bskylogin, bskypw]):
    print("All Fields not filled. Exiting. Rerun Program")
    sys.exit(1)

data = { 
    "API_KEY":API_KEY,
    "API_Secret":API_SECRET,
    "ACCESS_TOKEN":ACCESS_TOKEN,
    "ACCESS_TOKEN_SECRET":ACCESS_TOKEN_SECRET,
    "bskylogin":bskylogin,
    "bskypw":bskypw
}

with open ("data.json", "w") as f:
    json.dump(data, f)

print("Data stored opening program")
