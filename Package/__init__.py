class Package:
    def __init__(self, code, weight, cost_per_gram, description):
        self.code = code
        self.weight = max(weight, 0)  # asegurando que el peso es positivo
        self.cost_per_gram = max(cost_per_gram, 0)  # asegurando que el costo por gramo es positivo
        self.description = description

    def calculate(self):
        return self.weight * self.cost_per_gram



