# -*- coding: UTF-8 -*-
import datetime
import time


def str_time_stamp(str_time, flag):
    """ 时间格式转为时间戳 """
    if flag == 0:
        return int(time.mktime(time.strptime(str_time, "%Y-%m-%d %H:%M:%S")))
    elif flag == 1:
        return int(time.mktime(time.strptime(str_time, "%Y-%m-%d")))


def system_time():
    """ 获取系统时间 """
    now0 = datetime.datetime.now()
    now = now0.strftime('%Y-%m-%d %H:%M')
    return int(time.mktime(time.strptime(now, "%Y-%m-%d %H:%M")))


if __name__ == "__main__":
    print str_time_stamp('2018-11-16 03:24:57', 0)
