import os
import time

def biaoji_time():
    t=time.strftime("%Y%m%d%H%M%S", time.localtime())
    ft=open('D:\\text.txt','w')
    ft.write(str(t))
    ft.close()


biaoji_time()
ft=open('D:\\text.txt')
s=ft.read()
s=int(s)
print(s)
t = time.strftime("%Y%m%d%H%M%S", time.localtime())
t=int(t)
if s-1>t:
    print(1111)
if s-1==t-1:
    print(22222)