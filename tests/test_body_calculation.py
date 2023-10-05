from src.calculators.body_calculation import BodyCalculation
from pytest import mark


@mark.parametrize('body, result', [
    (1500, {'maximum': 4500, 'minimum': 3000, 'bargain': 2700}),
    (5000, {'maximum': 15000, 'minimum': 10000, 'bargain': 7500}),
    (8000, {'maximum': 24000, 'minimum': 12000, 'bargain': 10800})
])
def test_new_portfolio(body, result):
    calculation_body = BodyCalculation(body)
    assert calculation_body.new_portfolio() == result


@mark.parametrize('body, result', [
    (1500, {'maximum': 4500, 'minimum': 2700, 'bargain': 1725}),
    (5000, {'maximum': 15000, 'minimum': 7500, 'bargain': 5750}),
    (8000, {'maximum': 24000, 'minimum': 10800, 'bargain': 9200})
])
def test_portfolio_after_tp(body, result):
    calculation_body = BodyCalculation(body)
    assert calculation_body.portfolio_after_tp() == result


def test_portfolio_2022():
    calculation_body = BodyCalculation(1500)
    assert calculation_body.portfolio_2022() == {'maximum': 4500, 'minimum': 2025, 'bargain': 1725}


def test_portfolio_up_to_2021():
    calculation_body = BodyCalculation(1500)
    assert calculation_body.portfolio_up_to_2021() == {'maximum': 4500, 'minimum': 1725, 'bargain': 1500}