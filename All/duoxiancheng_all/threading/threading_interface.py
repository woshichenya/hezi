import time
import threading
import baibaoxiangInterface

go=baibaoxiangInterface.go()
class a(threading.Thread):
    def __init__(self,url, data, header,name):
        threading.Thread.__init__(self)
        self.url=url
        self.data = data
        self.header = header
        self.name = name

    def run(self):
        for i in range(10):
            print(self.name,"本次执行时间是","时间是：",time.time())
            go.post(self.url,self.data,self.header,self.name)


'''
数据块
'''
data1={
    "account":"18871551774",
    "password":"123456"
}

data2={
    "account":"188715517741",
    "password":"123456"
}

'''
方案块
'''
t1=time.time()
k1=a("http://test-plus.moliyan.com.cn/api/index/login",data1,"","登录接口1")
k2=a("http://test-plus.moliyan.com.cn/api/index/login",data2,"","登录接口2")


'''
执行块
'''
k1.start()
k2.start()


'''
附加块
'''
t2=time.time()
t3=float(t2)-float(t1)
print(t3)
