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

#hmac username="kYdPFVLoEp4NW8ct", algorithm="hmac-sha256", headers="date request-line", signature="BiqZvszr12BKOmosy+gdGCAnnF64Wt9O1zQTsJvDJrc="

#TODO : check again for the generation of hmac header, is it correct to use the full url or just the path and query params, and also check for the request line format, is it correct to use HTTP/1.1 or should it be something else
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
    log.info(f"{file}Date: {dateString}")
    return {
        "Authorization": hmacHeader,
        "Date": dateString
    }
# const Header = require('postman-collection').Header;
# const url = require('url');

# const hmac_username = pm.environment.get('hmac_username');
# const hmac_secret = pm.environment.get('hmac_secret');

# console.log("Username:", hmac_username);
# console.log("Secret:", hmac_secret);
# const requestUrl = url.parse(request['url']);
# const requestLine = pm.request.method + ' ' + requestUrl.path + ' HTTP/1.1';
# const dateString = new Date().toUTCString();
# console.log(['date: ' + dateString, requestLine].join('\n'))
# const digest = CryptoJS.HmacSHA256(['date: ' + dateString, requestLine].join('\n'), hmac_secret);


# const signature = CryptoJS.enc.Base64.stringify(digest);
# const hmac_header = 'hmac username="' + hmac_username + '", algorithm="hmac-sha256", headers="date request-line", signature="' + signature + '"'

# pm.request.headers.add(new Header("Authorization: " + hmac_header));
# pm.request.headers.add(new Header("Date: " + dateString));