from mon_premier_projet.module1 import *
from mon_premier_projet.module2 import *
from mon_premier_projet.movies.movie import create_movie, delete_movie, movies, get_movies
from mon_premier_projet.utilitaires.maths import *
from mon_premier_projet.utilitaires.text import *
from mon_premier_projet.utilitaires.convert import *



def main():
    # print(hello_module1())
    # print("5 + 4 =", add(5,4))
    # print("7 * 6 =", multiply(7,6))
    # print("45 - 9 =", subtract(45,9))
    # print(to_upper_case("barbecue"))
    # print(to_lower_case("BANANE"))
    # print("20000 yen en euros :", yen_euros(20000))
    # print("2 euros en dollars :", euros_dollars(2))
    create_movie("Harry Potter")
    create_movie("Mission impossible")
    create_movie("Cars")
    create_movie("Toys Story")
    create_movie("Inception")
    create_movie("Oppenheimer")
    delete_movie("Cars")
    print(get_movies())
    create_movie("mon film²")
    print(get_movies())
    delete_movie("mon film²")
    print(get_movies())

if __name__ == "__main__":
    main()

