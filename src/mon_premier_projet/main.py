from mon_premier_projet.module1 import *
from mon_premier_projet.module2 import *
from mon_premier_projet.utilitaires.maths import *
from mon_premier_projet.utilitaires.text import *
from mon_premier_projet.utilitaires.convert import *


def main():
    print(hello_module1())
    print("5 + 4 =", add(5,4))
    print("7 * 6 =", multiply(7,6))
    print("45 - 9 =", subtract(45,9))
    print(to_upper_case("barbecue"))
    print(to_lower_case("BANANE"))
    print("20000 yen en euros :", yen_euros(20000))
    print("2 euros en dollars :", euros_dollars(2))

if __name__ == "__main__":
    main()

