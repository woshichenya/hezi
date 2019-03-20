from beifen import BaibaoxiangMobile
import time


'''必改参数'''
shopname="请输入页面标题"
box = (53, 994, 560, 1047)




'''启动手机微信'''
M= BaibaoxiangMobile.MGO()
M.biaoji_time()
time.sleep(20)


'''
M.dianji(143,273,390,337,500)
print("点击产品研发9公众号")
time .sleep(10)
M.paizhao("进入产品研发9公众号")

M.Cid("com.tencent.mm:id/acp","输入框按钮","展开输入框","Bug--无法展开输入框")


M.driver.find_element_by_id("com.tencent.mm:id/ac8").send_keys("11111111")
'''


M.moblie_huadong()
M.Cid("com.tencent.mm:id/gd","管家plus小程序入口","进入管家plus小程序中","Bug--无法进入小程序")


gogo=1
ii=1
while gogo==1 and ii<=10:
    M.biaoji_time()
    try:
        biaoti_new=M.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/kt']").text
        print("成功进入小程序")
        print("当前标题是：",biaoti_new)
        gogo=2
        M.biaoji_time()
    except:
        print("再次点击执行进入小程序操作")
        M.Cid("com.tencent.mm:id/gd", "管家plus小程序入口", "进入管家plus小程序中", "Bug--无法进入小程序")
        ii+=1
        time.sleep(5)
        M.biaoji_time()
if ii==11:
    print("呵呵了")

time.sleep(20)

'''打开全部分类'''
shuxin = "//android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
M.Cxpath(shuxin, "底部导航全部分类", "进入全部分类", "Bug--无法进入全部分类")
M.biaoji_time()
time.sleep(15)
'''拍照'''
pen_names = M.paizhao("打开全部分类")


'''打开所有商品'''
print("打开所有商品")
M.dianji(65,395,175,545,500)
M.biaoji_time()
time.sleep(10)

'''拍照'''
pen_names =M.paizhao("打开所有商品")

#M.driver.find_element_by_xpath("//android.view.View[@content-desc='输入关键字进行搜索']").send_keys("111111111")
try:
    M.driver.find_element_by_xpath("//android.view.View[@content-desc='轩斯顿2018夏装韩版假两件短袖t恤男宽松潮流七分袖上衣五分半袖体恤打底衫男装 灰色1 XXXL']").click()
except Exception as e:
    print(e)
#//android.view.View[@content-desc='输入关键字进行搜索']