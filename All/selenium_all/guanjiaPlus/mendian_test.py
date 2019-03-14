import guanjiaPlus.xiaochengxuguanliyemian
import traceback
import time
from selenium.webdriver.support.ui import Select

'''调用进入小程序管理页面的脚本'''
go=guanjiaPlus.xiaochengxuguanliyemian.go
Go=guanjiaPlus.xiaochengxuguanliyemian.Go
GO=guanjiaPlus.xiaochengxuguanliyemian.GO
bug_num=0

def shop_home():
    go.Ctext("门店","门店超链接","点击门店超链接","Bug--点击门店超链接")
def shop_new():
    go.CText_partial_s("添加门店","添加门店超链接","点击添加门店超链接","Bug--无法点击添加门店超链接")
    go.Sname("storename","门店名称输入框","selenium自动门店","输入名店名称","Bug--无法输入名店名称")
    go.C_class_text("选择图片插件", "button", "btn btn-primary", "选择图片", "打开选择图片插件", "Bug--无法打开选择图片插件")
    go.Cxpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[1]/div", "第一张图片", "点击第一张图片", "Bug--无法点击第一张图片")
    go.Cid("sel-provance","省下拉框","展开省","Bug--无法展开省")
    go.C_xialakuang_zidingyi_text("sel-provance",u"北京市","id","省选项","已选中省","Bug--无法选择省")
    go.Cid("sel-city", "市下拉框", "展开市下拉框", "Bug--无法展开市下拉框")
    go.C_xialakuang_zidingyi_text("sel-city", u"北京辖区", "id", "市选项", "已选中省", "Bug--无法选择市")
    go.Cid("sel-area", "区下拉框", "展开区下拉框", "Bug--无法展开区下拉框")
    go.C_xialakuang_zidingyi_text("sel-area", u"昌平区", "id", "区选项", "已选中区", "Bug--无法选择区")
    go.Sname("tel","电话输入框","18710262651","输入号码","Bug--无法输入号码")
    #saletime
    go.Sname("saletime", "营业时间输入框", "全天营业", "输入营业时间", "Bug--无法输入营业时间")
    go.Sname("map[lng]", "经度输入框", "116.35422864652487", "输入经度", "Bug--无法输入经度")
    go.Sname("map[lat]", "纬度输入框", "40.08552330485823", "输入纬度", "Bug--无法输入纬度")
    #address
    go.Sname("address", "地址输入框", "北京市昌平区回龙观东大街", "输入地址", "Bug--无法输入地址")
    go.CClassNameS_danxuan('radio-inline',"支持自提+核销","选项支持自提+核销","选择支持自提+核销选项","Bug--无法选择支持自提+核销选项")
    "radio-inline"
    go.CClassNameS_danxuan('radio-inline', "启用", "选项启用", "选择启用选项", "Bug--无法选择启用选项")
    go.CTag_name_zidingyi("input","value","提交","提交按钮","点击提交按钮","Bug--无法点击提交按钮")


def shop_sousuo():
    #keyword
    go.STag_name_zidingyi("input","placeholder","门店名称/地址/电话","selenium自动门店","关键字输入框","输入关键字", "Bug--无法输入关键字" )
    go.CTag_name_zidingyi("button", "text", "搜索", "搜索按钮", "点击搜索按钮", "Bug--无法点击搜索按钮")

def shop_delete():
    go.CTag_name_zidingyi("span", "data-original-title", "删除", "删除按钮", "点击删除按钮", "Bug--无法点击删除按钮")
    go.C_class_text("确定按钮", "button", "btn btn-primary", "确 定", "点击确定按钮", "Bug--无法点击确定按钮")

try:
    shop_home()
    shop_new()
    shop_home()
    shop_sousuo()
    shop_delete()
    print("***************************************************门店测试通过")
except:
    print("***************************************************门店管理测试过程之中有Bug")
    bug_num+=1