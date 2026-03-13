from dataclasses import dataclass

@dataclass
class UpdateFuel:
    supplier: str
    description: str
    fuelling_station: str
    fuelling_date: str
    registration: str
    quantity: float
    price: float
    net_value: float
    tax_rate: float
    total_value: float
