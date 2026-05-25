import httpx
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAWG_API")

async def get_info_game(query):

    BASE_URL = "https://api.rawg.io/api/games"

    params = {
        "key": API_KEY,
        "search": query
    }

    try:

        async with httpx.AsyncClient(timeout=15) as client:

            response = await client.get(
                BASE_URL,
                params=params
            )

            response.raise_for_status()

            data = response.json()

            result = []

            for game in data["results"][:7]:

                platforms = []

                if game.get("platforms"):

                    platforms = [
                        p["platform"]["slug"]
                        for p in game["platforms"]
                    ]

                genres = []

                if game.get("genres"):

                    genres = [
                        g["slug"]
                        for g in game["genres"]
                    ]

                result.append({
                    "id": game["id"],
                    "name": game["name"],
                    "image": game["background_image"],
                    "rating": game["rating"],
                    "platforms": platforms,
                    "genres": genres
                })

            return result

    except httpx.HTTPError as e:

        print("Error HTTP RAWG:", e)

        return []

    except Exception as e:

        print("Error RAWG:", e)

        return []