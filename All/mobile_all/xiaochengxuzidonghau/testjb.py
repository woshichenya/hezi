from appium import webdriver
import time

# QQ群522720170

desired_caps = {}

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.1.1',
    #'deviceName': 'emulator-5554',
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


contexts = driver.contexts
print(contexts)
print(driver.context)

try:
    driver.switch_to.content(contexts[1])
    print(driver.context)
except:
    print("11111111111111")
'''截图======================================================================================================'''

#while iii<5
a="D:\\img\\"
b=".png"
Time=time.strftime("%Y-%m-%d--%H^%M^%S", time.localtime())
driver.get_screenshot_as_file(a+Time+b)

print("角标为：",contexts.index("WEBVIEW_com.tencent.mm"))
try:
    webview=driver.contexts[-1]
    print(webview)
    #driver.switch_to.context(webview)
except:
    print("22222222222222")
#driver.switch_to.default_content
print(driver.context)
driver.find_element_by_id("com.tencent.mm:id/cdh").click()
print("点击成功1")
driver.find_element_by_id("WEBVIEW_com.tencent.mm:id/cdh").click()
print("点击成功2")