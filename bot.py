import tweepy
from tweepy import OAuthHandler

import gspread
from oauth2client.service_account import ServiceAccountCredentials

CONSUMER_KEY = <CONSUMER_KEY>
CONSUMER_SECRET = <CONSUMER_SECRET>
ACCESS_KEY = <ACCESS_KEY>
ACCESS_SECRET = <ACCESS_SECRET>

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name(<FILE_CLIENT_SECRET>, scope)
client = gspread.authorize(creds)
sheet = client.open('bot-twitter').sheet1

auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api = tweepy.API(auth)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
line = 1
limit = range(1000,50000)
sheet.update_cell(line,1, 'Name')
sheet.update_cell(line,2, 'Followers')
api = tweepy.API(auth)	
for tweet in tweepy.Cursor(api.search, q='#mentalhealth, #mindfulness').items(100):
	if(tweet.user.followers_count in limit):
		line += 1
		sheet.update_cell(line,1, tweet.user.name)
		sheet.update_cell(line,2, tweet.user.followers_count)
