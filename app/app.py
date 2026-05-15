from fastapi import FastAPI
from app.router import game_router
app = FastAPI()


app.include_router(game_router.router)

@app.get('/')
async def root():
    return{'Hello':'World'}