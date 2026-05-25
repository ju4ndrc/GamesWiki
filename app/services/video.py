def get_video(game_name: str):

    if not game_name:
        return None

    query = game_name.strip().replace(" ", "+")

    return (
        "https://www.youtube.com/results?"
        f"search_query={query}+trailer"
    )