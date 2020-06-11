import spotipy
import spotipy.util as util

token = util.prompt_for_user_token(
        username="INSERT_SPOTIFY_USERNAME",
        scope="user-follow-read",
        client_id="INSERT_CLIENT_ID",
        client_secret="INSERT_CLIENT_SECRET",
        redirect_uri="INSERT_REDIRECT_URI")

spotify = spotipy.Spotify(auth=token)

def getFollowedArtists(afterId):
	current_user_followed_artists = spotify.current_user_followed_artists(limit=50,after=afterId)
	return current_user_followed_artists
###########################################################################################

artistId=""
artistName=""

for i in range(14): #INSERT THE NUMBER OF ARTISTS YOU FOLLOW ON SPOTIFY DIVIDED BY 50. DO NOT EXCEED 14 SINCE THE CRAWL WILL TAKE LONGER THAN HEROKU'S MAXIMUM BOOT TIMEOUT
	if i==0:
		followedArtistsJson=getFollowedArtists(None) #retrieving first 50
		for j in range(len(followedArtistsJson['artists']['items'])):
			artistId=followedArtistsJson['artists']['items'][j]['id']
			artistName=followedArtistsJson['artists']['items'][j]['name']
			print(artistId+'	###'+artistName)
	
	else:
		followedArtistsJson=getFollowedArtists(artistId) #here artistId will be the last one from before
		for j in range(len(followedArtistsJson['artists']['items'])):
			artistId=followedArtistsJson['artists']['items'][j]['id']
			artistName=followedArtistsJson['artists']['items'][j]['name']
			print(artistId+'	###'+artistName)
