import time
def dengdai_shijian(wait_time):
    time.sleep(wait_time)
def shuchu_time():
    t=time.strftime("%Y%m%d%H%M%S", time.localtime())
    return t



a_t=shuchu_time()
print(a_t[10:12])
a_t=int(a_t)
t_t=shuchu_time()
t_t=int(t_t)
print(a_t)
'''
while t_t-a_t<=100:
    t_t=shuchu_time()
    t_t=int(t_t)
    dengdai_shijian(1)
'''
d=int(t_t)-int(a_t)
f=str(d)
f=f[10:12]
print(f)
s=str(d)[12:13]
print("最初时间:",a_t,"最终时间:",t_t,"相差时间:",f,"分",s,"秒")



t=time.strftime("%Y%m%d%H%M%S", time.localtime())
print(t)
print(len(t))
print(t[12:14])
print(t[10:12])
print(t[8:10])
print(t[6:8])

t=time.time()
t=int(t)
print(t)
time.sleep(2)
t=time.time()
t=int(t)
print(t)
