from accountant import calculate, Charge, summarize
from decimal import Decimal

def test_two_units_standard_vat():
    
    vat_rate = "0.23"
    unit_price = "10"
    quantity = 2
    
    result = calculate(vat_rate, unit_price, quantity)
    expected = Charge.from_amounts("20", "4.60", "24.60")
    
    assert result == expected
    
    
    
def test_zero_vat_rate():
    
    vat_rate = "0.00"
    unit_price = "10"
    quantity = 2
    
    result = calculate(vat_rate, unit_price, quantity)
    expected = Charge.from_amounts("20", "0.00", "20")
    
    assert result == expected
    
    
def test_zero_quantity():
    
    vat_rate = "0.23"
    unit_price = "10"
    quantity = 0
    
    result = calculate(vat_rate, unit_price, quantity)
    expected = Charge.from_amounts("0.00", "0.00", "0.00")
    
    assert result == expected
    
    
def test_rounding_half_up():
    
    vat_rate = "0.05"
    unit_price = "66.85"
    quantity = 2
    
    result = calculate(vat_rate, unit_price, quantity)
    expected = Charge.from_amounts("133.70", "6.69", "140.39")
    
    assert result == expected  
    
    
    
def test_summarize_two_charges():
    
    charges = [Charge.from_amounts('100', '23', '123'), Charge.from_amounts('200', '46', '246')]
    
    result = summarize(charges)
    expected = Charge.from_amounts('300', '69', '369')
    
    assert  result == expected
    
    
    
def test_summarize_empty_list():
    
    charges = []
    
    result = summarize(charges)
    expected = Charge.from_amounts('0', '0', '0')
    
    assert result == expected