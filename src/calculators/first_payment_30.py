def checking_payments(payments):
    if payments >= 9:
        raise ValueError(f'Вы указали {payments}, количество платежей не может быть больше указанного алгоритма')
    if payments <= 1:
        raise ValueError(f'Вы указали {payments}, количество платежей не может быть меньше двух')
    return payments


class FirstPaymentThirtyDays:
    def __init__(self, summ, first_payment, payment):
        self.summ = summ
        self.payments = checking_payments(payment)
        self.first_payment = first_payment

    def restructuring_first_payment(self):
        summ = "%.2f" % self.summ
        first_payment = "%.2f" % self.first_payment
        payment_schedule = [summ, first_payment]

        if self.summ <= 3001:
            down_payment_percentage = self.first_payment / self.summ
            if down_payment_percentage >= 0.50:
                if self.payments <= 3:
                    payment = (self.summ - self.first_payment) / (self.payments - 1)
                    for i in range(self.payments - 1):
                        payment_schedule.append(payment)
                else:
                    raise TypeError('Количество платежей не соответствует алгоритму')
            else:
                raise ValueError('Сумма первого платежа не соответствует алгоритму')

        elif self.summ >= 3001 and self.summ <= 5000:
            down_payment_percentage = self.first_payment / self.summ
            if down_payment_percentage >= 0.35:
                if self.payments <= 4:
                    payment = (self.summ - self.first_payment) / (self.payments - 1)

                    for i in range(self.payments - 1):
                        payment_schedule.append(payment)
                else:
                    raise TypeError('Количество платежей не соответствует алгоритму')
            else:
                raise ValueError('Сумма первого платежа не соответствует алгоритму')

        elif self.summ >= 5001 and self.summ <= 8001:
            down_payment_percentage = self.first_payment / self.summ
            if down_payment_percentage >= 0.30:
                if self.payments <= 6:
                    payment = (self.summ - self.first_payment) / (self.payments - 1)

                    for i in range(self.payments - 1):
                        payment_schedule.append(payment)
                else:
                    raise TypeError('Количество платежей не соответствует алгоритму')
            else:
                raise ValueError('Сумма первого платежа не соответствует алгоритму')

        elif self.summ >= 8001 and self.summ <= 11001:
            down_payment_percentage = self.first_payment / self.summ
            if down_payment_percentage >= 0.25:
                if self.payments <= 8:
                    payment = (self.summ - self.first_payment) / (self.payments - 1)

                    for i in range(self.payments - 1):
                        payment_schedule.append(payment)
                else:
                    raise TypeError('Количество платежей не соответствует алгоритму')
            else:
                raise ValueError('Сумма первого платежа не соответствует алгоритму')

        elif self.summ >= 11001 and self.summ <= 15001:
            down_payment_percentage = self.first_payment / self.summ
            if down_payment_percentage >= 0.20:
                if self.payments <= 8:
                    payment = (self.summ - self.first_payment) / (self.payments - 1)

                    for i in range(self.payments - 1):
                        payment_schedule.append(payment)
                else:
                    raise TypeError('Количество платежей не соответствует алгоритму')
            else:
                raise ValueError('Сумма первого платежа не соответствует алгоритму')

        elif self.summ >= 15001:
            down_payment_percentage = self.first_payment / self.summ
            if down_payment_percentage >= 0.15:
                if self.payments <= 8:
                    payment = (self.summ - self.first_payment) / (self.payments - 1)

                    for i in range(self.payments - 1):
                        payment_schedule.append(payment)
                else:
                    raise TypeError('Количество платежей не соответствует алгоритму')
            else:
                raise ValueError('Сумма первого платежа не соответствует алгоритму')

        return payment_schedule
