def checking_payments(payments):
    if payments >= 9:
        raise ValueError(f'Вы указали {payments}, количество платежей не может быть больше указанного алгоритма')
    if payments <= 1:
        raise ValueError(f'Вы указали {payments}, количество платежей не может быть меньше двух')
    return payments


class RestructuringThirtyDays:

    def __init__(self, summ, payments):
        self.summ = summ
        self.payments = checking_payments(payments)

    def algorithm_calculation(self):
        summ = "%.2f" % self.summ
        payment_schedule = [summ]

        if self.summ <= 3001:
            if self.payments == 2:
                payment_1 = self.summ * 0.50
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = payment_1
                payment_schedule.append('%.2f' % payment_2)

            elif self.payments == 3:
                payment_1 = self.summ * 0.50
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.25
                payment_schedule.append('%.2f' % payment_2)

                payment_3 = payment_2
                payment_schedule.append('%.2f' % payment_3)

            else:
                raise TypeError('Количество платежей не соответствует алгоритму')

        elif self.summ >= 3001 and self.summ <= 5001:
            if self.payments == 2:
                payment_1 = self.summ * 0.50
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = payment_1
                payment_schedule.append('%.2f' % payment_2)

            elif self.payments == 3:
                payment_1 = self.summ * 0.40
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.30
                payment_schedule.append('%.2f' % payment_2)

                payment_3 = payment_2
                payment_schedule.append('%.2f' % payment_3)

            elif self.payments == 4:
                payment_1 = self.summ * 0.35
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.22
                payment_schedule.append('%.2f' % payment_2)

                payment_3 = payment_2
                payment_schedule.append('%.2f' % payment_3)

                payment_4 = self.summ * 0.21
                payment_schedule.append('%.2f' % payment_4)

            else:
                raise TypeError('Количество платежей не соответствует алгоритму')

        elif self.summ >= 5001 and self.summ <= 8001:
            if self.payments == 2:
                payment_1 = self.summ * 0.50
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = payment_1
                payment_schedule.append('%.2f' % payment_2)

            elif self.payments == 3:

                payment_1 = self.summ * 0.35
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.325
                payment_schedule.append('%.2f' % payment_2)

                payment_3 = payment_2
                payment_schedule.append('%.2f' % payment_3)

            elif self.payments == 4:
                payment_1 = self.summ * 0.30
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.24
                payment_schedule.append('%.2f' % payment_2)

                payment_3 = self.summ * 0.23
                payment_schedule.append('%.2f' % payment_3)

                payment_4 = payment_3
                payment_schedule.append('%.2f' % payment_4)

            elif self.payments == 5:
                payment_1 = self.summ * 0.30
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.175
                payment_schedule.append('%.2f' % payment_2)

                for i in range(3):
                    payment_schedule.append('%.2f' % payment_2)

            elif self.payments == 6:
                payment_1 = self.summ * 0.30
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.14
                payment_schedule.append('%.2f' % payment_2)

                for i in range(4):
                    payment_schedule.append('%.2f' % payment_2)

            else:
                raise TypeError('Количество платежей не соответствует алгоритму')

        elif self.summ >= 8001 and self.summ <= 11001:
            if self.payments == 2:
                payment_1 = self.summ * 0.50
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = payment_1
                payment_schedule.append('%.2f' % payment_2)

            elif self.payments == 3:
                payment_1 = self.summ * 0.36
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.32
                payment_schedule.append('%.2f' % payment_2)

                payment_3 = payment_2
                payment_schedule.append('%.2f' % payment_3)

            elif self.payments == 4:
                payment_1 = self.summ * 0.28
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.24
                payment_schedule.append('%.2f' % payment_2)

                for i in range(2):
                    payment_schedule.append('%.2f' % payment_2)

            elif self.payments == 5:
                payment_1 = self.summ * 0.25
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.1875
                payment_schedule.append('%.2f' % payment_2)

                for i in range(3):
                    payment_schedule.append('%.2f' % payment_2)

            elif self.payments == 6:
                payment_1 = self.summ * 0.25
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.15
                payment_schedule.append('%.2f' % payment_2)

                for i in range(4):
                    payment_schedule.append('%.2f' % payment_2)

            elif self.payments == 7:
                payment_1 = self.summ * 0.25
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.125
                payment_schedule.append('%.2f' % payment_2)

                for i in range(5):
                    payment_schedule.append('%.2f' % payment_2)

            elif self.payments == 8:
                payment_1 = self.summ * 0.25
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.11
                payment_schedule.append('%.2f' % payment_2)

                for i in range(4):
                    payment_schedule.append('%.2f' % payment_2)

                payment_7 = self.summ * 0.10
                payment_schedule.append('%.2f' % payment_7)

                payment_8 = payment_7
                payment_schedule.append('%.2f' % payment_8)

            else:
                raise TypeError('Количество платежей не соответствует алгоритму')

        elif self.summ >= 11001 and self.summ <= 15001:
            if self.payments == 2:
                payment_1 = self.summ * 0.50
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = payment_1
                payment_schedule.append('%.2f' % payment_2)

            elif self.payments == 3:
                payment_1 = self.summ * 0.36
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.32
                payment_schedule.append('%.2f' % payment_2)

                payment_3 = payment_2
                payment_schedule.append('%.2f' % payment_3)

            elif self.payments == 4:
                payment_1 = self.summ * 0.28
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.24
                payment_schedule.append('%.2f' % payment_2)

                for i in range(2):
                    payment_schedule.append('%.2f' % payment_2)

            elif self.payments == 5:
                payment_1 = self.summ * 0.28
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.18
                payment_schedule.append('%.2f' % payment_2)

                for i in range(3):
                    payment_schedule.append('%.2f' % payment_2)

            elif self.payments == 6:
                payment_1 = self.summ * 0.20
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.16
                payment_schedule.append('%.2f' % payment_2)

                for i in range(4):
                    payment_schedule.append('%.2f' % payment_2)

            elif self.payments == 7:
                payment_1 = self.summ * 0.20
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.14
                payment_schedule.append('%.2f' % payment_2)

                payment_3 = payment_2
                payment_schedule.append('%.2f' % payment_3)

                payment_4 = self.summ * 0.13
                payment_schedule.append('%.2f' % payment_4)

                for i in range(3):
                    payment_schedule.append('%.2f' % payment_4)

            elif self.payments == 8:
                payment_1 = self.summ * 0.20
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.12
                payment_schedule.append('%.2f' % payment_2)

                for i in range(2):
                    payment_schedule.append('%.2f' % payment_2)

                payment_5 = self.summ * 0.11
                payment_schedule.append('%.2f' % payment_5)

                for i in range(3):
                    payment_schedule.append('%.2f' % payment_5)

            else:
                raise TypeError('Количество платежей не соответствует алгоритму')

        elif self.summ >= 15001:
            if self.payments == 2:
                payment_1 = self.summ * 0.50
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = payment_1
                payment_schedule.append('%.2f' % payment_2)

            elif self.payments == 3:
                payment_1 = self.summ * 0.36
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.32
                payment_schedule.append('%.2f' % payment_2)

                payment_3 = payment_2
                payment_schedule.append('%.2f' % payment_3)

            elif self.payments == 4:
                payment_1 = self.summ * 0.28
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.24
                payment_schedule.append('%.2f' % payment_2)

                for i in range(2):
                    payment_schedule.append('%.2f' % payment_2)

            elif self.payments == 5:
                payment_1 = self.summ * 0.28
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.18
                payment_schedule.append('%.2f' % payment_2)

                for i in range(3):
                    payment_schedule.append('%.2f' % payment_2)

            elif self.payments == 6:
                payment_1 = self.summ * 0.20
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.16
                payment_schedule.append('%.2f' % payment_2)

                for i in range(4):
                    payment_schedule.append('%.2f' % payment_2)

            elif self.payments == 7:
                payment_1 = self.summ * 0.16
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.14
                payment_schedule.append('%.2f' % payment_2)

                for i in range(5):
                    payment_schedule.append('%.2f' % payment_2)

            elif self.payments == 8:
                payment_1 = self.summ * 0.15
                payment_schedule.append('%.2f' % payment_1)

                payment_2 = self.summ * 0.13
                payment_schedule.append('%.2f' % payment_2)

                payment_3 = self.summ * 0.12
                payment_schedule.append('%.2f' % payment_3)

                for i in range(5):
                    payment_schedule.append('%.2f' % payment_3)

            else:
                raise TypeError('Количество платежей не соответствует алгоритму')

        return payment_schedule

