notes = []

def add_note(note : int ,movie : string):
    notes[movie] = note

def get_highest_note():
    high_note = notes[0]
    highest_movie = notes[0]
    for movie in notes:
        if notes[movie] >= high_note:
            high_note = notes[movie]
            highest_movie = movie
    return highest_movie + " " + highest_note