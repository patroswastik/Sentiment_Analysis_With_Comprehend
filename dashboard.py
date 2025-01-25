import boto3
import matplotlib.pyplot as plt
from collections import Counter

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
TABLE_NAME = 'tweetsrealtimetable'

def fetch_data():
    table = dynamodb.Table(TABLE_NAME)
    response = table.scan()
    return response['Items']

def visualize_data(data):
    sentiments = [item['detected_sentiment'] for item in data]

    sentiment_counts = Counter(sentiments)

    # Plot pie chart
    labels = sentiment_counts.keys()
    sizes = sentiment_counts.values()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Sentiment Analysis')
    plt.show()

def visualize_data_for_gender(data):
    gender = [item['gender'] for item in data]

    gender_count = Counter(gender)

    # Plot pie chart
    labels = gender_count.keys()
    sizes = gender_count.values()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Tweet Gender Analysis')
    plt.show()

def visualize_data_for_region(data):
    region = [item['region'] for item in data]

    region_count = Counter(region)

    # Plot pie chart
    labels = region_count.keys()
    sizes = region_count.values()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Tweet Region Analysis')
    plt.show()

def visualize_data_for_age(data):
    age = [item['age_range'] for item in data]

    age_count = Counter(age)

    # Plot pie chart
    labels = age_count.keys()
    sizes = age_count.values()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Tweet age Analysis')
    plt.show()

if __name__ == "__main__":
    data = fetch_data()
    # visualize_data(data)
    visualize_data_for_gender(data)
    visualize_data_for_region(data)
    visualize_data_for_age(data)