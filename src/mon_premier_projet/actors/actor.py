actors = []


def add_actor(actor: str, movie: str):
    actors.append({
        "name": actor,
        "movie": movie
    })
def remove_actor(actor: str, movie: str):
    actors.remove({
        "name": actor,
        "movie": movie
    })

def get_actors(movie: str):
    for actor in actors:
        if actor["name"] == movie:
            return actor