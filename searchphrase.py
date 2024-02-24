import requests
import json
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv('youtubekey')

max_results = 10  # Number of results you want to retrieve

with open('search_queries.json') as f:
    data = json.load(f)
    phrases = data['phrases']

videos = []

for phrase in phrases:
    query = phrase.replace(" ", "+")
    url = f'https://www.googleapis.com/youtube/v3/search?key={API_KEY}&part=snippet&q={query}&maxResults={max_results}'
    response = requests.get(url)
    data = response.json()

    for item in data.get('items', []):
        try:
            video_id = item['id']['videoId']
            title = item['snippet']['title']
            video_url = f'https://www.youtube.com/watch?v={video_id}'
            videos.append({'title': title, 'url': video_url})
        except KeyError:
            # Handle missing 'videoId' key
            print(f"Skipping item: {item}")

with open('videos.json', 'w') as outfile:
    json.dump(videos, outfile, indent=4)

print('Videos exported to videos.json')
