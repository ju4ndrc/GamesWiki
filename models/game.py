from typing import Optional
from pydantic import BaseModel , Field


class Game(BaseModel):
    id:int
    title:str
    price:float
    img:str
    rating:float
    trailer:str | None
    
