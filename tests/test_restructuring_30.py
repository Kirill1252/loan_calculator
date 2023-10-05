from src.calculators.restructuring_30 import RestructuringThirtyDays
from pytest import mark


@mark.parametrize('summ, payment, result', [
    (2750, 2, ['2750', '1375.00', '1375.00']),
    (2180, 3, ['2180', '1090.00', '545.00', '545.00'])
])
def test_algorithm_calculation_3000(summ, payment, result):
    pp = RestructuringThirtyDays(summ, payment)
    assert pp.algorithm_calculation() == result


@mark.parametrize('summ, payment, result', [
    (4837, 2, ['4837', '2418.50', '2418.50']),
    (4837, 3, ['4837', '1934.80', '1451.10', '1451.10']),
    (4650, 4, ['4650', '1627.50', '1023.00', '1023.00',  '976.50'])
])
def test_algorithm_calculation_5000(summ, payment, result):
    pp = RestructuringThirtyDays(summ, payment)
    assert pp.algorithm_calculation() == result


@mark.parametrize('summ, payment, result', [
    (7750, 2, ['7750', '3875.00', '3875.00']),
    (7750, 3, ['7750', '2712.50', '2518.75', '2518.75']),
    (7750, 4, ['7750', '2325.00', '1860.00', '1782.50',  '1782.50']),
    (7750, 5, ['7750', '2325.00', '1356.25', '1356.25',  '1356.25', '1356.25']),
    (7750, 6, ['7750', '2325.00', '1085.00', '1085.00',  '1085.00', '1085.00', '1085.00'])
])
def test_algorithm_calculation_8000(summ, payment, result):
    pp = RestructuringThirtyDays(summ, payment)
    assert pp.algorithm_calculation() == result


@mark.parametrize('summ, payment, result', [
    (7750, 2, ['7750', '3875.00', '3875.00']),
    (7750, 3, ['7750', '2712.50', '2518.75', '2518.75']),
    (7750, 4, ['7750', '2325.00', '1860.00', '1782.50',  '1782.50']),
    (7750, 5, ['7750', '2325.00', '1356.25', '1356.25',  '1356.25', '1356.25']),
    (7750, 6, ['7750', '2325.00', '1085.00', '1085.00',  '1085.00', '1085.00', '1085.00'])
])
def test_algorithm_calculation_8000(summ, payment, result):
    pp = RestructuringThirtyDays(summ, payment)
    assert pp.algorithm_calculation() == result


@mark.parametrize('summ, payment, result', [
    (9780, 2, ['9780', '4890.00', '4890.00']),
    (9780, 3, ['9780', '3520.80', '3129.60', '3129.60']),
    (9780, 4, ['9780', '2738.40', '2347.20', '2347.20',  '2347.20']),
    (9780, 5, ['9780', '2445.00', '1833.75', '1833.75',  '1833.75', '1833.75']),
    (9780, 6, ['9780', '2445.00', '1467.00', '1467.00',  '1467.00', '1467.00', '1467.00']),
    (9780, 7, ['9780', '2445.00', '1222.50', '1222.50',  '1222.50', '1222.50', '1222.50', '1222.50']),
    (9780, 8, ['9780', '2445.00', '1075.80', '1075.80',  '1075.80', '1075.80', '1075.80', '978.00', '978.00'])
])
def test_algorithm_calculation_11000(summ, payment, result):
    pp = RestructuringThirtyDays(summ, payment)
    assert pp.algorithm_calculation() == result


@mark.parametrize('summ, payment, result', [
    (14999, 2, ['14999', '7499.50', '7499.50']),
    (14999, 3, ['14999', '5399.64', '4799.68', '4799.68']),
    (14999, 4, ['14999', '4199.72', '3599.76', '3599.76',  '3599.76']),
    (14999, 5, ['14999', '4199.72', '2699.82', '2699.82',  '2699.82', '2699.82']),
    (14999, 6, ['14999', '2999.80', '2399.84', '2399.84',  '2399.84', '2399.84', '2399.84']),
    (14999, 7, ['14999', '2999.80', '2099.86', '2099.86',  '1949.87', '1949.87', '1949.87', '1949.87']),
    (14999, 8, ['14999', '2999.80', '1799.88', '1799.88',  '1799.88', '1649.89', '1649.89', '1649.89', '1649.89'])
])
def test_algorithm_calculation_11000(summ, payment, result):
    pp = RestructuringThirtyDays(summ, payment)
    assert pp.algorithm_calculation() == result


@mark.parametrize('summ, payment, result', [
    (22300, 2, ['22300', '11150.00', '11150.00']),
    (22300, 3, ['22300', '8028.00', '7136.00', '7136.00']),
    (22300, 4, ['22300', '6244.00', '5352.00', '5352.00',  '5352.00']),
    (22300, 5, ['22300', '6244.00', '4014.00', '4014.00',  '4014.00', '4014.00']),
    (22300, 6, ['22300', '4460.00', '3568.00', '3568.00',  '3568.00', '3568.00', '3568.00']),
    (22300, 7, ['22300', '3568.00', '3122.00', '3122.00',  '3122.00', '3122.00', '3122.00', '3122.00']),
    (22300, 8, ['22300', '3345.00', '2899.00', '2676.00',  '2676.00', '2676.00', '2676.00', '2676.00', '2676.00'])
])
def test_algorithm_calculation_15000(summ, payment, result):
    pp = RestructuringThirtyDays(summ, payment)
    assert pp.algorithm_calculation() == result
