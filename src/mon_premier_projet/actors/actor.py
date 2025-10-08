actors = []

def add_actor(actor: str, movie: str):
    actors.append({
        "name": actor,
        "movie": movie
    })

def remove_actor(actor: str):
    for actor in actors:
        if actor["name"] == actor["name"]:
            actors.remove(actor)
            break

def get_actors():
    return actors