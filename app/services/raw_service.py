import httpx
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAWG_API")


async def get_info_game(query):

    BASE_URL = f"https://api.rawg.io/api/games?key={API_KEY}&search={query}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL)
        data = response.json()
        
    result = []
    
    for game in data['results'][:5]:
        result.append({
            "id":game["id"],
            "name":game["name"],
            "image":game["background_image"],
            "rating":game["rating"]
        })
    return result
