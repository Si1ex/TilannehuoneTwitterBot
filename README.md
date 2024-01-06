# TilannehuoneBot

**Real-time Emergency Alerts Twitter Bot**

## Description

This Python script utilizes the Tweepy library to create a Twitter bot that automatically tweets real-time emergency alerts from the Tilannehuone website. The script extracts information about emergency events in Finland and posts them on Twitter.

## Prerequisites

Before running the script, make sure you have the necessary dependencies installed. You can install them using the following command:

```bash
pip install tweepy requests beautifulsoup4 python-dotenv
````

Please replace `your_api_key`, `your_api_key_secret`, `your_access_token`, and `your_access_token_secret` with your actual Twitter API keys and tokens. The script is currently set to scrape data from "https://www.tilannehuone.fi/halytys.php", but you can modify this to suit your needs.

Create a .env file in the same directory as the script, and add your Twitter API keys and tokens:
````
API_KEY=your_api_key
API_KEY_SECRET=your_api_key_secret
ACCESS_TOKEN=your_access_token
ACCESS_TOKEN_SECRET=your_access_token_secret
````
Create a folder "tmp" and create a file called last_emergency.txt in that folder.

Run the script with Python:
````
python lambda_function.py
````

Made by Daniel Kurhinen (and ChatGPT)
