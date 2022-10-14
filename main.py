import tweepy
from urllib.request import urlopen
from bs4 import BeautifulSoup

#########################################################################################
# Twitter API setup

# reading keys from file

# open keys.txt file
file = open("C:\\Users\\Daniel\\Desktop\\keys.txt", "r")
read = file.readlines()

# create new array for elements
modified = []

for line in read:
    modified.append(line.strip())

# keys
api_key = modified[0]
api_key_secret = modified[1]
access_token = modified[2]
access_token_secret = modified[3] 


# basic authentication 

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit = True)

print("auth OK...")
#########################################################################################

# functions

def get_index_data(url):

    print("finding data...")

    # define array for collecting values
    data = []

    # read data from internet
    html = urlopen(url, timeout = 10).read()
    soup = BeautifulSoup(html, "html.parser")

    # GET data from specific elements
    city = soup.find("a", attrs = {"class" : "YMlKec fxKbKc"}) # kaupungin nimi
    tapahtuma = soup.find("div", attrs = {"class" : "P6K39c"}) # get last days closing points
    aika = soup.find("div", attrs = {"class" : "zzDege"}) # get index name
    
    # converting to float for calculations
    points_now_format = float(city.text.replace(",", ""))
    points_start_format = float(tapahtuma.text.replace(",", ""))

    # counting prosentual rise/fall of index 
    #prosentual_rise = str("{0:.2f}".format(((points_now_format / points_start_format) - 1) * 100))

    # append data to array
    data.append(aika.text)
    data.append(city.text)
    data.append(aika.text)

    # return data[]
    return data

# Tweet data
def tweetAll() :

    # URLs 

    # url0 = "https://www.tilannehuone.fi/index.php"
    url1 =  "https://www.google.com/finance/quote/OMXHPI:INDEXNASDAQ"
    # url3 = 
    # url4 =
    # url5 =
    # url6 =
    # url7 =

    # dax_data = get_index_data(url0)[0] + ": " + get_index_data(url0)[1] + " " + get_index_data(url0)[2] 
    data = get_index_data(url1)[0] + ": " + get_index_data(url1)[1] + " " + get_index_data(url1)[2]

    # Posting tweet
    print("updating twitter status...")
    api.update_status(data)
    print("Status updated!")

tweetAll()