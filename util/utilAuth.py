import hmac
import hashlib
import base64
from datetime import datetime, timezone
from urllib.parse import urlparse

from constants.constantsGeneral import ConstantsGeneral

def basicAuthGenerator():
    credentials = f"{ConstantsGeneral.getCartrackApiUsername()}:{ConstantsGeneral.getCartrackApiPassword()}"
    encodedCredentials = base64.b64encode(credentials.encode()).decode()
    return encodedCredentials

#hmac username="kYdPFVLoEp4NW8ct", algorithm="hmac-sha256", headers="date request-line", signature="BiqZvszr12BKOmosy+gdGCAnnF64Wt9O1zQTsJvDJrc="

def hmacHeadersGenerator(url: str, method: str, hmac_username: str, hmac_secret: str) -> dict:
    parsedUrl = urlparse(url)
    path = parsedUrl.path
    if parsedUrl.query:
        path += '?' + parsedUrl.query
    requestLine = f"{method} {path} HTTP/1.1"
    dateString = datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')
    signingString = f"date: {dateString}\n{requestLine}"
    digest = hmac.new(
        hmac_secret.encode('utf-8'),
        signingString.encode('utf-8'),
        hashlib.sha256
    ).digest()
    signature = base64.b64encode(digest).decode('utf-8')
    hmacHeader = (
        f'hmac username="{hmac_username}", '
        f'algorithm="hmac-sha256", '
        f'headers="date request-line", '
        f'signature="{signature}"'
    )
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