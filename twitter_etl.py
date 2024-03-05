import tweepy
import pandas as pd
import time
import requests
from datetime import datetime


def run_twitter_etl():
    
    # To set your environment variables in your terminal run the following line:
    # export 'BEARER_TOKEN'='<your_bearer_token>'
    bearer_token = "" # Add your bearer token

    client = tweepy.Client(bearer_token, wait_on_rate_limit=True)

    # Get user ID for screen name
    # Specify the username
    username = "elonmusk"

    # Define the endpoint URL
    url = f"https://api.twitter.com/2/users/by/username/{username}"

    # Set the authorization header
    headers = {"Authorization": f"Bearer {bearer_token}"}

    # Send the request to Twitter API v2
    response = requests.get(url, headers=headers)
    user_data = response.json()
    #print(user_data)

    # Extract the user ID
    user_id = user_data['data']['id']

    # Define the endpoint URL for fetching user timeline
    timeline_url = f"https://api.twitter.com/2/users/{user_id}/tweets"

    # Define parameters for pagination
    params = {
        "max_results": 100,  # Maximum number of tweets per request (100 is the maximum allowed)
        "tweet.fields": "created_at",  # Include tweet creation timestamp
    }

    # Send the request to Twitter API v2 to fetch user timeline
    timeline_response = requests.get(timeline_url, headers=headers, params=params)
    print(timeline_response)
    print(timeline_response.json())
    timeline_data = timeline_response.json()
    #print(timeline_data)


    data = pd.DataFrame()
    # Print the tweets
    for tweet in timeline_data['data']:
        #print(tweet)
        raw_data = pd.json_normalize(tweet)
        data = pd.concat([data, raw_data])

    #print(data)
    data = data[['id', 'created_at', 'text']]
    timestr = datetime.now().strftime("%Y%m%d-%H%M%S")
    data.to_csv("s3://nidhi-twitter-airflow-etl/tweet_data"+timestr+".csv", index=False) # add your s3 destination


#run_twitter_etl()

