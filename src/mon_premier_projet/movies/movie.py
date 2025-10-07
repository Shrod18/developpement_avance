movies = []

def add_movie(title: str) -> None:
    movies.append({
        "title": title,
    })

def remove_movie(title: str) -> None:
    movies.remove({"title":title})

def get_movies():
    return movies
