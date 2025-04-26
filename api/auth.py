import tweepy

def twit_connection(creds):
    # Define Keys
    consumer_key = creds['twitter']['consumer_key']
    consumer_secret = creds['twitter']['consumer_secret']

    # Access:
    access_token = creds['twitter']['access_token']
    access_secret = creds['twitter']['access_secret']

    client = tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_secret)

    return client


# version 1 method
def twit_connection_v1(creds):
    # Define Keys
    consumer_key = creds['twitter']['consumer_key']
    consumer_secret = creds['twitter']['consumer_secret']

    # Access:
    access_token = creds['twitter']['access_token']
    access_secret = creds['twitter']['access_secret']

    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    return tweepy.API(auth)