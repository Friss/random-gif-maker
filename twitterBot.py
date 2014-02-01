import base64
import json
import requests
import ConfigParser
import random
import os
import time
import subprocess

from twython import Twython
from base64 import b64encode
from randomGif import makeGif


config = ConfigParser.ConfigParser()
config.read("config.cfg")
config.sections()
ROOT_FOLDER = config.get("general", "movies_path")
CLIENT_ID = config.get("imgur", "client_id")
API_KEY = config.get("imgur", "api_key")
APP_KEY = config.get("twitter", "app_key")
APP_SECRET = config.get("twitter", "app_secret")
OAUTH_TOKEN = config.get("twitter", "oauth_token")
OAUTH_TOKEN_SECRET = config.get("twitter", "oauth_token_secret")

headers = {"Authorization": "Client-ID " + CLIENT_ID}
url = "https://api.imgur.com/3/upload.json"

while True:
	moviename, hour, mins, secs = makeGif(ROOT_FOLDER)

	title = "Random " + moviename + "GIF"
	print title

	# first pass reduce the amount of colors
	if(os.path.getsize('movie.gif') > 2097152):
		subprocess.call(['convert',
						'movie.gif',
						'-layers',
						'Optimize',
						'-colors',
						'64',
						'movie.gif'])

	# other passes reduce the size
	while(os.path.getsize('movie.gif') > 2097152):
		subprocess.call(['convert',
						'movie.gif',
						'-resize',
						'90%',
						'-coalesce',
						'-layers',
						'optimize',
						'movie.gif'])
	
	#If first upload fails try again.
	for i in range(0,2):
		while True:	
			try:
				response = requests.post(
					url,
					headers = headers,
					data = {
						'key': API_KEY,
						'image': b64encode(open('movie.gif', 'rb').read()),
						'type': 'base64',
						'name': 'movie.gif',
						'title': title
					}
				)
			except requests.exceptions.ConnectionError:
				# try again.
				continue
			break;


	try:
		res_json = response.json()
		link = res_json['data']['link']
	except ValueError:
		# try again.
		continue

	print link

	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


	status = title +" " + link + " " + str(hour) +":"+str(mins)+":"+str(secs)+ ' in. #moviegif #gif'

	print "tweeting..."
	twitter.update_status(status=status)

	print "sleeping..."
	# sleep 1 hour
	time.sleep(3600)