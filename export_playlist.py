import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# ---- CONFIG ----
CLIENT_ID = 'ADD_CLIENT_ID'
CLIENT_SECRET = 'ADD_CLIENT_SECRET'
REDIRECT_URI = "http://127.0.0.1:8888/callback"
OLD_ACCOUNT = "ADD_USERNAME"
SOURCE_PLAYLIST_ID = "ADD_PLAYLIST_ID"
OUTPUT_FILE = "playlist.json"
# ----------------

# Authenticate
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-read-private",
    username=OLD_ACCOUNT
))

# Get tracks
tracks = []
results = sp.playlist_items(SOURCE_PLAYLIST_ID)
while results:
    tracks.extend([item['track']['uri'] for item in results['items']])
    if results['next']:
        results = sp.next(results)
    else:
        results = None

# Save to file
with open(OUTPUT_FILE, "w") as f:
    json.dump(tracks, f, indent=2)

print(f"Playlist saved! {len(tracks)} tracks written to {OUTPUT_FILE}")
