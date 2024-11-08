import sys
import json
import argparse
import getpass
#import cryptography

print("In order to run this program you need an API Key and Access Token from twitter")
print("Do you have this info ready?")
start = input("Y/n")

sys.exit(1) if start.upper()!= "Y" else None


API_KEY=getpass.getpass("Insert API_KEY/Consumer Key: \n")
API_SECRET=getpass.getpass("Insert API_SECRET/Consumer Secret Key: \n")
ACCESS_TOKEN=getpass.getpass("Insert ACCESS_TOKEN: \n")
ACCESS_TOKEN_SECRET=getpass.getpass("Insert ACCESS_TOKEN_SECRET: \n")

bskylogin=input("Insert Bluesky Login: \n")
bskypw=getpass.getpass("Insert Bluesky Password: \n")


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
#Add command to run crosspost.py

#11.8.24 REFACTOR FOR SECURITY LATER WHEN I GET TIME
#Encrypting JSON file and passing it to the crossposting app