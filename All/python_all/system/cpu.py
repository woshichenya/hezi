import time
import psutil
# print(time.time())
# print(time.strftime("%Y%m%d%H%M%S", time.localtime()))


# print('CPU Ringing time : %s'%psutil.cpu_times(percpu=True))
# print(psutil.cpu_stats())
# print("cpu个数:\t",psutil.cpu_count())
# print(psutil._cpu_busy_time())
# print(psutil.cpu_times().idle)
# print(psutil.cpu_times().system)
# print(psutil.cpu_times().user)


m_all=psutil.virtual_memory().total/1024/1024
# print("全部内存大小为%sM"%m_all)
# m_new=psutil.virtual_memory().free/1024/1024
# m_new_bl=float(m_new)/float(m_all)
# print("剩余内存大小为%sM，剩余占比为%f"%(m_new,m_new_bl*100),"%")
# m=psutil.virtual_memory().available/1024/1024
m=psutil.virtual_memory().used/1024/1024
# print("已使用内存大小为%sM,已用占比为%s"%(m,m/m_all*100),"%")

m_bl=psutil.virtual_memory().percent
print(" CPU使用率:\t"+str(psutil.cpu_percent(0.1))+"%\t|\t内存使用百分比：",m_bl,"\t",m,"M/",m_all,"M")
# if m + m_new ==m_all:
#     print("内存输出正确")
# print(" CPU使用率:\t"+str(psutil.cpu_percent(0.1))+"%")