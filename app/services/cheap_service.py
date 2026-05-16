import requests

BASE_URL = 'https://www.cheapshark.com/api/1.0/'

def get_game(game_name: str):
    url = f"{BASE_URL}games?title={game_name}&limit=5"
    
    response = requests.get(url)
    data = response.json()

    if not data:
        return None

    game = data[0]

    return {
        "price": float(game["cheapest"]),
        "deal_id": game["cheapestDealID"],
        "steam_app_id": game.get("steamAppId")
    }
