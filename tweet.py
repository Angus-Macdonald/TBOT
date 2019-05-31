#Importing Modules
import tweepy
from time import sleep
from keys import *
import httplib, urllib

#Authorising my keys with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Searching for AI with :), 1 result in the items variable
for tweet in tweepy.Cursor(api.search, q='Artificial Intelligence' + ':)').items(1):
	try:
		username = tweet.user.name #Defining twitter username as easy variable
		d= open('./username_db/UsefulHumans.txt', 'a+') #Opening the usefulhumans.txt
	  	d.write(str(username) + '\n') #Writing the username within txt
		tweet.retweet() #Retweeting the post

                #Taken from Pushover Tutorial
		conn = httplib.HTTPSConnection("api.pushover.net:443")
 		conn.request("POST", "/1/messages.json",
 		urllib.urlencode({
		"token": "aca8zdv5cvnwnydg8k377ik8c4ibjj",
  		"user": "uy1nzd13e5x1vi3i1kgin34x7uzx3a",
   		"message": "Another Potential Ally - " + str(username), #Edited the message to include the username
		}), { "Content-type": "application/x-www-form-urlencoded" })
		conn.getresponse()
	except:
		break


