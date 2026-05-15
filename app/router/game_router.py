from fastapi import APIRouter
from app.services.cheap_service import get_game
from app.services.raw_service import  get_info_game
from app.services.yout_service import get_video
from models.game import Game

router = APIRouter(tags=["game_req"])

@router.get('/search')
async def search_game(searchGame:str):
    info_game = await get_info_game(searchGame)
    
    results = []
    
    for game in info_game:
        price = await get_game(game["name"])
        
        trailer = await get_video(game["name"])
        
        results.append({
            "id":game["id"],
            "title":game["title"],
            "price":price,
            "img":game["img"],
            "raiting":game["raiting"],
            "trailer":trailer,
    
        })
    return results
        
        