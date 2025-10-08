class ConvertibleMixin:
    TAUX_EUR_TO_USD = 1.08
    TAUX_EUR_TO_GBP = 0.85

    def en_dollars(self) -> float:
        return self.montant * self.TAUX_EUR_TO_USD

    def en_livres(self) -> float:
        return self.montant * self.TAUX_EUR_TO_GBP

    def convertir(self, devise: str) -> float:
        if devise == 'USD':
            return self.en_dollars()
        elif devise == 'GBP':
            return self.en_livres()
        else:
            raise ValueError('devise must be USD or GBP')