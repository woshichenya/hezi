import pytesseract
from PIL import Image
import time
#__author__ = 'admin'
im = Image.open('D:\img\\TIM截图20181010103001.png')




print(pytesseract.image_to_string (im))
print("-----------------------------------")
print(pytesseract.image_to_string (im2))
print("-----------------------------------")

print("-----------------------------------")

print("-----------------------------------")
print(pytesseract.image_to_string (im5))

'''封装一个拍照方法
def paizhao(mingcheng):
        a="D:\\img\\"
        b=".png"
        Time=time.strftime("%Y-%m-%d--%H^%M^%S", time.localtime())
        png_name=a+Time+mingcheng+b
        driver.get_screenshot_as_file(png_name)
        return png_name
'''

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.1.1',
    #'platformVersion': '7.0',
    #'deviceName': 'emulator-5554',
    'deviceName': 'freeme-4g-868607020470921',
    #'deviceName': 'mi_5s-66680442',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,
    'appPackage': 'com.tencent.mm',
    'appActivity': 'com.tencent.mm.ui.LauncherUI',
    'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
}


