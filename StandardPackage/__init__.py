import Package


class StandardPackage(Package):
    def __init__(self, code, weight, cost_per_gram, description, two_day_delivery_fee):
        super().__init__(code, weight, cost_per_gram, description)
        self.two_day_delivery_fee = two_day_delivery_fee

    def calculate(self):
        return super().calculate() + self.two_day_delivery_fee
