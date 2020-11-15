import spotipy
import spotipy.util as util
import re
from datetime import datetime as dt
import sendgrid
from sendgrid.helpers.mail import *
import os
from sendgrid.helpers.mail import To

sg = sendgrid.SendGridAPIClient(os.environ.get('INSERT_SENDGRID_API_KEY'))

token = util.prompt_for_user_token(
        username = "INSERT_SPOTIFY_USERNAME",
        scope = "user-follow-read",
        client_id = "INSERT_CLIENT_ID",
        client_secret = "INSERT_CLIENT_SECRET",
        redirect_uri = "INSERT_REDIRECT_URI")

spotify = spotipy.Spotify(auth = token)

msg = ""

def getNewReleasesOfArtist(artistName, uri):
	global msg
	results = spotify.artist_albums(uri, album_type = None)
	albums = results['items']
	if len(albums) != 0:
		while results['next']:
		    results = spotify.next(results)
		    albums.extend(results['items'])
		for i in range(len(albums)):	
			if albums[i]['release_date_precision'] != 'year':	
				releaseAsDate = dt.strptime(albums[i]['release_date'], "%Y-%m-%d").replace(hour = 0, minute = 0, second = 0, microsecond = 0)
				dateToday = dt.today().replace(hour = 0, minute = 0, second = 0, microsecond = 0)
				if releaseAsDate == dateToday:
					msg = msg + artistName + '\n' + albums[i]['name'] + '\n' + albums[i]['external_urls']['spotify'] + '\n' + '\n'
					break

def fetchResults():
	artistId = ""
	artistName = ""
	artistsFile = open("artists.txt", "r")
	for line in artistsFile:
		artistId = re.sub(r'\t###.+\n', '', line)
		artistName = re.sub(r'.+###', '', line)
		artistName = artistName[:-1] #remove \n
		birdy_uri = 'spotify:artist:' + artistId
		getNewReleasesOfArtist(artistName, birdy_uri)
		
def sendEmails(msg):
	from_email = Email("INSERT_THE_SENDGRID_SENDER_EMAIL")
	subject = 'Spotify Releases Today: ' + f"{dt.now():%d/%m/%Y}"
	to_emails = To("INSERT_EMAIL_TO_SEND_TO")
	#to_emails = [To('INSERT_EMAIL1_TO_SEND_TO'), To('INSERT_EMAIL2_TO_SEND_TO')]
	
	if not msg: msg = 'There are no new releases today'
		
	content = Content("text/plain", msg)
	mail = Mail(from_email, to_emails, subject , content)
	response = sg.send(mail)

###########################################################################################
fetchResults()
sendEmails(msg)
