import boto3
import json
import time
from faker import Faker
import pandas as pd

# Initialize Faker and Kinesis client
fake = Faker()
kinesis = boto3.client('kinesis', region_name='us-east-1')

# Define your Kinesis Stream Name
STREAM_NAME = "SocialMediaStream"

# Function to generate fake tweets
def generate_fake_tweet():
    return {
        "tweet_id": fake.uuid4(),
        "user": fake.user_name(),
        "text": fake.text(max_nb_chars=140),
        "timestamp": fake.iso8601()
    }

# Function to send data to Kinesis
def send_data_to_kinesis():
    df = pd.read_csv("train.csv")
    while True:
        

        # Generate a fake tweet
        tweet = generate_fake_tweet()
        print(f"Sending tweet: {tweet}")

        # Send the tweet to Kinesis
        response = kinesis.put_record(
            StreamName=STREAM_NAME,
            Data=json.dumps(tweet),
            PartitionKey="partition_key"
        )
        print(f"Response: {response}")

        # Wait 1 second before sending the next tweet
        time.sleep(1)

# Run the script
if __name__ == "__main__":
    send_data_to_kinesis()
