# coding: utf-8
import psutil
import time
import python_all.huoquPid.test2
def h_a_pid():
    a_pid = python_all.huoquPid.test2.Pid()
    return a_pid
def h_all_pid():
    running_pid = psutil.pids()
    print("",running_pid)
    return running_pid

fg=open('pid.log','r')
print(fg.read())

go=h_a_pid()
do=h_all_pid()

time.sleep(65)
h_all_pid()


