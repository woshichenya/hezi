from appium import webdriver
import time

# QQ群522720170

desired_caps = {}

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.1.1',
    'deviceName': 'emulator-5554',
    #'deviceName': 'freeme-4g-868607020470921',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,
    'appPackage': 'com.tencent.mm',
    'appActivity': 'com.tencent.mm.ui.LauncherUI',
    'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
}


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
print("启动手机程序打开微信")
driver.implicitly_wait(5)
print("已经打开微信程序")
driver.implicitly_wait(5)
print("等待五秒")


xxx=1
while xxx==1:
    try:
        driver.find_element_by_id("com.tencent.mm:id/b0w")
        xxx=2
    except:
        print("微信未完全打开，等待中...")

'''封装一个点击操作'''
def Cid(shuxing,mingcheng,chenggong,shibai):
    xxx=1
    i=1
    while xxx==1 and i<=20:
        try:
            driver.find_element_by_id(shuxing)
            print(mingcheng,"存在，执行下一步")
            xxx=2
            i=1
            while xxx==2 and i<=30:
                try:
                    driver.find_element_by_id(shuxing).click()
                    print(chenggong)
                    xxx=3
                except:
                    print(shibai,"执行等待操作，当前等待",i,"秒")
                    i+=1
                    time.sleep(1)
        except:

            print(mingcheng,"不存在，执行等待操作，当前等待",i,"秒")
            i+=1
            time.sleep(1)

contexts = driver.contexts
print(contexts)
print(driver.context)


'''获取频幕分辨率，并进行输出'''
sss=1
ii=1
while sss==1:
    try:
        driver.get_window_size()['width']
        x = driver.get_window_size()['width']
        y=driver.get_window_size()['height']
        print("横坐标最大值",x)
        print("纵坐标最大值",y)
        '''尝试滑动频幕'''
        x1 = x*0.5
        y1 = y*0.25
        y2 = y*0.9
        time.sleep(3)
        print("滑动前")
        driver.swipe(148,146,148,530)
        driver.implicitly_wait(5)
        print("滑动后")
        sss=2
    except:
        print("获取分辨率失败，再来一次，当前第",ii,"次")
        ii+=1
        time.sleep(1)

'''尝试进入小程序'''
time.sleep(5)
Cid("com.tencent.mm:id/gd","飞龙小程序入口","进入飞龙小程序中","Bug--无法进入小程序")
print("点击小程序图标")
time.sleep(20)
# 切换到图书界面后获取所有的环境
i=1
while i<=20:
    print("第",i,"次")
    contexts = driver.contexts
    print(contexts)
    print(driver.context)
    i+=1
time.sleep(10)
