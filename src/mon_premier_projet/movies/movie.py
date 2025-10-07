movies = []

def create_movie(title: str, year: int) -> None:
    movies.append({
        "title": title,
    })

def delete_movie(movie_id: int) -> None:
    movies.pop(movie_id)
