#!/home/autotest/software/Python3.6
# -*- coding: utf-8 -*-
################################################################################################################################
##首先在Linux服务器上，给appium启用多个线程，用命令   appium -p 4777 -U 10.130.33.57:5555   appium -p 4778 -U 10.130.32.161:5555
################################################################################################################################


from appium import webdriver
#from appium.webdriver.common.touch_action import TouchAction
import time
#from selenium import *
import sys

a=eval(sys.argv[1])  #py文件后带的第一个参数


desired_caps1= {
    'platformName': 'Android',
    'platformVersion': '5.1',
    #'platformVersion': '4.4.2',
   # 'deviceName': '127.0.0.1:62001',
    'deviceName': '10.130.32.161:5555',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,
    'appPackage': 'com.tencent.mm',
    'appActivity': 'com.tencent.mm.ui.LauncherUI',
    'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}

}

desired_caps2= {
    'platformName': 'Android',
    'platformVersion': '5.1',
    #'platformVersion': '4.4.2',
   # 'deviceName': '127.0.0.1:62001',
    'deviceName': '10.130.33.57:5555',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,
    'appPackage': 'com.tencent.mm',
    'appActivity': 'com.tencent.mm.ui.LauncherUI',
    'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}

}


if(a==1):
    #driver = webdriver.Remote('http://10.11.41.65:4723/wd/hub', desired_caps1)
    driver = webdriver.Remote('http://127.0.0.1:4778/wd/hub', desired_caps1)
    #driver = webdriver.Remote('http://localhost:<span style="color:#FF0000;">4723</span>/wd/hub',desired_caps1)
    print("启动手机程序打开微信")
    '''开始启动程序'''


elif(a==2):
    #driver = webdriver.Remote('http://10.11.41.65:4723/wd/hub', desired_caps2)
    driver = webdriver.Remote('http://127.0.0.1:4777/wd/hub', desired_caps2)
    #driver = webdriver.Remote('http://localhost:<span style="color:#FF0000;">4724</span>/wd/hub',desired_caps2)
    print("启动手机程序打开微信")
