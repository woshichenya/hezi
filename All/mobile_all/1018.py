from appium import webdriver
#from appium.webdriver.common.touch_action import TouchAction
import time
#from selenium import *
import sys

#a=eval(sys.argv[1])  #py文件后带的第一个参数


desired_caps1= {
    'platformName': 'Android',
    'platformVersion': '5.1',
    #'platformVersion': '4.4.2',
   # 'deviceName': '127.0.0.1:62001',
    'deviceName': '10.130.32.88:5555',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,
    'appPackage': 'com.tencent.mm',
    'appActivity': 'com.tencent.mm.ui.LauncherUI',
   # 'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}

}

desired_caps2= {
    'platformName': 'Android',
    'platformVersion': '5.1',
    #'platformVersion': '4.4.2',
   # 'deviceName': '127.0.0.1:62001',
    'deviceName': '10.130.33.172:5555',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,
    'appPackage': 'com.tencent.mm',
    'appActivity': 'com.tencent.mm.ui.LauncherUI',
    #'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}

}
desired_caps3 = {
        'platformName': 'Android',
        'platformVersion': '5.1.1',
         #'platformVersion': '7.0',
         #'deviceName': 'emulator-5554',
        'deviceName': 'freeme-4g-868607020470921',
        # 'deviceName': 'mi_5s-66680442',
        #'unicodeKeyboard': True,
        #'resetKeyboard': True,
        'noReset': True,
        'appPackage': 'com.tencent.mm',
        'appActivity': 'com.tencent.mm.ui.LauncherUI',
        #'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
    }
desired_caps4 = {
        'platformName': 'Android',
        'platformVersion': '5.1.1',
         #'platformVersion': '7.0',
         'deviceName': 'emulator-5554',
        #'deviceName': 'freeme-4g-868607020470921',
        # 'deviceName': 'mi_5s-66680442',
        #'unicodeKeyboard': True,
        #'resetKeyboard': True,
        'noReset': True,
        'appPackage': 'com.tencent.mm',
        'appActivity': 'com.tencent.mm.ui.LauncherUI',
       # 'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
    }
'''
if(a==1):
    desired_caps=desired_caps1
elif(a==2):
    desired_caps=desired_caps2
'''


'''开始启动程序'''
driver = webdriver.Remote('http://127.0.0.1:5555/wd/hub', desired_caps4)
print("启动手机程序打开微信")