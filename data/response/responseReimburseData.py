from dataclasses import dataclass

@dataclass
class ResponseReimburseData:
    id: int
    transaction_id: int
    user_id: int
    employee_id: str
    employee_name: str
    reimbursement_id: int
    reimbursement_name: str
    request_date: str
    approved_date: str
    status: str
    request_amount: float
    paid_amount: float
    description: str
    created_at: str
    