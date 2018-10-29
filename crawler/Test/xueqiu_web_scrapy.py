#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json, urllib, sys

s = requests.session()
url = "https://stock.xueqiu.com/v5/stock/quote.json?symbol=" + sys.argv[1] + "&extend=detail"

headers = {
    "Connection": "keep-alive",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": "device_id=6d76e41a68c28003f0aa29dad460f59c; _ga=GA1.2.1951401772.1533108518; s=ez12awvxa4; Hm_lvt_1db88642e346389874251b5a1eded6e3=1539843474; xq_a_token=252d903a9b08cff7eeaf118912e3a89d11a58173; xq_a_token.sig=iJSQemtd0RwEFHtNwWknvzbPxbc; xq_r_token=a3e265710c9cfea653b52b4e1cdae60e6cf53824; xq_r_token.sig=G2IYi9vvKKQRaS28-_scAv8wYJA; u=261540454817199; _gid=GA1.2.2031941817.1540454817; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1540460187; _gat_gtag_UA_16079156_4=1",
    # "Host": "stock.xueqiu.com",
    # "Referer": "https://xueqiu.com/",
    # "Origin": "https://xueqiu.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

requests.packages.urllib3.disable_warnings()
response = requests.get(url, headers=headers, verify=False)
res_dict = json.loads(response.text)
data = res_dict['data']
print(data)

