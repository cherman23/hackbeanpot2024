import json
import googleapiclient.discovery
import googleapiclient.errors
import os
from dotenv import load_dotenv

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and_secret.
CLIENT_SECRETS_FILE = "client_secrets.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_local_server(port=8080)
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

# Build the service
youtube = get_authenticated_service()
# Define the video IDs
# Load video IDs from a JSON file
with open('idTable.json') as f:
    video_ids = json.load(f)
# Fetch the playlist title
# playlist_title = fetch_playlist_title()

# Create a new playlist
playlist = youtube.playlists().insert(
    part='snippet,status',
    body={
        'snippet': {
            'title': "Learn more about {topic}!",
            'description': 'This is my playlist created by LearnFlow to learn {topic}!'
        },
        'status': {
            'privacyStatus': 'public'
        }
    }
).execute()

while not os.path.exists('idTable.json'):
    pass

# Add videos to the playlist
for video_id in video_ids:
    youtube.playlistItems().insert(
        part='snippet',
        body={
            'snippet': {
                'playlistId': playlist['id'],
                'resourceId': {
                    'kind': 'youtube#video',
                    'videoId': video_id
                }
            }
        }
    ).execute()

    # Get the playlist URL
playlist_url = f"https://www.youtube.com/playlist?list={playlist['id']}"
print(f"Playlist URL: {playlist_url}")

print('Playlist created successfully!')

# Delete the video IDs file
os.remove('idTable.json')

# Delete the topics file
os.remove('topics.json')
