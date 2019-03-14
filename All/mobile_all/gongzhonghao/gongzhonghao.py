from appium import webdriver
import time

# QQ群522720170

desired_caps = {}

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.1.1',
   # 'deviceName': 'emulator-5554',

    'deviceName': 'freeme-4g-868607020470921',
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
print("已经打开微信程序,等待五秒")
driver.implicitly_wait(5)
print("等待五秒")



'''封装一个点击操作'''
def Cid(shuxing,mingcheng,chenggong,shibai):
    xxx=1
    i=1
    while xxx==1 and i<=5:
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


Cid("com.tencent.mm:id/as6","产品研发中心9公众号","进入公众号中","Bug--无法进入公众号")
Cid("com.tencent.mm:id/acn","微动商城下拉框","展开二级菜单","Bug--无法展开菜单")
driver.find_element_by_class_name("android.widget.TextView").click()

time.sleep(10)