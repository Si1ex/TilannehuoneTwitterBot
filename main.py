import tweepy
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

client = tweepy.Client(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_KEY_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

print("auth OK...")

# Function to get data from the website
def get_index_data(url):
    # define array for collecting values
    data = []

    # Set the user agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # read data from the internet with the user agent
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Error fetching page")
        exit()
    else:
        content = response.content

    soup = BeautifulSoup(content, "html.parser")
    
    results = []
    
    # GET data from specific elements
    city_element = soup.find("td", class_="kunta")
    pvm_td_element = soup.find("td", class_="pvm")
    td_elements = soup.find_all("td", {"width": "100%"})
    
    #Iterating over a list of HTML td elements
    for td_element in td_elements:
        text_content = td_element.get_text(strip=True)
        results.append(text_content)
        
    city = city_element.text.strip() if city_element else "Kaupunki ei saatavilla"
    
    ajankohta = pvm_td_element.text.strip() if pvm_td_element else "Aika ei saatavilla"
    
    tapahtuma = results[1]
    
    # Append extracted data to the array
    data.append(city)
    data.append(ajankohta)
    data.append(tapahtuma)
    return data

# Tweet data
def tweetAll(data):
    print("finding data...")

    # Format the tweet string
    tweet = f"Hälytys! Paikkakunnalla {data[0]} ajankohtana {data[1]} tapahtui {data[2]}"

    # Posting tweet
    print("updating twitter status...")
    client.create_tweet(text=tweet)
    print("Status updated!")

# Example usage
url = "https://www.tilannehuone.fi/halytys.php"
data = get_index_data(url)
tweetAll(data)