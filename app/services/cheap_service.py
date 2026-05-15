import httpx

BASE_URL = 'https://www.cheapshark.com/api/1.0/'

# https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15

async def get_game(game_name:str):
    
    url = f"{BASE_URL}games?title={game_name}&limit=5"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    if not data:
        return None
    game = data[0]
    
    return{
        "price":float(game["cheapest"]),
        "deal_id":game["cheapestDealID"],
        "steam_app_id":game.get("steamAppId")
    }