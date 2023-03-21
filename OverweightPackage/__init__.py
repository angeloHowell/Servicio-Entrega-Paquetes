import Package


class OverweightPackage(Package):
    def __init__(self, code, weight, cost_per_gram, description, overweight_cost_per_gram):
        super().__init__(code, weight, cost_per_gram, description)
        self.overweight_cost_per_gram = overweight_cost_per_gram

    def calculate(self):
        overweight_cost = max(self.weight - 10,
                              0) * self.overweight_cost_per_gram  # calcula el costo adicional por sobrepeso
        return super().calculate() + overweight_cost
