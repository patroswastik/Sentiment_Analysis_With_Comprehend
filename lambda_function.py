import boto3
import json
import base64
import logging
from decimal import Decimal
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize resources and constants
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
TABLE_NAME = 'SentimentAnalysis'
analyzer = SentimentIntensityAnalyzer()  # Initialize VADER sentiment analyzer

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)

    for record in event['Records']:
        try:
            # Decode Base64-encoded Kinesis data
            encoded_data = record['kinesis']['data']
            decoded_data = base64.b64decode(encoded_data).decode('utf-8')

            # Parse JSON payload
            payload = json.loads(decoded_data)
            text = payload.get('text', '')
            if not text:
                logger.warning("No text field in payload, skipping record.")
                continue
            logger.info(f"Processing text: {text}")

            # Analyze sentiment using VADER
            scores = analyzer.polarity_scores(text)
            sentiment = (
                "Positive" if scores['compound'] > 0.05
                else "Negative" if scores['compound'] < -0.05
                else "Neutral"
            )
            sentiment_score = Decimal(str(scores['compound']))

            # Store data in DynamoDB
            table.put_item(
                Item={
                    'TweetID': payload['tweet_id'],
                    'User': payload['user'],
                    'Text': text,
                    'Sentiment': sentiment,
                    'SentimentScore': sentiment_score,
                    'Timestamp': payload['timestamp']
                }
            )
            logger.info(f"Stored record in DynamoDB: {payload['tweet_id']}")

        except KeyError as e:
            logger.error(f"Missing key in payload: {e}")
        except Exception as e:
            logger.error(f"Error processing record: {e}")
            raise

    return {"statusCode": 200, "body": "Processed successfully"}
