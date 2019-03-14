import pytesseract
from PIL import Image
from PIL import ImageGrab
import time
from appium import webdriver
import traceback
import win32gui, win32ui, win32con, win32api


'''封装一个拍照方法'''
def paizhao(mingcheng):
        a="D:\\img\\"
        b=".png"
        Time=time.strftime("%Y-%m-%d--%H^%M^%S", time.localtime())
        png_name=a+Time+mingcheng+b
        driver.get_screenshot_as_file(png_name)
        return png_name


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

try:
    #开始启动程序
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # driver = webdriver.Remote('http://10.11.41.116:4723/wd/hub', desired_caps)

    print("启动手机程序打开微信")
    '''
    driver.implicitly_wait(5)
    print("已经打开微信程序")
    driver.implicitly_wait(5)
    print("等待五秒")
    '''
except Exception as e:
    ee = traceback.format_exc()
    print("e报错开始")
    print(e)
    print("e报错结束")
    print("ee报错开始")
    print(ee)
    print("ee报错结束")

'''
mingcheng="aaa1"
a="D:\\img\\"
b=".png"
Time=time.strftime("%Y-%m-%d--%H^%M^%S", time.localtime())
png_name=a+Time+mingcheng+b
driver.get_screenshot_as_file(png_name)
'''
bbox = (53,994,560,1047)
im = ImageGrab.grab(bbox)

# 参数 保存截图文件的路径
im.save('a.png')







paizhao("打开手机")
'''
def window_capture(filename):
  hwnd = 0 # 窗口的编号，0号表示当前活跃窗口
  # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
  hwndDC = win32gui.GetWindowDC(hwnd)
  # 根据窗口的DC获取mfcDC
  mfcDC = win32ui.CreateDCFromHandle(hwndDC)
  # mfcDC创建可兼容的DC
  saveDC = mfcDC.CreateCompatibleDC()
  # 创建bigmap准备保存图片
  saveBitMap = win32ui.CreateBitmap()
  # 获取监控器信息
  MoniterDev = win32api.EnumDisplayMonitors(None, None)
  w = MoniterDev[0][2][2]
  h = MoniterDev[0][2][3]
  # print w,h　　　#图片大小
  # 为bitmap开辟空间
  saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
  # 高度saveDC，将截图保存到saveBitmap中
  saveDC.SelectObject(saveBitMap)
  # 截取从左上角（0，0）长宽为（w，h）的图片
  saveDC.BitBlt((53,994), (500, 53), mfcDC, (0, 0), win32con.SRCCOPY)
  saveBitMap.SaveBitmapFile(saveDC, filename)
beg = time.time()
for i in range(10):
  window_capture("haha.jpg")

end = time.time()
print(end - beg)
'''