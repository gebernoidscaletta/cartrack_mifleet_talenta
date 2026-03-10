from dataclasses import dataclass
from typing import Dict

@dataclass
class GetReimburseData:
    start_request_date: str
    end_request_date: str
    page : int = 1
    limit : int = 100
    
    def toQueryParams(self) -> Dict[str, str]:
        return {
            "start_request_date": self.start_request_date,
            "end_request_date": self.end_request_date,
            "page": str(self.page),
            "limit": str(self.limit)
        }