from decimal import Decimal, ROUND_HALF_UP
from dataclasses import dataclass

@dataclass
class Charge:
    net: Decimal
    vat: Decimal
    gross: Decimal
    
    
def calculate(vat_rate:str, unit_price:str, quantity:int) -> Charge:
    net = (Decimal(quantity)*Decimal(unit_price)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    vat = (Decimal(vat_rate)*net).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    gross = net + vat
    return Charge(net, vat, gross)
