from dataclasses import dataclass

@dataclass
class ResponseFuel:
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
    general_ledger_code: int
    discount: float
    registration: str
    vehicle_deleted: bool
    fuel_transaction_type: str
    fuelling_date: str
    fuelling_station: str
    ct_fuel_station: str
    ct_fuel_station_latitude: float
    ct_fuel_station_longitude: float
    ct_latitude: float
    ct_longitude: float
    consumption: float
    fuel_validation_status: str
    ct_odometer: int
    ct_quantity: int
    is_tank_full: bool
    fuel_card: str
    odometer: int
