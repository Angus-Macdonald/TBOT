
# Importing Modules
import tweepy
from time import sleep
from keys import *
import httplib, urllib

#Authorising my request with my Twitter Api Keys, I've hidden them in
#another file and imported them in above

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Search query for 'Elon Musk', looking for 1 result in the items parameter.
for tweet in tweepy.Cursor(api.search, q='Elon Musk').items(1):
	try:
		username = tweet.user.name #Defining the username as a variable
		d= open('./username_db/RemoveHumans.txt', 'a+') #Opening RemoveHumans.txt
	  	d.write(str(username) + '\n') #Writing their name within the txt

                ## The following python code has been taken from the Pushover Tutorial
		conn = httplib.HTTPSConnection("api.pushover.net:443")
 		conn.request("POST", "/1/messages.json",
 		urllib.urlencode({
		"token": "aca8zdv5cvnwnydg8k377ik8c4ibjj",
  		"user": "uy1nzd13e5x1vi3i1kgin34x7uzx3a",
   		"message": "Another Potential Enemy - " + str(username), #I've edited the notification to contain the username
		}), { "Content-type": "application/x-www-form-urlencoded" })
		conn.getresponse()
	except:
		break
