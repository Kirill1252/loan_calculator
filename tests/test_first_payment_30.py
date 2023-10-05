from src.calculators.first_payment_30 import FirstPaymentThirtyDays
from pytest import mark


@mark.parametrize('summ, payment, first_payment, result', [
    (3000, 2, 1750, [3000, 1750, 1250.0]),
    (3000, 3, 1750, [3000, 1750, 625.0, 625.0])
])
def test_algorithm_first_payment_3000(summ, payment, first_payment, result):
    pp = FirstPaymentThirtyDays(summ, first_payment, payment)
    assert pp.restructuring_first_payment() == result


@mark.parametrize('summ, payment, first_payment, result', [
    (5000, 2, 2700, [5000, 2700, 2300.0]),
    (5000, 3, 2700, [5000, 2700, 1150.0, 1150.0]),
    (5000, 4, 2702, [5000, 2702, 766.0, 766.0, 766.0])
])
def test_algorithm_first_payment_5000(summ, payment, first_payment, result):
    pp = FirstPaymentThirtyDays(summ, first_payment, payment)
    assert pp.restructuring_first_payment() == result


@mark.parametrize('summ, payment, first_payment, result', [
    (8000, 2, 3200, [8000, 3200, 4800.0]),
    (8000, 3, 3200, [8000, 3200, 2400.0, 2400.0]),
    (8000, 4, 3200, [8000, 3200, 1600.0, 1600.0, 1600.0]),
    (8000, 5, 3200, [8000, 3200, 1200.0, 1200.0, 1200.0, 1200.0]),
    (8000, 6, 3200, [8000, 3200, 960.0, 960.0, 960.0, 960.0, 960.0]),
])
def test_algorithm_first_payment_8000(summ, payment, first_payment, result):
    pp = FirstPaymentThirtyDays(summ, first_payment, payment)
    assert pp.restructuring_first_payment() == result


@mark.parametrize('summ, payment, first_payment, result', [
    (10000, 2, 3500, [10000, 3500, 6500.0]),
    (10000, 3, 3500, [10000, 3500, 3250.0, 3250.0]),
    (11000, 4, 2750, [11000, 2750, 2750.0, 2750.0, 2750.0]),
    (10000, 5, 3500, [10000, 3500, 1625.0, 1625.0, 1625.0, 1625.0]),
    (10000, 6, 3500, [10000, 3500, 1300.0, 1300.0, 1300.0, 1300.0, 1300.0]),
    (10000, 7, 3646, [10000, 3646, 1059.0, 1059.0, 1059.0, 1059.0, 1059.0, 1059.0]),
    (11000, 8, 2754, [11000, 2754, 1178.0, 1178.0, 1178.0, 1178.0, 1178.0, 1178.0, 1178.0]),
])
def test_algorithm_first_payment_11000(summ, payment, first_payment, result):
    pp = FirstPaymentThirtyDays(summ, first_payment, payment)
    assert pp.restructuring_first_payment() == result


@mark.parametrize('summ, payment, first_payment, result', [
    (15000, 2, 7500, [15000, 7500, 7500.0]),
    (15000, 3, 7000, [15000, 7000, 4000.0, 4000.0]),
    (15000, 4, 6000, [15000, 6000, 3000.0, 3000.0, 3000.0]),
    (15000, 5, 5980, [15000, 5980, 2255.0, 2255.0, 2255.0, 2255.0]),
    (15000, 6, 5000, [15000, 5000, 2000.0, 2000.0, 2000.0, 2000.0, 2000.0]),
    (15000, 7, 4740, [15000, 4740, 1710.0, 1710.0, 1710.0, 1710.0, 1710.0, 1710.0]),
    (15000, 8, 4402, [15000, 4402, 1514.0, 1514.0, 1514.0, 1514.0, 1514.0, 1514.0, 1514.0]),
])
def test_algorithm_first_payment_15000(summ, payment, first_payment, result):
    pp = FirstPaymentThirtyDays(summ, first_payment, payment)
    assert pp.restructuring_first_payment() == result


@mark.parametrize('summ, payment, first_payment, result', [
    (20000, 2, 9000, [20000, 9000, 11000.0]),
    (20000, 3, 9000, [20000, 9000, 5500.0, 5500.0]),
    (20000, 4, 8000, [20000, 8000, 4000.0, 4000.0, 4000.0]),
    (20000, 5, 8000, [20000, 8000, 3000.0, 3000.0, 3000.0, 3000.0]),
    (20000, 6, 7000, [20000, 7000, 2600.0, 2600.0, 2600.0, 2600.0, 2600.0]),
    (20000, 7, 5300, [20000, 5300, 2450.0, 2450.0, 2450.0, 2450.0, 2450.0, 2450.0]),
    (20000, 8, 5300, [20000, 5300, 2100.0, 2100.0, 2100.0, 2100.0, 2100.0, 2100.0, 2100.0]),
])
def test_algorithm_first_payment_20000(summ, payment, first_payment, result):
    pp = FirstPaymentThirtyDays(summ, first_payment, payment)
    assert pp.restructuring_first_payment() == result
