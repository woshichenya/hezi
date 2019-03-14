# coding: utf-8
import os
import psutil
import time


def write_pid():
    pid = os.getpid()
    fp = open("pid.log", 'w')
    fp.write(str(pid))
    fp.close()
    print(pid)
    print(fp)


def read_pid():
    if os.path.exists("pid.log"):
        fp = open("pid.log", 'r')
        pid = fp.read()
        fp.close()
        print("???",pid)
        return pid
    else:
        return False


def write_log(log_content):
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log_content = time_now + "---->" + log_content + os.linesep
    fp = open('recognition.log', 'a+')
    fp.write(log_content)
    fp.close()


def run():
    pid = read_pid()
    # print pid
    pid = int(pid)
    if pid:
        running_pid = psutil.pids()
        print("",running_pid)
        if pid in running_pid:
            log_content = "process is running..."
            write_log(log_content)
        else:
            write_pid()
            time.sleep(20)
    else:
        write_pid()
        time.sleep(20)


if __name__ == "__main__":
    run()