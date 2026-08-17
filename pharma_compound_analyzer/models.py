class Compound:
    def __init__(self, name, molecular_weight, logP, solubility):
        self.name = name
        self.molecular_weight = molecular_weight
        self.logP = logP
        self.solubility = solubility

    def to_dict(self):
        return {
            "name": self.name,
            "molecular_weight": self.molecular_weight,
            "logP": self.logP,
            "solubility": self.solubility
        }

    def __str__(self):
        return f"{self.name} | MW: {self.molecular_weight} | LogP: {self.logP} | Solubility: {self.solubility}"

class Compound:
    def __init__(self, name, molecular_weight, logP, solubility):
        self.name = name
        self.molecular_weight = molecular_weight
        self.logP = logP
        self.solubility = solubility

    def to_dict(self):
        return {
            "name": self.name,
            "molecular_weight": self.molecular_weight,
            "logP": self.logP,
            "solubility": self.solubility
        }

    def __str__(self):
        return f"{self.name} | MW: {self.molecular_weight} | LogP: {self.logP} | Solubility: {self.solubility}"
