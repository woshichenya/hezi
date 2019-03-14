import os
import time

def biaoji_time():
    t=time.time()
    t=int(t)
    ft=open('D:\\text.txt','w')
    ft.write(str(t))
    ft.close()


biaoji_time()

#cmd="G:\WDSeleniumObject\All\WeChat_applet\\40_china.py"
cmd="python G:\WDSeleniumObject\All\WeChat_applet\\plus_test_new.py"
#cmd="python G:\WDSeleniumObject\All\WeChat_applet\\test111.py"
p=os.popen(cmd)



k=1
while k==1:
    try:
        t=time.time()
        t=int(t)
        ft = open('D:\\text.txt')
        s = ft.read()
        s = int(s)
        print(s)
        t = int(t)
        nn=200
        if t - s < nn:
            print("当前时间为：",t,"记录时间为：",s,"时间差距为",t-s,"不执行脚本")
        if t-s>=nn:
            biaoji_time()
            print("当前时间为：", t, "记录时间为：", s, "时间差距为", t - s, "准备执行脚本")
            time.sleep(60)
            print("当前时间为：", t, "记录时间为：", s, "时间差距为", t - s, "开始执行脚本")
            p=os.popen(cmd)
    except Exception as e:
        print("报错信息：")
        print(e)
        print("报错结束")

    time.sleep(10)


