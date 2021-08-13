#!/usr/bin/env python3
 
#
# API doc: https://portals.aliexpress.com/help.htm?page=help_center_api
#
# Python wrapper: https://github.com/kronas/python-aliexpress-api-client
# (There are some mistakes in example on GitHub)
#
 
#----------------------------------------------------------------------
# using standard modules: urllib, json
#----------------------------------------------------------------------
 
import urllib.request, urllib.parse
import json
 
API_KEY = '<api-key>'
AFFILIANTE_ID = '<affiliate_id>'
 
url = 'https://gw.api.alibaba.com/openapi/param2/2/portals.open/api.listPromotionProduct/' + API_KEY
 
payload = {
    'fields': ','.join(['productId', 'productTitle', 'salePrice']),
    'keywords': 'chess',
    'highQualityItems': 'yes',
}
 
response = urllib.request.urlopen(url + '?' + urllib.parse.urlencode(payload))
data = json.loads(response.read())
#print(data)
result = data['result']
#print(result)
products = result['products']
 
for product in products:
    print('#%s %s: %s' % (product['productId'], product['productTitle'], product['salePrice']))
 
#----------------------------------------------------------------------
# using external module: requests
# $ pip install requests
#----------------------------------------------------------------------
 
import requests
 
API_KEY = '<api-key>'
AFFILIANTE_ID = '<affiliate_id>'
 
url = 'https://gw.api.alibaba.com/openapi/param2/2/portals.open/api.listPromotionProduct/' + API_KEY
 
payload = {
    'fields': ','.join(['productId', 'productTitle', 'salePrice']),
    'keywords': 'chess',
    'highQualityItems': 'yes',
}
 
response = requests.get(url, params=payload)
#print(response.request.url)
data = response.json()
#print(data)
result = data['result']
#print(result)
products = result['products']
 
for product in products:
    print('#%s %s: %s' % (product['productId'], product['productTitle'], product['salePrice']))
 
# ---------------------------------------------------------------------
# using external module: aliexpress_api_client
# $ pip install aliexpress_api_client
# or
# $ git clone https://github.com/kronas/python-aliexpress-api-client
# ---------------------------------------------------------------------
# There are some mistakes in example on GitHub
# ---------------------------------------------------------------------
 
from aliexpress_api_client import AliExpress
 
API_KEY = '<api-key>'
AFFILIANTE_ID = '<affiliate_id>'
 
aliexpress = AliExpress(API_KEY, AFFILIANTE_ID)
 
fields = ['productId', 'productTitle', 'salePrice']
keywords = 'chess'
 
result = aliexpress.get_product_list(fields, keywords)
#print(result)
products = result['products']
 
for product in products:
    print('#%s %s: %s' % (product['productId'], product['productTitle'], product['salePrice']))
