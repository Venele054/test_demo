import urllib3

#
urllib3.disable_warnings()
import os
import hashlib
import hmac
import json
import random
from time import time
import uuid
from urllib.parse import urlparse, quote

import requests
import json


# url = "https://mp-prod.smartmidea.net/mas/v5/app/proxy?alias=/dcp-web/api-product/message/getProdMessageForMJ"
#
# payload = json.dumps({
#   "tm": 1620629727,
#   "version": "5.0",
#   "code": "CLGG13E",
#   "plugin_version": "7.5.0.1_202104201925",
#   "codeType": "70",
#   "sourceSys": "APP"
# })
# headers = {
#   'Content-Type': 'application/json',
#   'Content-Length': '124',
#   'Cookie': 'acw_tc=707c9f9a16206296770744524e2fd6e67b6c4bab6e3b40a50f531504e84f2c',
#   'accessToken': 'T15rf9zersow5cvl7',
#   'random': '2021051014552730592',
#   'secretVersion': '1',
#   'sign': 'c8c234597fa3fa10ecf16e44d45f35fd950f7ed8941f31f1a71f2cae6d49128a',
#   'Host': 'mp-prod.smartmidea.net:443'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload.replace(' ', ''))
#
# print(response.headers)
# print(response.text)


def hmacsha256_get_sign(sign_str):
    hmacsha256_key = 'PROD_VnoClJI9aikS8dyy'
    message = sign_str.encode('utf-8')
    sign = hmac.new(hmacsha256_key.encode('utf-8'), message, digestmod=hashlib.sha256).hexdigest()
    return sign


pro_secret = "prod_secret123@muc"
random_str = str(random.random())

url = "https://mp-prod.smartmidea.net/mas/v5/app/proxy?alias=/dcp-web/api-product/message/getProdMessageForMJ"

payload = json.dumps({
    "tm": str(int(time() // 60 * 60)),
    "version": "5.0",
    "code": "CLGG13E",
    "reqId": str(uuid.uuid4()),
    "codeType": "70",
    "sourceSys": "APP"
})

sign_str = pro_secret + payload + random_str
sign = hmacsha256_get_sign(sign_str)
headers = {
    'Content-Type': 'application/json',
    'Cookie': 'acw_tc=707c9f9a16206296770744524e2fd6e67b6c4bab6e3b40a50f531504e84f2c',
    'accessToken': 'T15rf9zersow5cvl7',
    'random': random_str,
    'secretVersion': '1',
    'sign': sign,
    'Host': 'mp-prod.smartmidea.net:443',
    'Connection': 'close'
}

# response = requests.request("POST", url, headers=headers, data=payload.replace(' ', ''))
response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.request.headers)
print(response.request.body)
print(response.text)
