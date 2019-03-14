import PC_zonghe_selenium.into.into_applet_later.into_lonely_applet_catering
import traceback
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

'''调用进入小程序管理页面的脚本'''
f=PC_zonghe_selenium.into.into_applet_later.into_lonely_applet_catering
go=f.go
Go=f.Go
GO=f.GO
object_on=f.object_on
type_on=f.type_on
'''定义一些固定的值'''
bug_num=0
miaoshu="这是一个自动添加的商品分类，纯测试用分类，只在这次测试过程中使用，当脚本测试结束之后，本分类会被删除。"
miaoshu_g="这是一个自动添加的商品分类，纯测试用分类，只在这次测试过程中使用，当脚本测试结束之后，本分类会被删除--改。"


def shop_list():
    go.CText_partial_s("门店管理","门店管理列表","进入门店管理列表","Bug-无法进入门店管理列表")
    go.CTag_name_zidingyi("li","kw","门店列表","门店列表","进入门店列表","Bug-无法进入门店列表")
def shop_area_home():
    go.CText_partial_s("门店区域", "门店区域列表", "进入门店区域列表", "Bug-无法进入门店区域列表")
def shop_area_new():
    go.CTag_name_zidingyi("li", "kw", "区域添加", "区域添加", "进入区域添加", "Bug-无法进入区域添加")
    go.Sname("area_name","地区名称","北京市","输入地区","Bug--无法输入地区")
    go.Cname("submit","提交按钮","点击提交按钮","Bug--无法点击提交按钮")
def shop_type_home():
    go.CText_partial_s("门店类型", "门店类型列表", "进入门店类型列表", "Bug-无法进入门店类型列表")
def shop_type_new():
    go.CTag_name_zidingyi("li", "kw", "类型添加 ", "类型添加", "进入添加类型", "Bug-无法进入添加类型")
    go.Sname("type_name", "类型名称", "实体店", "输入类型", "Bug--无法输入类型")
    go.Sid("points","平台手续费输入框","1","输入平台手续费","Bug--无法输入平台手续费")
    go.Cname("submit", "提交按钮", "点击提交按钮", "Bug--无法点击提交按钮")
def system_setting_home():
    go.CText_partial_s("系统设置", "系统设置列表", "进入系统设置", "Bug-无法进入系统设置")
def system_setting_basics():
    go.CText_partial_s("系统设置", "系统设置列表", "进入系统设置", "Bug-无法进入系统设置")
    go.Sname("pt_name","平台名称输入框","selenium级餐饮平台","输入平台名称","Bug--无法输入平台名称")
    go.Sname("tel", "平台电话输入框", "18710262651", "输入平台电话", "Bug--无法输入平台电话")
    go.danxuan_tagname("开启")
    go.Cname("submit", "提交按钮", "点击提交按钮", "Bug--无法点击提交按钮")
def system_setting_applet():
    go.CTag_name_zidingyi("li", "kw", "小程序配置", "小程序配置", "进入小程序配置", "Bug-无法进入小程序配置")
    go.Sname("appid","appid输入框","wx9f6d03289af0458d","输入appid","Bug--无法输入appid")
    go.Sname("appsecret", "Appsecret输入框", "01cd77df3f2846a64c9d12c644b2e2d4", "输入Appsecret", "Bug--无法输入Appsecret")
    go.Sname("map_key", "map_key输入框", "54HBZ-R5LRO-SB2WL-SVRQM-EFOGZ-XSFQM", "输入map_key", "Bug--无法输入map_key")
    go.Cname("submit", "保存设置按钮", "点击保存设置按钮", "Bug--无法点击保存设置按钮")




'''***********************************************************************执行区域'''
try:
    shop_area_home()
    shop_area_new()
    shop_type_home()
    shop_type_new()
    system_setting_basics()
    system_setting_home()
    system_setting_applet()
except:
    go.error()
    bug_num += 1
'''***********************************************************************反馈区域'''









'''***********************************************************************最终反馈区域'''
print("不通过的模块共有%d个" % bug_num)