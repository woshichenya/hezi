# -*- coding: UTF-8 -*-

import datetime
import time

def get_date_by_datetime(days=1):
    today=datetime.date.today()
    oneday=datetime.timedelta(days=days)
    someday=today-oneday
    return someday

def now_time_start(hour = 3600):
    """当前时间段的开始XX:00:00"""
    ct = time.time() - hour
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%dT%H:00:00", local_time)
    return data_head

def get_date_by_date(date,days = -1):
    timeArray = time.strptime(date, "%Y-%m-%d")
    timeStamp = int(time.mktime(timeArray) + (days * 86400))
    timeArray = time.localtime(timeStamp)
    return time.strftime("%Y-%m-%d", timeArray)

def now_time_end(hour = 3600):
    """当前时间的结束时间XX:59:59"""
    ct = time.time() - hour
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%dT%H:59:59", local_time)
    return data_head

def get_date_ymd(timeStamp):
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
    return otherStyleTime

def param_day_yesterday(day,days=-1):
    """ 获取参数day（字符串2018-11-06）的前一天时间，days（一个int值）获取参数day的前days天的时间"""
    now0 = datetime.datetime.strptime(day, "%Y-%m-%d") + datetime.timedelta(days)
    now = now0.strftime('%Y-%m-%d')
    return now


def system_time_befor(days=0):
    """ 获取系统时间的前days（一个int值）的时间 """
    now0 = datetime.datetime.now() + datetime.timedelta(days)
    now = now0.strftime('%Y-%m-%d')
    return now


def get_date(timestamp):
    """传入时间戳 返回时间格式 es 时间转换"""
    local_time = time.localtime(int(timestamp) / 1000.0)
    time_stamp = time.strftime("%Y-%m-%dT%H:%M:%S", local_time)
    return time_stamp

def system_time():
    """ 获取系统时间 """
    now0 = datetime.datetime.now()
    now = now0.strftime('%Y-%m-%d %H:%M:%S')
    return now


if __name__ == "__main__":

    print now_time_end()
    print system_time_befor(1)
    print param_day_yesterday("2018-10-22")
    print param_day_yesterday("2018-10-22",days=-2)
    print param_day_yesterday("2018-10-22",days=-3)
    print now_time_start()
    print now_time_end()
