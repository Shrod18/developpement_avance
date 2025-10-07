notes = []

def add_note(note : int ,movie : string, all_movies : []):
    all_movies[movie] = note

def get_highest_note(all_movies : []):
    high_note = allMovies[0]
    highest_movie = all_movies[0]
    for movie in allMovies:
        if all_movies[movie] >= high_note:
            high_note = all_movies[movie]
            highest_movie = movie
    return highest_movie + " " + highest_note