import PC_zonghe_selenium.into.into_applet_later.into_lonely_applet_same_city
import traceback
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

'''调用进入小程序管理页面的脚本'''
f=PC_zonghe_selenium.into.into_applet_later.into_lonely_applet_same_city
go=f.go
Go=f.Go
GO=f.GO
object_on=f.object_on
type_on=f.type_on
'''定义一些固定的值'''
bug_num=0
miaoshu="这是一个自动添加的商品分类，纯测试用分类，只在这次测试过程中使用，当脚本测试结束之后，本分类会被删除。"
miaoshu_g="这是一个自动添加的商品分类，纯测试用分类，只在这次测试过程中使用，当脚本测试结束之后，本分类会被删除--改。"



def gps_setting_home():
    go.CText_partial_s("导航管理", "导航管理列表", "进入导航管理列表", "Bug-无法进入导航管理列表")
def gps_setting_new():
    go.CText_partial_s("导航管理", "导航管理列表", "进入导航管理列表", "Bug-无法进入导航管理列表")
    go.CTag_name_zidingyi("li", "kw", "添加导航", "添加导航", "进入添加导航", "Bug-无法进入添加导航")
    go.Sname("title","导航名称输入框","selenium入口","输入导航名称","Bug--无法输入导航名称")
    go.C_class_text("选择图片","button","btn btn-default","选择图片","打开选择图片插件","Bug--无法打开选择图片插件")
    go.Cxpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]","第一张图片","选择第一张图片","Bug--无法选择第一张图片")
    go.CTag_name_zidingyi("button","text","确定","确定按钮","点击确定按钮","Bug--无法点击确定按钮")
    go.Sname("orderby","排序输入框","99","输入排序","Bug--无法输入排序")
    go.Cname("submit", "提交按钮", "点击提交按钮", "Bug--无法点击提交按钮")
    go.Ctext("如果你的浏览器没有自动跳转，请点击此链接","自动转跳链接","点击自动转跳","Bug--无法点击自动转跳")
def shop_setting_home():
    go.CText_partial_s("商家管理", "商家管理列表", "进入商家管理列表", "Bug-无法进入商家管理列表")
def shop_setting_new():
    go.CText_partial_s("商家管理", "商家管理列表", "进入商家管理列表", "Bug-无法进入商家管理列表")
    go.CTag_name_zidingyi("li", "kw", "商家添加 ", "添加商家页面", "进入商家添加页面", "Bug-无法进入商家添加页面")
    go.Sname("store_name", "商家名称输入框","selenium商家","输入商家名称", "Bug--无法输入商家名称")
    go.Sname("tel", "商家电话输入框","18710262651", "输入商家电话", "Bug--无法输入商家电话")
    go.Sname("address", "商家地址输入框","北京市昌平区回龙观东大街", "输入商家地址", "Bug--无法输入商家地址")
    go.Sname("coordinates", "地址坐标输入框", "40.081700,116.360514", "输入地址坐标", "Bug--无法输入地址坐标")
    mop=go.llq.find_elements_by_xpath("//button[@class = 'btn btn-default' and text() = '选择图片']")
    time.sleep(2)
    print("共有选择图片",len(mop),"个")
    if len(mop) >=2:
        for mop_i in mop:
            try:
                mop_i_t=mop_i.text
            except:
                mop_i_t=mop_i.get_attribute("value")
            if mop_i_t == "选择图片":
                print("点击一次")
                mop_i.click()
                go.Cxpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]", "第一张图片", "选择第一张图片", "Bug--无法选择第一张图片")
                go.CTag_name_zidingyi("button", "text", "确定", "确定按钮", "点击确定按钮", "Bug--无法点击确定按钮")
                time.sleep(4)
    go.Sname("announcement","公告输入框","selenium的小广告","输入广告","Bug--无法输入广告")
    go.Sname("start_time", "营业开始时间输入框", "00:00", "输入营业开始时间", "Bug--无法输入营业开始时间")
    go.Sname("end_time", "营业结束时间输入框", "23:59", "输入营业结束时间", "Bug--无法输入营业结束时间")

    # go.C_class_text("选择图片", "button", "btn btn-default", "选择图片", "打开选择图片插件", "Bug--无法打开选择图片插件")








'''***********************************************************************执行区域'''
try:
    print("开始执行")
    # gps_setting_new()
    # shop_setting_home()
    shop_setting_new()

except:
    go.error()
    bug_num += 1
'''***********************************************************************反馈区域'''









'''***********************************************************************最终反馈区域'''
print("不通过的模块共有%d个" % bug_num)