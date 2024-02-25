import json
import googleapiclient.discovery
import googleapiclient.errors
import os
from dotenv import load_dotenv

# Set up the YouTube Data API client
load_dotenv()  # Load environment variables from .env file
youtube_key = os.getenv('youtubekey')
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=youtube_key)

# Load search terms from topics.json
while not os.path.exists('topics.json'):
    pass

# Checks every element in the topics.json file to make sure none are empty

with open('topics.json') as f:
    topics_data = json.load(f)

topics_data['outputs'] = [term for term in topics_data.get('outputs', []) if term]

# Extract items from the JSON data
search_terms = []
for outputs in topics_data.get('outputs', []):
    for term in outputs:
        search_terms.append(term)

# Search each term on YouTube and extract the ID of the first video
video_ids = []
for term in search_terms:
    try:
        search_response = youtube.search().list(
            q=term,
            part='id',
            maxResults=1
        ).execute()
        if 'items' in search_response and search_response['items']:
            video_id = search_response['items'][0]['id'].get('videoId')
            if video_id:
                video_ids.append(video_id)
    except googleapiclient.errors.HttpError as e:
        print(f'An error occurred while searching for "{term}": {e}')

# Save the video IDs to idtable.json
with open('idtable.json', 'w') as f:
    json.dump(video_ids, f)

# Checker to see if the file was created, else wait 1 second and check again

