import urllib.request
import requests
import urllib
import json
url="https://test-plus.vdongchina.com/app/ewei_shopv2_api.php?i=1001&r=creditshop.log.getlist&timestamp=1539266067120"

r = requests.get(url)
kk = json.loads(r.text)
print(kk)
print(kk[1])
cc=kk['logno']
print(cc)
#jine_float = float(kk['logno'])
#print("金额是：", jine_float, "元")