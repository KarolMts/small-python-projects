from decimal import Decimal, ROUND_HALF_UP
from dataclasses import dataclass


@dataclass
class Charge:
    
    net: Decimal
    vat: Decimal
    gross: Decimal
    
    def __add__(self, other):
        
        net = self.net + other.net 
        vat = self.vat + other.vat
        gross = self.gross + other.gross
        return Charge(net, vat, gross)
    
    @classmethod
    def from_amounts(cls, net:str, vat:str, gross:str):
        
        return cls(Decimal(net), Decimal(vat), Decimal(gross))
        
    
    
def calculate(vat_rate:str, unit_price:str, quantity:int) -> Charge:
    
    net = (Decimal(quantity)*Decimal(unit_price)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    vat = (Decimal(vat_rate)*net).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    gross = net + vat
    return Charge(net, vat, gross)



def summarize(charges:list[Charge]) -> Charge:
    
    return sum(charges, start=Charge(Decimal("0"), Decimal("0"), Decimal("0")))
