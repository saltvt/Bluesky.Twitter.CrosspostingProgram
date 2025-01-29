import sys
import json
import argparse
import getpass
import cryptography.fernet
import base64
import os
import hashlib





def generateKey ():
    key = cryptography.fernet.Fernet.generate_key()
    return key

def encrypt_data(data, key):
    f = cryptography.fernet.Fernet(key)
    json_string = json.dumps(data)
    encrypted_data = f.encrypt(json_string.encode())
    print ("data encrypted")
    return encrypted_data

def hash_password (password):
    return hashlib.sha256(password.encode()).hexdigest()

def store_encrypted_data(data):
    keyFile = "encryptionKey.key"
    if not os.path.exists(keyFile):
        key = generateKey()
        with open (keyFile, "wb") as kf:
            kf.write(key)
    else: 
        with open(keyFile, "rb") as kf:
            key = kf.read()
            
    encryptedData = encrypt_data(data, key)
    with open("encryptedData.dat", "wb") as ef:
        ef.write(encryptedData)
    
    print("Login information successfully collected. Open crosspost.py")

if __name__ == "__main__":

    print("In order to run this program you need an API Key and Access Token from twitter")
    print("Do you have this info ready?")
    start = input("Y/n? \n")

    sys.exit(1) if start.upper()!= "Y" else None


    API_KEY=getpass.getpass("Insert API_KEY/Consumer Key: \n")
    API_SECRET=getpass.getpass("Insert API_SECRET/Consumer Secret Key: \n")
    ACCESS_TOKEN=getpass.getpass("Insert ACCESS_TOKEN: \n")
    ACCESS_TOKEN_SECRET=getpass.getpass("Insert ACCESS_TOKEN_SECRET: \n")

    bskylogin=input("Insert Bluesky Login: \n")
    bskypw=getpass.getpass("Insert Bluesky Password: \n")
    # hashbskypw= hash_password(bskypw)
    # bluesky api doesn't accept hashed passwords?????????????????

    if not all([API_KEY,API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, bskylogin, bskypw]):
        print("All Fields not filled. Exiting. Rerun Program")
        sys.exit(1)

    _data = { 
        "API_KEY":API_KEY,
        "API_Secret":API_SECRET,
        "ACCESS_TOKEN":ACCESS_TOKEN,
        "ACCESS_TOKEN_SECRET":ACCESS_TOKEN_SECRET,
        "bskylogin":bskylogin,
        "bskypw":bskypw
    }

    store_encrypted_data(_data)
#Add command to run crosspost.py

#11.15.24 added encryption 
# Need to make this an executable on all platforms later. 
# All this does is take user data, create an encrypted file for the CLI Crossposting Script   