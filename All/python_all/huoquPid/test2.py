# coding: utf-8
import os
import psutil
import time

def Pid():
    print("gogogogogo")
    pid = os.getpid()
    fp = open("pid.log", 'w')
    fp.write(str(pid))
    fp.close()
    print(pid)

    time.sleep(2)
    return pid


d=time.time()
print(d)


