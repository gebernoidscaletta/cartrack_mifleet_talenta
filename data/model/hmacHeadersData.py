from dataclasses import dataclass

@dataclass
class HmacHeadersData:
    url: str
    method: str
    hmac_username: str
    hmac_secret: str
    params: dict | None = None