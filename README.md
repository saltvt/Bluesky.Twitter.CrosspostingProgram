**This is a simple python program that crossposts to both X(formerly Twitter) and Bluesky Social Media Platform. Runs in the command line and is designed for Power Users. I made this because there really are no good alternatives outside of Buffer. Constantly tinkering with the code so expect more functionality as time passes. Adding image posting and UI eventually.**

Requires developer account access from twitter. => https://developer.x.com/en
    Step 1. Create an application that has Read and Write permissions
    !(images/ApplicationSetup.png)
    !(images/applicationSetup2.png)
    Step 2. Make sure to create your consumer keys to connect to the API
    !(images/KeySetup.png)
    Step 3. Make sure to create your authentication/access keys for the twitter account of your choice
    !(AuthenticationTokens.png)


Dependencies neeeded to run this program:
    -AtProto
    -Normalizer
    -tweepy
    -Python3.12

To run the program:
    1. Download the files from src into a directory of choice. 
    2. Create a virtual environment in the directory(Highly Recommended!)
    3. pip install -r requirements.txt
    4. Run python config.py to generate data
    5. Run python crosspost.py "With your post adjacent in the command line"

I recommend making an alias in your ./bashrc or ./zsh file so that you can just use keywords such as "post" and "tweet" to run the program.

## THIS APPLICATION IS FOR PERSONAL USE ONLY AND IS UNSECURE AT THE MOMENT PLEASE DO NOT USE THIS FOR ANYTHING OTHER THAN PERSONAL USE ##
- Salt 🖤




