def mon_decorateur(func):
    def wrapper(*args, **kwargs):
        print("Avant l'appel de la fonction")
        func(*args, **kwargs)
        print("Après l'appel de la fonction")
    return wrapper

@mon_decorateur
def dire_bonjour():
    print("Bonjour !")

