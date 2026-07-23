from accountant import calculate, Charge
from decimal import Decimal

def test_a_simple_case_for_start():
    
    vat_rate = "0.23"
    unit_price = "10"
    quantity = 2
    
    result = calculate(vat_rate, unit_price, quantity)
    
    assert result == Charge(Decimal("20"), Decimal("4.60"), Decimal("24.60"))
    
def test_zero_vat_rate():
    
    vat_rate = "0.00"
    unit_price = "10"
    quantity = 2
    
    result = calculate(vat_rate, unit_price, quantity)
    
    assert result == Charge(Decimal("20"), Decimal("0.00"), Decimal("20"))
    
    
def test_zero_quantity():
    
    vat_rate = "0.23"
    unit_price = "10"
    quantity = 0
    
    result = calculate(vat_rate, unit_price, quantity)
    
    assert result == Charge(Decimal("0.00"), Decimal("0.00"), Decimal("0.00"))
    
    
def test_rounding_half_up():
    
    vat_rate = "0.05"
    unit_price = "66.85"
    quantity = 2
    
    result = calculate(vat_rate, unit_price, quantity)
    
    assert result == Charge(Decimal("133.70"), Decimal("6.69"), Decimal("140.39"))    