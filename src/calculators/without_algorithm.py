class RestructuringWithoutAlgorithm:
    def __init__(self, summ, first_payment, payments):
        self.summ = summ
        self.first_payment = first_payment
        self.payments = payments

    def restructuring_without_algorithm(self):
        summ = "%.2f" % self.summ
        first_payment = "%.2f" % self.first_payment
        payment_schedule = [summ, first_payment]
        payment = (self.summ - self.first_payment) / (self.payments - 1)

        for i in range(self.payments - 1):
            payment_schedule.append("%.2f" % payment)

        return payment_schedule
#148