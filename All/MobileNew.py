from appium import webdriver
import time
from beifen import femail
import traceback
import requests
import json
from PIL import Image
import pytesseract



class MGO():
    print(111111)
    #1111111111111111111
    '''定义会员折扣信息'''
    print("dingyiihuiyuanxinxi")
    huiyuan_zehou = {
        "普通会员": 1,
        "钻石会员": 0.77,
        "白银会员": 1,
        "黄金会员": 1
    }

    '''封装wechat方法'''
    desired_caps = {}

    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '5.1.1',
        # 'platformVersion': '7.0',
        # 'deviceName': 'emulator-5554',
        'deviceName': 'freeme-4g-868607020470921',
        # 'deviceName': 'mi_5s-66680442',
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'noReset': True,
        'appPackage': 'com.tencent.mm',
        'appActivity': 'com.tencent.mm.ui.LauncherUI',
        'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
    }

    '''邮件方法'''
    email = femail.email

    '''开始启动程序'''
    i=1
    go=1
    while go==1 and i<30:
        try:
            driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
            print("启动手机程序打开微信")
            driver.implicitly_wait(5)
            print("已经打开微信程序")
            driver.implicitly_wait(5)
            print("等待五秒")
            go=2
        except Exception as e:
            ee = traceback.format_exc()
            print("开始打印错误日志")
            print(ee)
            print("结束打印错误日志")
            i+=1

    '''启动微信'''
    def On(self):
        i = 1
        go = 1
        while go == 1 and i < 30:
            try:
                driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', MGO.desired_caps)
                print("启动手机程序打开微信")
                driver.implicitly_wait(5)
                print("已经打开微信程序")
                driver.implicitly_wait(5)
                print("等待五秒")
                go = 2
            except Exception as e:
                ee = traceback.format_exc()
                print("开始打印错误日志")
                print(ee)
                print("结束打印错误日志")
                i += 1

    '''封装一个在商品详情页面获取商品价格的方法'''
    def get_shoping_img_jiage(self,png_names,box):
        try:
            self.png_names=png_names
            self.box=box
            image = Image.open(self.png_names)
            newImage = image.crop(self.box)
            newImage.save('a.png')
            im = Image.open('a.png')
            print(pytesseract.image_to_string(im))
            jiage = pytesseract.image_to_string(im)
            jiage = float(jiage)
            print("商品价格", jiage, "元")
            return jiage
        except Exception as e:
            ee=traceback.format_exc()
            MGO.email("从图片获取商品价格报错！！报错信息如下<br>%s"%ee,"html",self.png_names)


    '''判断微信是否正常打开了'''
    def panduan_dakai_wechat(self):
        print(222222)
        xxx = 1
        i=1
        while xxx == 1 and i<30:
            try:
                MGO.driver.find_element_by_id("com.tencent.mm:id/b0w")
                # driver.find_element_by_id("com.tencent.mm:id/chn")
                print("微信开始运行")
                xxx = 2
                return 1
            except:
                print("微信未完全打开，等待中...")
                i+=1
                time.sleep(1)



    '''封装一个截取手机屏幕的方法'''
    def paizhao(self,mingcheng):
        self.mingcheng=mingcheng
        try:
            a = "D:\\img\\"
            b = ".png"
            Time = time.strftime("%Y-%m-%d--%H^%M^%S", time.localtime())
            png_name = a + Time + self.mingcheng + b
            MGO.driver.get_screenshot_as_file(png_name)
            return png_name
        except Exception as e:
            ee=traceback.format_exc()
            print("开始打印错误日志")
            print(ee)
            print("结束打印错误日志")
            return 1

    '''封装一个获取会员积分的方法'''
    def vip_jifen(self,url):
        self.url=url
        try:
            r = requests.get(self.url)
            kk = json.loads(r.text)
            jifen_float = float(kk['credit1'])
            print("积分是：", jifen_float)
            return jifen_float
        except Exception as e:
            ee = traceback.format_exc()
            print("开始打印错误日志")
            print(ee)
            print("结束打印错误日志")
            return 1

    '''封装一个获取会员金额的方法'''
    def vip_jine(self,url):
        self.url = url
        try:
            r = requests.get(self.url)
            kk = json.loads(r.text)
            jine_float = float(kk['credit2'])
            print("金额是：", jine_float, "元")
            return jine_float
        except Exception as e:
            ee=traceback.format_exc()
            print("开始打印错误日志")
            print(ee)
            print("结束打印错误日志")
            return 1

    '''封装一个获取会员折扣的方法'''
    def vip_lv_zekou(self,url):
        self.url = url
        try:
            r = requests.get(self.url)
            kk = json.loads(r.text)
            vip_lv = kk['levelname']
            print("等级是：", vip_lv)
            vip_zekou = MGO.huiyuan_zehou[vip_lv]
            vip_zekou=float(vip_zekou)
            print("会员折扣为：", vip_zekou, "折")
            return vip_zekou
        except Exception as e:
            ee=traceback.format_exc()
            print("开始打印错误日志")
            print(ee)
            print("结束打印错误日志")
            return 1



    '''封装一个输出标题的方法'''
    def inputbt(self,dbiaoti, em_neirong_text, shifouquan, geshi_plain_or_html_s, pen_all_name):
        gogo = 2
        ii = 1
        while gogo == 2 and ii <= 30:
            try:
                if dbiaoti != "微信":
                    bt = MGO.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
                elif dbiaoti == "微信":
                    bt = MGO.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='android:id/text1']").text
                gogo = 1
            except Exception as e:
                print("标题获取中。。。")
                time.sleep(1)
        if shifouquan == 1:
            if bt != dbiaoti:
                MGO.email(em_neirong_text, geshi_plain_or_html_s, pen_all_name)
                print("标题不完全一样，已发送邮件")
            else:
                print("标题是：", bt, "标题验证通过")
        if shifouquan == 0:
            if dbiaoti not in bt:
                MGO.email(em_neirong_text, geshi_plain_or_html_s, pen_all_name)
                print("标题不包含判断值,已发送邮件")
            else:
                print("标题是：", bt, "标题验证通过")
        if shifouquan == 3:
            if dbiaoti not in bt:
                print("未转跳页面，标题不一致")
        return bt

    '''保存运行时间'''
    def biaoji_time(self):
        t = time.time()
        t = int(t)
        ft = open('D:\\text.txt', 'w')
        ft.write(str(t))
        ft.close()

    '''封装一个mobile_id点击操作'''
    def Cid(self,shuxing, mingcheng, chenggong, shibai):
        xxx = 1
        i = 1
        while xxx == 1 and i <= 30:
            try:
                MGO.driver.find_element_by_id(shuxing)
                print(mingcheng, "存在，执行下一步")
                xxx = 2
                i = 1
                while xxx == 2 and i <= 30:
                    try:
                        i = 1
                        MGO.driver.find_element_by_id(shuxing).click()
                        print(chenggong)
                        xxx = 3
                    except:
                        print(shibai, "执行等待操作，当前执行", i, "次")
                        i += 1
            except:
                print(mingcheng, "不存在，执行等待操作，当前等待", i, "秒")
                i += 1
                time.sleep(1)

    '''封装一个mobile_xpath点击操作'''
    def Cxpath(self,shuxing, mingcheng, chenggong, shibai):
        xxx = 1
        i = 1
        while xxx == 1 and i <= 30:
            try:
                MGO.driver.find_element_by_xpath(shuxing)
                print(mingcheng, "存在，执行下一步")
                xxx = 2
                i = 1
                while xxx == 2 and i <= 30:
                    try:
                        MGO.driver.find_element_by_xpath(shuxing).click()
                        print(chenggong)
                        xxx = 3
                    except:
                        print(shibai, "执行等待操作，当前等待", i, "秒")
                        i += 1
                        time.sleep(1)
            except:
                print(mingcheng, "不存在，执行等待操作，当前等待", i, "秒")
                i += 1
                time.sleep(1)

    '''封装一个滑动屏幕的方法'''
    def moblie_huadong(self):
        sss = 1
        ii = 1
        while sss == 1:
            try:
                # driver.get_window_size()['width']
                x = MGO.driver.get_window_size()['width']
                y = MGO.driver.get_window_size()['height']
                print("横坐标最大值", x)
                print("纵坐标最大值", y)
                '''尝试滑动屏幕'''
                x1 = x * 0.5
                y1 = y * 0.15
                y2 = y * 0.75
                time.sleep(3)
                print("滑动前")
                '''开始滑动屏幕'''
                MGO.driver.swipe(x1, y1, x1, y2)
                MGO.driver.implicitly_wait(5)
                print("滑动后")
                sss = 2
            except:
                print("获取分辨率失败，再来一次，当前第", ii, "次")
                ii += 1
                time.sleep(1)
