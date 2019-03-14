import MobileNew
import time
import femail
from PIL import Image
import pytesseract
import traceback

'''必改参数'''
url='https://test-plus.vdongchina.com/app/ewei_shopv2_api.php?i=1001&r=member&comefrom=wxapp&openid=sns_wa_o6mWA4noeUX5DRr-FaAajrjZ0e1o&mid=&merchid=&authkey=&timestamp=1539064803196'
shopname="请输入页面标题"
box = (53, 994, 560, 1047)
'''启动手机微信'''
M = MobileNew.MGO()
x=1
while x==1:

    '''先获取该会员的金额'''
    vip_jine_start=M.vip_jine(url)

    '''拍个照片，记录手机状态'''
    M.paizhao("打开微信")

    '''判断微信是否正常打开了'''
    dakai=M.panduan_dakai_wechat()
    if dakai==1:
        '''拍照'''
        png_name=M.paizhao("已打开微信")
    else:
        '''拍照'''
        png_name = M.paizhao("已打开微信")
        '''发邮件报错'''
        M.email("未成功打开微信","plain",png_name)
    print("运行完毕，等待80s")
    time.sleep(80)
    M.On()