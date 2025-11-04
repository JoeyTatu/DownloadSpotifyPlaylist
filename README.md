# DownloadSpotifyPlaylist

# Getting your Client ID and Client Secret.
1. Login into Spotify Developers and go to the Dashboard: (developer.spotify.com/dashboard)(https://developer.spotify.com/dashboard)
2. Select "Create app"
3. Insert an app name and app description (anything you want)
4. Set the Redirect URIs to http://&#8203;127.0.0.1:8888/callback
5. Select "Web API" and "I understand and agree with Spotify's Developer Terms of Service and Design Guidelines"
6. Select Save
7. Copy and save your Client ID
8. Selct "View client secret", copy and save your Client Secret

# Download playlist from old account
1. Go to the file `export_playlist.py`
3. Add your Client ID into the `CLIENT_ID` section
4. Add your Client Secret into the `CLIENT_SECRET` section
5. Go to (open.spotify.com)(https://open.spotify.com)
6. Select your playlist
7. From the URL, take the Playlist ID.
   <br>For example: https:&#8203;//open.spotify.com/playlist/32zeeaKANoo9ZWuBdNc8VE
   <br>Playlist ID is 32zeeaKANoo9ZWuBdNc8VE
8. Add Playlist ID to `SOURCE_PLAYLIST_ID`
9. Go to [spotify.com/account/profile/](https://www.spotify.com/account/profile/) to get your username
10. Add your username to `OLD_ACCOUNT`
11. Run `export_playlist.py`, and autorise.
12. The file playlist.json will be created with Spotify IDs of songs in your playlist.

# Upload playlist to new account
1. Ensure you clear cache for Spotify.
2. Log into your NEW Spotify account.
3. Go to the file `importPlaylist.py`
4. Create a new app in your new account to get your Client ID and Client Secret.
   <br>(Do not use the other ones, as they are for the other account only!!!)
5. Add your new Client ID into the `CLIENT_ID` section
6. Add your new Client Secret into the `CLIENT_SECRET` section
7. Go to [spotify.com/account/profile/](https://www.spotify.com/account/profile/) to get your username
8. Add your username to `NEW_ACCOUNT`
9. Add a playlist name (of your choice) to `NEW_PLAYLIST_NAME`
10. Run `importPlaylist.py`.
11. New playlist appears in Spotify.
