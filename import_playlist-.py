import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# ---- CONFIG ----
CLIENT_ID = "ADD_CLIENT_ID"
CLIENT_SECRET = "ADD_CLIENT_SECRET"
REDIRECT_URI = "http://127.0.0.1:8888/callback"
NEW_ACCOUNT = "ADD_USERNAME"
NEW_PLAYLIST_NAME = "ADD_PLAYLIST_NAME"
INPUT_FILE = "playlist.json"
# ----------------

# Authenticate
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-private playlist-modify-public",
    username=NEW_ACCOUNT
))

# Load playlist from file
with open(INPUT_FILE, "r") as f:
    tracks = json.load(f)

# Create new playlist
new_playlist = sp.user_playlist_create(user=NEW_ACCOUNT,
                                       name=NEW_PLAYLIST_NAME,
                                       public=True)

# Add tracks in batches of 100
for i in range(0, len(tracks), 100):
    sp.playlist_add_items(new_playlist['id'], tracks[i:i+100])

print(f"Playlist imported! Total tracks: {len(tracks)}")
