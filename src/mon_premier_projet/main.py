from mon_premier_projet.module1 import *
from mon_premier_projet.module2 import *
from mon_premier_projet.movies.movie import *
from mon_premier_projet.notes.notes import *
from mon_premier_projet.actors.actor import *
from mon_premier_projet.utilitaires.maths import *
from mon_premier_projet.utilitaires.text import *
from mon_premier_projet.utilitaires.convert import *
from mon_premier_projet.POO.BankAccount import *
from mon_premier_projet.POO.Person import *
from mon_premier_projet.POO.Vehicle import *
from mon_premier_projet.POO.Heritage import *
from mon_premier_projet.POO.Animal import *

def main():
    # print(hello_module1())
    # print("5 + 4 =", add(5,4))
    # print("7 * 6 =", multiply(7,6))
    # print("45 - 9 =", subtract(45,9))
    # print(to_upper_case("barbecue"))
    # print(to_lower_case("BANANE"))
    # print("20000 yen en euros :", yen_euros(20000))
    # print("2 euros en dollars :", euros_dollars(2))

    # add_movie("Harry Potter")
    # add_movie("Mission impossible")
    # add_movie("Cars")
    # add_movie("Toys Story")
    # add_movie("Inception")
    # add_movie("Oppenheimer")
    # print(get_movies())
    # remove_movie("Cars")
    # print(get_movies())

    # add_note(10, "Harry Potter")
    # add_note(14, "Toys Story")
    # add_note(18, "Inception")
    # add_note(15, "Oppenheimer")
    # add_note(14, "Mission impossible")
    # print(get_note("Harry Potter"))
    # print(get_highest_note())

    # add_actor("Harry Potter", "Daniel Radcliffe")
    # add_actor("Mission impossible", "Tom Cruise")
    # print(get_actors())
    # remove_actor("Daniel Radcliffe")
    # print(get_actors())
    # print(get_avg_note())

    account = BankAccount(100)
    account.deposit(50)
    print(account.get_balance())

    p = Person("Alice", 30)
    print(p.name)
    p.age = 35
    print(p.age)

    car = Car()
    car.start()
    car.stop()

    child = Child()
    child.method()

    animals = [Dog("Rex"), Cat("Felix")]
    for animal in animals:
        animal.speak()

if __name__ == "__main__":
    main()

