import guanjiaPlus.xiaochengxuguanliyemian
import traceback
import time
from selenium.webdriver.support.ui import Select

'''调用进入小程序管理页面的脚本'''
go=guanjiaPlus.xiaochengxuguanliyemian.go
Go=guanjiaPlus.xiaochengxuguanliyemian.Go
GO=guanjiaPlus.xiaochengxuguanliyemian.GO
bug_num=0

def dianpu():

    go.Ctext("店铺","店铺超链接","进入店铺超链接","Bug--无法进入店铺超链接")
    #幻灯片操作
    go.Ctext("幻灯片","幻灯片超链接","进入幻灯片超链接","Bug--无法进入幻灯片超链接")
    go.Ctext("添加幻灯片", "添加幻灯片超链接", "进入添加幻灯片超链接", "Bug--无法进入添加幻灯片超链接")
    go.Ctext("返回列表","返回列表按钮","点击返回列表按钮","Bug--无法点击返回列表按钮")
    # 导航图标
    go.Ctext("导航图标", "导航图标超链接", "进入导航图标超链接", "Bug--无法进入导航图标超链接")
    go.Ctext("添加首页导航", "添加首页导航超链接", "点击添加首页导航超链接", "Bug--无法点击添加首页导航超链接")
    go.CTag_name_zidingyi("input","value","返回列表","返回列表按钮", "点击返回列表按钮", "Bug--无法点击返回列表按钮")

    # 广告
    go.Ctext("广告", "广告超链接", "进入广告超链接", "Bug--无法进入广告超链接")
    go.Ctext("添加广告", "添加广告超链接", "点击添加广告超链接", "Bug--无法点击添加广告超链接")
    go.CTag_name_zidingyi("input", "value", "返回列表", "返回列表按钮", "点击返回列表按钮", "Bug--无法点击返回列表按钮")
    #魔方推荐
    go.Ctext("魔方推荐", "魔方推荐超链接", "点击魔方推荐超链接", "Bug--无法点击魔方推荐超链接")
    go.Cxpath("/html/body/div[6]/div[2]/form/table/tfoot/tr/td/button","添加魔方按钮", "点击添加魔方按钮", "Bug--无法点击添加魔方按钮")
    #商品推荐
    go.Ctext("商品推荐","商品推荐超链接","点击商品超链接按钮","Bug--无法点击商品按钮")
    #排版设置
    go.Ctext("排版设置", "排版设置超链接", "点击排版设置按钮", "Bug--无法点击排版设置按钮")
    #商城

    go.C_class_text("商城超链接","div",'menu-header ',"商城", "点击商城按钮", "Bug--无法点击商城按钮")
    go.Ctext("公告管理", "公告管理超链接", "点击公告管理按钮", "Bug--无法点击公告管理按钮")
    go.Ctext("添加公告", "添加公告超链接", "点击添加公告超链接", "Bug--无法点击添加公告超链接")
    go.CTag_name_zidingyi("input", "value", "返回列表", "返回列表按钮", "点击返回列表按钮", "Bug--无法点击返回列表按钮")

    go.Ctext("评价管理", "评价管理超链接", "点击评价管理按钮", "Bug--无法点击评价管理按钮")
    go.Ctext("添加虚拟评论", "添加虚拟评论超链接", "点击添加虚拟评论超链接", "Bug--无法点击添加虚拟评论超链接")
    go.CTag_name_zidingyi("input", "value", "返回列表", "返回列表按钮", "点击返回列表按钮", "Bug--无法点击返回列表按钮")

    go.Ctext("退货地址", "退货地址超链接", "点击退货地址按钮", "Bug--无法点击退货地址按钮")
    go.Ctext("添加退货地址", "添加退货地址超链接", "点击添加退货地址超链接", "Bug--无法点击添加退货地址超链接")
    go.CTag_name_zidingyi("input", "value", "返回列表", "返回列表按钮", "点击返回列表按钮", "Bug--无法点击返回列表按钮")


    #配送方式
    #go.Ctext("配送方式", "配送方式超链接", "点击配送方式按钮", "Bug--无法点击配送方式按钮")
    go.C_class_text("配送方式超链接", "div", 'menu-header ', "配送方式", "点击配送方式按钮", "Bug--无法点击配送方式按钮")

    go.Ctext("普通快递", "普通快递超链接", "点击普通快递按钮", "Bug--无法点击普通快递按钮")
    go.Ctext("添加配送方式", "添加配送方式超链接", "点击添加配送方式超链接", "Bug--无法点击添加配送方式超链接")
    go.CTag_name_zidingyi("input", "value", "返回列表", "返回列表按钮", "点击返回列表按钮", "Bug--无法点击返回列表按钮")

    #店铺装修
    go.Ctext("店铺装修", "店铺装修超链接", "点击店铺装修按钮", "Bug--无法点击店铺装修按钮")



try:
    dianpu()
    print("***************************************************测试通过")
except:
    print("***************************************************会员测试过程之中有Bug")
    bug_num += 1