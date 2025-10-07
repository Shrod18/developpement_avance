movies = []

def create_movie(title: str) -> None:
    movies.append({
        "title": title,
    })

def delete_movie(title: str) -> None:
    movies.pop(title)
