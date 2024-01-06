import tweepy
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import logging
import time

# Load environment variables from the .env file
load_dotenv()

# Initialize Tweepy client outside the Lambda handler
client = tweepy.Client(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_KEY_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

print("auth OK...")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

EMERGENCY_FILE_PATH = "tmp/last_emergency.txt"
MAX_RETRIES = 3

def make_twitter_request(api, endpoint, **params):
    retries = 0

    while retries < MAX_RETRIES:
        try:
            # Make the API request
            response = api.create_tweet(text=params['status'])
            return response

        except tweepy.TweepyException as e:
            # Handle rate limit exceeded
            logger.warning(f"Rate limit exceeded. Retrying in {2 ** retries} seconds.")
            time.sleep(2 ** retries)
            retries += 1

        except Exception as e:
            # Handle other exceptions
            logger.error(f"An error occurred: {e}")
            break

    logger.error("Max retries reached. Unable to complete the request.")
    return None

def get_last_emergency():
    try:
        with open(EMERGENCY_FILE_PATH, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def set_last_emergency(last_emergency):
    with open(f"/{EMERGENCY_FILE_PATH}", "w") as file:
        last_emergency_str = "\n".join(last_emergency)
        file.write(last_emergency_str)

def get_index_data(url):
    data = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        logger.error("Error fetching page")
        return None

    soup = BeautifulSoup(response.content, "html.parser")
    
    results = [td.get_text(strip=True) for td in soup.find_all("td", {"width": "100%"})]

    city = soup.find("td", class_="kunta").text.strip() if soup.find("td", class_="kunta") else "Kaupunki ei saatavilla"
    ajankohta = soup.find("td", class_="pvm").text.strip() if soup.find("td", class_="pvm") else "Aika ei saatavilla"
    tapahtuma = results[1] if len(results) > 1 else ""

    data.extend([city, ajankohta, tapahtuma])
    return data

def tweet_all(data):
    logger.info("Finding data...")
    tweet = f"Hälytys! Paikkakunnalla {data[0]} ajankohtana {data[1]} tapahtui {data[2]}"

    last_emergency = get_last_emergency()
    if data != last_emergency:
        logger.info("Updating Twitter status...")
        try:
            make_twitter_request(client, 'statuses/update', status=tweet)
            logger.info("Status updated!")

            set_last_emergency(data)
        except tweepy.errors.Forbidden as e:
            logger.error(f"Error posting tweet: {e}")
    else:
        logger.info("No new emergency to tweet.")

def lambda_handler(event, context):
    url = "https://www.tilannehuone.fi/halytys.php"
    data = get_index_data(url)

    if data:
        tweet_all(data)

# This block is necessary for local testing (not for AWS Lambda)
if __name__ == "__main__":
    lambda_handler(None, None)
