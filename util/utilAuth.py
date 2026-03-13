import hmac
import hashlib
import base64
from datetime import datetime, timezone
from urllib.parse import urlparse, urlencode
from util.utilLogger import Log
from data.model.hmacHeadersData import HmacHeadersData
from constants.constantsGeneral import ConstantsGeneral

log = Log()
file = "utilAuth - "

def basicAuthGenerator():
    credentials = f"{ConstantsGeneral.getCartrackApiUsername()}:{ConstantsGeneral.getCartrackApiPassword()}"
    encodedCredentials = base64.b64encode(credentials.encode()).decode()
    return encodedCredentials

def hmacHeadersGenerator(data: HmacHeadersData) -> dict:
    log.info(f"{file}Generating HMAC Headers")

    parsedUrl = urlparse(data.url)
    path = parsedUrl.path
    if data.params:
        query = urlencode(data.params)
        path = f"{path}?{query}"

    requestLine = f"{data.method} {path} HTTP/1.1"
    dateString = datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')
    signingString = f"date: {dateString}\n{requestLine}"
    log.info(f"{file}signingString : {dateString} {requestLine}")

    digest = hmac.new(
        data.hmac_secret.encode('utf-8'),
        signingString.encode('utf-8'),
        hashlib.sha256
    ).digest()
    signature = base64.b64encode(digest).decode('utf-8')
    log.info(f"{file}Generated HMAC Signature: {signature}")
    hmacHeader = (
        f'hmac username="{data.hmac_username}", '
        f'algorithm="hmac-sha256", '
        f'headers="date request-line", '
        f'signature="{signature}"'
    )
    return {
        "Authorization": hmacHeader,
        "Date": dateString
    }
