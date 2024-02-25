import googleapiclient.discovery

# Replace 'YOUR_API_KEY' with your actual YouTube Data API key
api_key = 'AIzaSyD3J6UJglIu5ioeDt2exE89PoQJ7KL2Vqs'
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

# Replace 'VIDEO_ID_1' through 'VIDEO_ID_9' with your actual YouTube video IDs
video_ids = ['ORMx45xqWkA', 'r2JKV4_zlmM', 'V_xro1bcAuA', 'OIenNRt2bjg', 'Z_ikDlimN6A', 'lM23Y1XFd2Q', 'tHL5STNJKag', 'ORMx45xqWkA', 'V_xro1bcAuA"']

# Function to get video titles
def get_video_titles(video_ids):
    titles = []
    for video_id in video_ids:
        request = youtube.videos().list(part='snippet', id=video_id)
        response = request.execute()
        title = response['items'][0]['snippet']['title']
        titles.append(title)
    return titles

# Split the titles into three different lists (change the logic based on your requirements)
titles = get_video_titles(video_ids)
list1 = titles[:len(titles)//3]
list2 = titles[len(titles)//3:2*len(titles)//3]
list3 = titles[2*len(titles)//3:]

# Print or use the lists as needed
print("Beginner", list1)
print("Intermediate", list2)
print("Advanced", list3)
