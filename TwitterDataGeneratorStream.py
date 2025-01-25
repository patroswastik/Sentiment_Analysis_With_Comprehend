import boto3
import pandas as pd
import json
import time
from faker import Faker
import random

fake = Faker()
kinesis = boto3.client('kinesis', region_name='us-east-1')

df = pd.read_csv('train.csv')  # Ensure train.csv is in the working directory

age_ranges = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
genders = ['Male', 'Female', 'Non-binary']

def send_tweets_to_kinesis():
    for _, row in df.iterrows():
        tweet_data = {
            'id': str(row['id']),
            'text': row['tweet'],
            'username': fake.user_name(),
            'age_range': random.choice(age_ranges),
            'gender': random.choice(genders),
            'region': fake.country(),
            'timestamp': pd.Timestamp.now().isoformat()
        }
        # Send data to Kinesis stream
        kinesis.put_record(
            StreamName='SocialTweetStream',
            Data=json.dumps(tweet_data),
            PartitionKey=tweet_data['username']
        )
        print(f"Sent: {tweet_data}")
        time.sleep(0.5)

if __name__ == "__main__":
    send_tweets_to_kinesis()