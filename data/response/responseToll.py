from dataclasses import dataclass

@dataclass
class ResponseToll:
    id: int
    document_number: str
    document_type: str
    document_status: str
    supplier: str
    description: str
    quantity: int
    price: float
    net_value: float
    tax_rate: float
    total_value: float
    driver: str
    registration: str
    ct_toll_station: str
    ct_toll_station_latitude: float
    ct_toll_station_longitude: float
    ct_latitude: float
    ct_longitude: float
    ct_odometer: int
    general_ledger_code: int
    discount: float
    toll_validation_status: str
    toll_date: str
    passage_name: str
