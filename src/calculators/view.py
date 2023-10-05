def view_payments(payments):
    view = f"""
(Ссылка)
Гарантийное письмо (компания).
Общая сумма {payments[0]} грн до (дата последнего платежа)
1. {payments[1]}.грн - (дата) - оплачено.
"""
    count = 2
    for item in payments[2:]:
        payment = f'{count}. {item} грн - (дата)\n'
        view += payment
        count += 1

    return view


def view_first_payment(payments):
    view = f"""
(Ссылка)
Гарантийное письмо (компания).
Первый платеж {payments[1]} грн до (дата)
Общая сумма {payments[0]} грн
"""

    return view
