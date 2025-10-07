movies = []

def create_movie(title: str) -> None:
    movies.append({
        "title": title,
    })

def delete_movie(title: str) -> None:
    movies.remove({"title":title})

def get_movies():
    return movies
