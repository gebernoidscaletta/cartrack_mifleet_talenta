from dataclasses import dataclass

@dataclass
class UpdateToll:
    supplier: str
    description: str
    quantity: int
    price: float
    net_value: float
    tax_rate: float
    toll_date: str
    passage_name: str
    registration: str
