import httpx
import asyncio

BASE_URL = 'https://www.cheapshark.com/api/1.0/'

# CACHE EN MEMORIA
cache = {}

async def get_game(game_name: str):

    # VERIFICAR CACHE
    if game_name in cache:

        print(f"Usando cache para: {game_name}")

        return cache[game_name]

    url = f"{BASE_URL}games?title={game_name}&limit=1"

    try:

        async with httpx.AsyncClient(
            timeout=10,
            headers={
                "User-Agent": "GameFinder/1.0 (jdramirez90@ucatolica.edu.co)"
            }
        ) as client:

            response = await client.get(url)

        print(url)
        print(response.status_code)

        # RATE LIMIT
        if response.status_code == 429:

            retry = response.headers.get("Retry-After", 5)

            print(f"Bloqueado temporalmente. Esperando {retry} segundos")

            await asyncio.sleep(int(retry))

            return None

        response.raise_for_status()

        data = response.json()

        if not data:
            return None

        game = data[0]

        result = {
            "price": float(game["cheapest"]),
            "deal_id": game["cheapestDealID"],
            "steam_app_id": game.get("steamAppID")
        }

        # GUARDAR EN CACHE
        cache[game_name] = result

        print(f"Guardado en cache: {game_name}")

        return result

    except httpx.HTTPStatusError as e:
        print(f"Error HTTP CheapShark: {e}")

    except httpx.ConnectError as e:
        print(f"Error de conexión CheapShark: {e}")

    except httpx.TimeoutException:
        print("Timeout CheapShark")

    except Exception as e:
        print(f"Error inesperado CheapShark: {e}")

    return None