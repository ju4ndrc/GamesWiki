from fastapi import APIRouter
from app.services.cheap_service import get_game
from app.services.raw_service import  get_info_game
from app.services.yout_service import get_video
from models.game import Game

router = APIRouter(tags=["game_req"])

@router.get('/search')
async def search_game(searchGame:str):
    info_game =  get_info_game(searchGame)
    
    results = []
    
    for game in info_game:
        price =  get_game(game["name"])
        
        trailer =  get_video(game["name"])
        
        results.append({
            "id":game["id"],
            "title":game["name"],
            "price":price,
            "img":game["image"],
            "raiting":game["rating"],
            "trailer":trailer,
    
        })
    return results
        
        