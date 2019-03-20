import requests
import traceback
from beifen import femail

hand={
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,image/wxpic,image/sharpp,image/apng,image/tpg,*/*;q=0.8",
    "accept-encoding":"gzip, deflate",
    "accept-language":"zh-CN,en-US;q=0.8",
    "cookie":"PHPSESSID=5bb93004c236d5727dacc8b387bcb103",
    "user-agent":"Mozilla/5.0 (Linux; Android 5.1; 4G Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044306 Mobile Safari/537.36 MicroMessenger/6.6.7.1320(0x26060734) NetType/WIFI Language/zh_CN"

}


url="https://xiao.vdongchina.com/app/index.php?i=16&c=entry&m=ewei_shopv2&do=mobile&wxref=mp.weixin.qq.com&wxref=mp.weixin.qq.com"
try:
    x = requests.post(url)
    er_text="您访问的功能模块不存在，请重新进入"
    if er_text in x.text:
        femail.email("打开商城报错，报错内容是：%s" % er_text, "html", "")
    else:
        print("测试通过")
except:
    ee=traceback.format_exc()
    femail.email("监控小程序报错：$d" % ee, "html", "")

