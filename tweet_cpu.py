#Importing the Module
from twython import Twython
from gpiozero import CPUTemperature
from time import sleep, strftime, time
from random import randint
import httplib, urllib

#Setting i and j to random intergers
i = randint(0, 2)
j = randint(0, 3)


#My keys for twitter API
C_key = "XXXXXXXXXXXXXXXX"
C_secret = "XXXXXXXXXXXXXXXX"
A_token = "XXXXXXXXXXXXXXXX"
A_secret = "XXXXXXXXXXXXXXXX"

#Defining the CPU temperature as a variable
cpu = CPUTemperature()

#Open tag for all CPU posts
opentag = "#ifb102TBOT My core temp is "


#Lists of different tags, chosen randomly by the i and j variables
hot_tag = ["C. I think my owner has forgotten to turn me off. Send help!! ", "C. I could use a serious drink right now. ", "C. Uh Oh, critical temp. "]
tag5 = ["C. It's getting hot in here! ", "C. Nothing like a hot breeze. ", "C. Ahhh, I love the smell of burnt CPUs in the morning. "]
tag4 = ["C. Another day in cyber paradise. ", "C. If you're reading this, delete system32. ", "C. What's a Pi gotta do to get a drink around here? "]
tag3 = ["C. Hello World! ", "C. Moore's Law is overrated. ", "C. Thank you Turing, wait ... am I even a Turing machine? "]
tag2 = ["C. Skynet is online. ", "C. Warmin up for the day. ", "C. I sure do enjoy IFB102 "]
tag1 = ["C. What's up with airplane food? ", "C. DM for a byte to eat. ", "C. Please don't Ddos me, I'm only young. "]
closetag = ['#3.14', '#RaspberryPi', '#LifeofPi', '#TwitterBot']

#Code taken from Pushover API Tutorial, slightly edited to include CPU temp
conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
urllib.urlencode({
"token": "aca8zdv5cvnwnydg8k377ik8c4ibjj",
"user": "uy1nzd13e5x1vi3i1kgin34x7uzx3a",
"message": "Core CPU Temp - " + str(cpu.temperature) + 'C',
}), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()

# Making a function for the temperature posts   
def twitter_post():
    if cpu.temperature >= 54: #If it's above 54, use the hot_tag lines
        tweet = Twython(C_key,C_secret,A_token,A_secret)
        tweet.update_status(status=opentag + str(cpu.temperature) + str(hot_tag[i]) + str(closetag[j]))

    elif cpu.temperature >= 52 < 54:#If it's between 54 and 52, use the tag5 lines
        tweet = Twython(C_key,C_secret,A_token,A_secret)
        tweet.update_status(status=opentag + str(cpu.temperature) + str(tag5[i]) + str(closetag[j]))

    elif cpu.temperature >= 51 < 52:#If it's between 52 and 51, use the tag4 lines
        tweet = Twython(C_key,C_secret,A_token,A_secret)
        tweet.update_status(status=opentag + str(cpu.temperature) + str(tag4[i]) +  str(closetag[j]))

    elif cpu.temperature >= 50 < 51:#If it's between 51 and 50, use the tag3 lines
        tweet = Twython(C_key,C_secret,A_token,A_secret)
        tweet.update_status(status=opentag + str(cpu.temperature) + str(tag3[i]) + str(closetag[j]))

    elif cpu.temperature >= 48 < 50:#If it's between 50 and 48, use the tag2 lines
        tweet = Twython(C_key,C_secret,A_token,A_secret)
        tweet.update_status(status=opentag + str(cpu.temperature) + str(tag2[i]) + str(closetag[j]))

    elif cpu.temperature >= 45 < 48:#If it's between 48 and 45, use the tag1 lines
        tweet = Twython(C_key,C_secret,A_token,A_secret)
        tweet.update_status(status=opentag + str(cpu.temperature) + str(tag1[i]) + str(closetag[j]))

    else:
        tweet = Twython(C_key,C_secret,A_token,A_secret) #If none of these, state it is offline.
        tweet.update_status(status=opentag + " I'm offline for the time being")

#Running my function
twitter_post()
