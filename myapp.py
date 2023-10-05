from src.qt5.calculator_pp_v3 import Ui_MainWindow

from src.calculators.body_calculation import BodyCalculation
from src.calculators.restructuring_30 import RestructuringThirtyDays
from src.calculators.first_payment_30 import FirstPaymentThirtyDays
from src.calculators.without_algorithm import RestructuringWithoutAlgorithm
from src.search.search_for_counterparties import search_counterparty

from src.calculators.view import view_payments, view_first_payment
from PyQt5 import QtWidgets


def checking_data(summ):
    number = ''
    for item in summ:
        if item == ',':
            item = '.'
        elif item == ' ':
            item = ''
        number += item
    number = float(number)

    return number


def number_to_string_conversions(summ):
    str_summ = '%.2f' % summ

    if len(str_summ) == 7:
        number = str_summ[0] + ' ' + str_summ[1:]
    elif len(str_summ) == 8:
        number = str_summ[0:2] + ' ' + str_summ[2:]
    elif len(str_summ) == 9:
        number = str_summ[0:3] + ' ' + str_summ[3:]
    else:
        number = str_summ

    return number


class MyAppWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyAppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.add_functions()

    def add_functions(self):
        self.ui.pushButton_16.clicked.connect(
            lambda: self.loan_calculation(self.ui.lineEdit_5.text())
        )

        self.ui.pushButton_22.clicked.connect(
            lambda: self.restructuring_30(self.ui.lineEdit_15.text(), self.ui.spinBox_7.text(), self.ui.lineEdit_16.text())
        )

        self.ui.pushButton_24.clicked.connect(
            lambda: self.restructuring_without_algorithm(
                self.ui.lineEdit_19.text(), self.ui.lineEdit_20.text(), self.ui.spinBox_9.text()
            )
        )
        self.ui.pushButton_2.clicked.connect(
            lambda: self.search_counterparty_fun(self.ui.lineEdit_2.text())
        )

    def search_counterparty_fun(self, company):
        search_party = search_counterparty(company)
        self.ui.label_13.setText(search_party['name_crm'])
        self.ui.label_14.setText(search_party['company'])
        self.ui.label_15.setText(search_party['requisites'])

    def restructuring_without_algorithm(self, summ, first_payment, payments):
        letters = '0123456789., '

        if summ == '' or summ == '0':
            self.ui.textBrowser_5.setStyleSheet(
                "color: rgb(255, 11, 3);\n"
                "background-color: rgb(255, 255, 255);\n"
                "font-size: 30px;\n"
                "padding: 10px;\n"
            )
            self.ui.textBrowser_5.setText(f'Введіть домовлену суму кредиту')

        elif len(summ.strip(letters)) != 0:
            self.ui.textBrowser_5.setStyleSheet(
                "color: rgb(255, 11, 3);\n"
                "background-color: rgb(255, 255, 255);\n"
                "font-size: 30px;\n"
                "padding: 10px;\n"
            )
            self.ui.textBrowser_5.setText(f'Некоректне введення суми кредиту')

        elif first_payment == '0' or first_payment == '':
            self.ui.textBrowser_5.setStyleSheet(
                "color: rgb(255, 11, 3);\n"
                "background-color: rgb(255, 255, 255);\n"
                "font-size: 30px;\n"
                "padding: 10px;\n"
            )
            self.ui.textBrowser_5.setText(f'Введіть суму першого платежу')

        elif len(first_payment.strip(letters)) != 0:
            self.ui.textBrowser_5.setStyleSheet(
                "color: rgb(255, 11, 3);\n"
                "background-color: rgb(255, 255, 255);\n"
                "font-size: 30px;\n"
                "padding: 10px;\n"
            )
            self.ui.textBrowser_5.setText(f'Некоректне введення суми першого платежу')

        elif payments == '' or payments == '0':
            self.ui.textBrowser_5.setText(f'Некоректне введення кількість платежів')
            self.ui.textBrowser_5.setStyleSheet(
                "color: rgb(255, 11, 3);\n"
                "background-color: rgb(255, 255, 255);\n"
                "font-size: 30px;\n"
                "padding: 10px;\n"
            )
        elif summ < first_payment:
            self.ui.textBrowser_5.setText(f'Сума першого платежу не може бути більшою за обумовлену суму кредиту')
            self.ui.textBrowser_5.setStyleSheet(
                "color: rgb(255, 11, 3);\n"
                "background-color: rgb(255, 255, 255);\n"
                "font-size: 30px;\n"
                "padding: 10px;\n"
            )
        elif summ == first_payment:
            self.ui.textBrowser_5.setText(f'Ви вказали неправильну суму першого платежу')
            self.ui.textBrowser_5.setStyleSheet(
                "color: rgb(255, 11, 3);\n"
                "background-color: rgb(255, 255, 255);\n"
                "font-size: 30px;\n"
                "padding: 10px;\n"
            )
        else:
            c_summ = checking_data(summ)
            c_first = checking_data(first_payment)

            pp = RestructuringWithoutAlgorithm(float(c_summ), float(c_first), int(payments))
            f_payment = pp.restructuring_without_algorithm()

            self.ui.textBrowser_5.setStyleSheet(
                "background-color: rgb(255, 255, 255);\n"
                "font-size: 15px;\n"
            )

            self.ui.textBrowser_5.setText(
                f'{view_first_payment(f_payment)}\n\n{view_payments(f_payment)}'
            )

    def restructuring_30(self, summ, payment, first_payment):
        letters = '0123456789., '

        if summ == '' or summ == '0':
            self.ui.textBrowser_3.setStyleSheet(
                "color: rgb(255, 11, 3);\n"
                "background-color: rgb(255, 255, 255);\n"
                "font-size: 30px;\n"
                "padding: 10px;\n"
            )
            self.ui.textBrowser_3.setText(f'Введіть домовлену суму кредиту')

        elif len(summ.strip(letters)) != 0:
            self.ui.textBrowser_3.setStyleSheet(
                "color: rgb(255, 11, 3);\n"
                "background-color: rgb(255, 255, 255);\n"
                "font-size: 30px;\n"
                "padding: 10px;\n"
            )
            self.ui.textBrowser_3.setText(f'Некоректне введення суми кредиту')

        elif first_payment == '' or first_payment == '0':
            try:
                c_summ = checking_data(summ)
                pp = RestructuringThirtyDays(c_summ, int(payment))
                f_payment = pp.algorithm_calculation()

                self.ui.textBrowser_3.setStyleSheet(
                    "background-color: rgb(255, 255, 255);\n"
                    "font-size: 15px;\n"
                )

                self.ui.textBrowser_3.setText(
                    f'{view_first_payment(f_payment)}\n\n{view_payments(f_payment)}'
                )
            except TypeError:
                self.ui.textBrowser_3.setStyleSheet(
                    "color: rgb(255, 11, 3);\n"
                    "background-color: rgb(255, 255, 255);\n"
                    "font-size: 30px;\n"
                    "padding: 10px;\n"
                )

                self.ui.textBrowser_3.setText(f'Кількість платежів не відповідає алгоритму')
            except Exception as ex:
                print(ex)

        else:
            try:
                c_summ = checking_data(summ)
                c_first_payment = checking_data(first_payment)
                pp_first = FirstPaymentThirtyDays(float(c_summ), float(c_first_payment), int(payment))
                f_payment = pp_first.restructuring_first_payment()

                self.ui.textBrowser_3.setStyleSheet(
                    "background-color: rgb(255, 255, 255);\n"
                    "font-size: 15px;\n"
                )

                self.ui.textBrowser_3.setText(
                    f'{view_first_payment(f_payment)}\n\n{view_payments(f_payment)}'
                )
            except ValueError:
                self.ui.textBrowser_3.setStyleSheet(
                    "color: rgb(255, 11, 3);\n"
                    "background-color: rgb(255, 255, 255);\n"
                    "font-size: 30px;\n"
                    "padding: 10px;\n"
                )
                self.ui.textBrowser_3.setText(f'Сума першого платежу не відповідає алгоритму')
            except TypeError:
                self.ui.textBrowser_3.setStyleSheet(
                    "color: rgb(255, 11, 3);\n"
                    "background-color: rgb(255, 255, 255);\n"
                    "font-size: 30px;\n"
                    "padding: 10px;\n"
                )
                self.ui.textBrowser_3.setText(f'Кількість платежів не відповідає алгоритму')

    def loan_calculation(self, summ):
        try:
            letters = '0123456789., '

            if len(summ.strip(letters)) != 0:
                self.ui.label_89.setText("Error")
                self.ui.label_93.setText("Error")
                self.ui.label_97.setText("Error")

                self.ui.label_131.setText('Error')
                self.ui.label_135.setText('Error')
                self.ui.label_140.setText('Error')

                self.ui.label_133.setText('Error')
                self.ui.label_137.setText('Error')
                self.ui.label_141.setText('Error')

                self.ui.label_143.setText('Error')
                self.ui.label_145.setText('Error')
                self.ui.label_147.setText('Error')

            else:
                summ = checking_data(summ)
                body_credit = BodyCalculation(float(summ))

                self.ui.label_89.setText(
                    number_to_string_conversions(body_credit.new_portfolio()['maximum'])
                )
                self.ui.label_93.setText(
                    number_to_string_conversions(body_credit.new_portfolio()['minimum'])
                )
                self.ui.label_97.setText(
                    number_to_string_conversions(body_credit.new_portfolio()['bargain'])
                )

                self.ui.label_131.setText(
                    number_to_string_conversions(body_credit.portfolio_after_tp()['maximum'])
                )
                self.ui.label_135.setText(
                    number_to_string_conversions(body_credit.portfolio_after_tp()['minimum'])
                )
                self.ui.label_140.setText(
                    number_to_string_conversions(body_credit.portfolio_after_tp()['bargain'])
                )

                self.ui.label_133.setText(
                    number_to_string_conversions(body_credit.portfolio_2022()['maximum'])
                )
                self.ui.label_137.setText(
                    number_to_string_conversions(body_credit.portfolio_2022()['minimum'])
                )
                self.ui.label_141.setText(
                    number_to_string_conversions(body_credit.portfolio_2022()['bargain'])
                )

                self.ui.label_143.setText(
                    number_to_string_conversions(body_credit.portfolio_up_to_2021()['maximum'])
                )
                self.ui.label_145.setText(
                    number_to_string_conversions(body_credit.portfolio_up_to_2021()['minimum'])
                )
                self.ui.label_147.setText(
                    number_to_string_conversions(body_credit.portfolio_up_to_2021()['bargain'])
                )

        except Exception:
            self.ui.label_89.setText("0")
            self.ui.label_93.setText("0")
            self.ui.label_97.setText("0")

            self.ui.label_131.setText('0')
            self.ui.label_135.setText('0')
            self.ui.label_140.setText('0')

            self.ui.label_133.setText('0')
            self.ui.label_137.setText('0')
            self.ui.label_141.setText('0')

            self.ui.label_143.setText('0')
            self.ui.label_145.setText('0')
            self.ui.label_147.setText('0')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyAppWindow()
    ui.show()
    sys.exit(app.exec_())
