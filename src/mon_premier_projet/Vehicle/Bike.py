from mon_premier_projet.Vehicle.Vehicle import Vehicle

class Bike(Vehicle):
    def start(self):
        print('Démarrage du moteur...')

    def stop(self):
        print('Freinage...')

    def drive(self):
        return "Rouler à vélo"
