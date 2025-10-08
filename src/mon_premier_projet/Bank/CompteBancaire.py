from mon_premier_projet.Bank.ConvertibleMixin import ConvertibleMixin


class CompteBancaire(ConvertibleMixin):
    def __init__(self, solde_initial: float = 0.0):
        self.montant = solde_initial

    def __str__(self):
        return f"Compte : {self.montant:.2f}"
