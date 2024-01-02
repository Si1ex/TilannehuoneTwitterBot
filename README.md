# Project Title

**Real-time Emergency Alerts Twitter Bot**

## Description

This Python script utilizes the Tweepy library to create a Twitter bot that automatically tweets real-time emergency alerts from the Tilannehuone website. The script extracts information about emergency events in Finland and posts them on Twitter.

## Prerequisites

Before running the script, make sure you have the necessary dependencies installed. You can install them using the following command:

```bash
pip install tweepy requests beautifulsoup4 python-dotenv
```

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/your-username/your-repository.git
   cd your-repository```
2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```pip install -r requirements.txt```
4. Create a .env file and add your Twitter API credentials:
   ```
   API_KEY=your_api_key
   API_KEY_SECRET=your_api_key_secret
   ACCESS_TOKEN=your_access_token
   ACCESS_TOKEN_SECRET=your_access_token_secret```
5. Run the script:
   ```python your_script.py```

## Code Structure

your_script.py: The main script containing the Twitter bot logic.
requirements.txt: A file listing all Python dependencies.

## Usage

The script is set up to fetch data from the Tilannehuone website and post alerts on Twitter. To use it, simply run the script, and it will print status messages indicating the process.

## Acknowledgments
Tweepy: Library for accessing the Twitter API.
Requests: HTTP library for making requests.
Beautiful Soup: Library for pulling data out of HTML and XML files.
python-dotenv: Library for reading variables from a .env file.

## License
This project is licensed under the MIT License.

## Author
Daniel Kurhinen (and ChatGPT)
