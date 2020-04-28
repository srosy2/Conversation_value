from Model.Model import Money


class Dollars(Money):
    def __init__(self, name, pay):
        self.currency = 'Dollars'
        super().__init__(name, pay)


class Rubles(Money):
    def __init__(self, name, pay):
        self.currency = 'Rubles'
        super().__init__(name, pay)
