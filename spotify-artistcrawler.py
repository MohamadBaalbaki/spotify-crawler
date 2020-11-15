import spotipy
import spotipy.util as util

FOLLOWED_ARTISTS_COUNT = 250 #do not exceed 700
OFFSET = 50

token = util.prompt_for_user_token(
        username = "INSERT_SPOTIFY_USERNAME",
        scope = "user-follow-read",
        client_id = "INSERT_CLIENT_ID",
        client_secret = "INSERT_CLIENT_SECRET",
        redirect_uri = "INSERT_REDIRECT_URI")

spotify = spotipy.Spotify(auth = token)

def getFollowedArtistsByBatch(afterId):
	current_user_followed_artists = spotify.current_user_followed_artists(limit = OFFSET, after = afterId)
	return current_user_followed_artists
	
def getAllFollowedArtists():
	artistId = ""
	artistName = ""

	for i in range(FOLLOWED_ARTISTS_COUNT // OFFSET):
		followedArtistsJson = getFollowedArtistsByBatch(artistId if i!=0 else None)
		for j in range(len(followedArtistsJson['artists']['items'])):
			artistId = followedArtistsJson['artists']['items'][j]['id']
			artistName = followedArtistsJson['artists']['items'][j]['name']
			print(artistId + '	###' + artistName)

###########################################################################################
getAllFollowedArtists()
