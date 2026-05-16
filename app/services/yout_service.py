import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

def get_video(game_name):
    
    BASE_URL = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={game_name}+trailer&key={API_KEY}"
    
    response = requests.get(BASE_URL)
    data = response.json()
        
    try:
        video_id = data["items"][0]["id"]["videoId"]
        return f"https://www.youtube.com/watch?v={video_id}"
    except:
        return "Problems finding the video"
