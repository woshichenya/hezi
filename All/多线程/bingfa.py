import time
import threading
import requests


# username="18871551001"
# pas="123456abc"

print("一切开始之时：",time.time())

class a(threading.Thread):
    def __init__(self,url, data):
        threading.Thread.__init__(self)
        self.url=url
        self.data = data

    def run(self):
        # t=requests.post(self.url,data=self.data)
        t=requests.get(url)
        print(t)
        # try:
        #     print(t.json())
        # except:
        #     print(t.text)
        # print(t.url)
        # print(self.data)

time_start=time.time()
url="https://xiao.vdongchina.com/app/index.php?i=264&c=entry&eid=122"
# data={
#     "account":"18871551001",
#     "password":"123456abc"
#
# }
data={
    "time":time.time()
}
print(data)
a(url,data).start()


# for s in range (1,1):
#     a(url,data).start()

class b (threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name

    def run(self):
        print("第",self.name,"开始执行500并发之时：",time.time())
        for s in range(1, 500):
            a(url, data).start()
        print("结束第", self.name, "执行500并发之时：", time.time())

print("开始循环之时：",time.time())
for ss in range(5):
    b(ss).start()
print("结束循环之时：",time.time())


time_end=time.time()
print("启动共耗时：",time_end-time_start)