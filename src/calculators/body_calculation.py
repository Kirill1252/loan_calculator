class BodyCalculation:
    def __init__(self, body):
        self.body = body
        self.maximum = 0
        self.minimum = 0
        self.bargain = 0

    def new_portfolio(self):
        if self.body <= 3999:
            self.maximum = self.body * 3
            self.minimum = self.body * 2
            self.bargain = round(self.body * 1.8)

        elif self.body >= 4000 and self.body <= 7999:
            self.maximum = self.body * 3
            self.minimum = self.body * 2
            self.bargain = round(self.body * 1.5)

        elif self.body >= 8000:
            self.maximum = self.body * 3
            self.minimum = round(self.body * 1.5)
            self.bargain = round(self.body * 1.35)

        debt_relief = {
            'maximum': self.maximum,
            'minimum': self.minimum,
            'bargain': self.bargain
        }

        return debt_relief

    def portfolio_after_tp(self):
        if self.body <= 3999:
            self.maximum = self.body * 3
            self.minimum = round(self.body * 1.8, 2)
            self.bargain = round(self.body * 1.15, 2)

        elif self.body >= 4000 and self.body <= 7999:
            self.maximum = self.body * 3
            self.minimum = round(self.body * 1.5, 2)
            self.bargain = round(self.body * 1.15, 2)

        elif self.body >= 8000:
            self.maximum = self.body * 3
            self.minimum = round(self.body * 1.35, 2)
            self.bargain = round(self.body * 1.15, 2)

        debt_relief = {
            'maximum': self.maximum,
            'minimum': self.minimum,
            'bargain': self.bargain
        }

        return debt_relief

    def portfolio_2022(self):
        self.maximum = self.body * 3
        self.minimum = round(self.body * 1.35, 2)
        self.bargain = round(self.body * 1.15, 2)

        debt_relief = {
            'maximum': self.maximum,
            'minimum': self.minimum,
            'bargain': self.bargain
        }

        return debt_relief

    def portfolio_up_to_2021(self):
        self.maximum = self.body * 3
        self.minimum = round(self.body * 1.15, 2)
        self.bargain = self.body

        debt_relief = {
            'maximum': self.maximum,
            'minimum': self.minimum,
            'bargain': self.bargain
        }

        return debt_relief
