#https://api.mekari.com/v2/talenta/v3/reimbursement?page=1&limit=1000&start_request_date=2026-03-10&end_request_date=2026-03-10

from urllib.parse import urlencode

import requests
from constants.constantsGeneral import ConstantsGeneral
from constants.constantsEndpoint import ConstantsEndpoint
from data.model.hmacHeadersData import HmacHeadersData
from util import utilAuth
from util.utilLogger import Log

log = Log()

fullUrl = f"{ConstantsGeneral.getTalentaProductionBaseUrl()}{ConstantsEndpoint.getTalentaReimbursementV3()}"
log.info(fullUrl)

hmacData = HmacHeadersData(
    url=fullUrl,
    method="GET",
    hmac_username="",
    hmac_secret="",
    params={
        "page": 1,
        "limit": 1000,
        "start_request_date": "2026-03-09",
        "end_request_date": "2026-03-09"
    }
)
try:
    response = requests.get(fullUrl,
                            params=hmacData.params,
                            headers=utilAuth.hmacHeadersGenerator(hmacData),
                            )
    log.info(f"Response Status Code : {response.status_code}")
    log.info(f"Response Body : {response.json()}")
except Exception as e:
    log.error(f"Error Processing : {e}")
    raise e
