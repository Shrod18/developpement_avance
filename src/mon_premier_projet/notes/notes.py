notes = {}

def add_note(note : int, movie: str):
    notes[movie] = note

def get_note(movie):
    return movie + " : " + str(notes[movie])

def get_highest_note():
    high_note = 0
    highest_movie = 0
    for movie in notes:
        if notes[movie] >= high_note:
            high_note = notes[movie]
            highest_movie = movie
    return "Meilleure note : " + highest_movie + " " + str(high_note)