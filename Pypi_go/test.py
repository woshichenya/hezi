import time
import threading
from baibaoxiang import baibaoxiangInterface,excel,sys_powel,xingneng

data={
    "account":"18871551774",
    "password":"123456"
}
url="http://test-plus.moliyan.com.cn/api/index/login"
xingneng.Bingfa_test().bingfa_test_go(url,data,"某个登录接口",2)
# xx=baibaoxiangInterface.go()
# xx.post(url,data,"","xxx")
print(111111111)
excel.InputExcel().end("D:\\linshi\\","并发结果11")