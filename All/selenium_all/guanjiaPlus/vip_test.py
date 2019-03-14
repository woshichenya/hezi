import guanjiaPlus.xiaochengxuguanliyemian
import traceback
import time
from selenium.webdriver.support.ui import Select

'''调用进入小程序管理页面的脚本'''
go=guanjiaPlus.xiaochengxuguanliyemian.go
Go=guanjiaPlus.xiaochengxuguanliyemian.Go
GO=guanjiaPlus.xiaochengxuguanliyemian.GO
bug_num=0

def vip_home():
    go.CTextS("会员","会员超链接","进入会员管理页面","Bug--无法进入会员管理页面")

def vip_level_go():
    go.CTextS("会员等级", "会员等级超链接", "进入会员等级管理页面", "Bug--无法进入会员等级管理页面")

def vip_level_new():
    go.CTextS("添加会员等级","添加会员等级按钮","进入添加会员等级页面","Bug--无法进入添加会员等级页面")
    go.Sname("levelname","等级名称输入框","自动会员等级","输入会员等级名称","Bug--无法输入会员等级名称")

    go.Sname("ordermoney", "等级升级金额输入框", "200", "输入升级金额", "Bug--无法输入升级金额")
    go.CClassNameS_danxuan("radio-inline","启用","启用单选框","启用会员等级","Bug--无法启用会员等级")
    go.Cxpath("/html/body/div[6]/div[2]/form/div[7]/div/input[1]","提交按钮","点击提交按钮","Bug--无法点击提交按钮")
def vip_level_sousuo():
    go.Sname_zidingyi_s("keyword","placeholder","请输入关键词","自动会员等级","会员等级输入框","输入会员等级","Bug--无法输入会员等级")
    go.CTag_name_zidingyi("button","text","搜索","搜索按钮","点击搜索按钮","Bug--无法点击搜索按钮")


def vip_level_delete():
    #print(Go.find_element_by_xpath("/html/body/div[6]/div[2]/form[1]/div/div[2]/div/input").get_attribute("placeholder"))
    #print(Go.find_element_by_xpath("/html/body/div[6]/div[2]/form[1]/div/div[2]/div/input").text)
    #go.Sname("keyword","会员等级输入框","自动会员等级","输入会员等级","Bug--无法输入会员等级")
    print(Go.find_element_by_xpath("/html/body/div[6]/div[2]/form[2]/table/tbody/tr/td[7]/a[3]").text)
    go.Cxpath("/html/body/div[6]/div[2]/form[2]/table/tbody/tr/td[7]/a[3]/span/i", "第一个商品分类的删除按钮", "点击删除按钮","Bug--无法点击删除按钮")
    # go.CTextS("确 定","确定给删除按钮","点击确定删除按钮","Bug--无法点击确定删除按钮")
    go.Cxpath("/html/body/div[8]/div[2]/div/div/div/div/div[4]/button[1]", "确定给删除按钮", "点击确定删除按钮", "Bug--无法点击确定删除按钮")

def vip_level_updata():
    go.Cxpath("/html/body/div[6]/div[2]/form[2]/table/tbody/tr/td[7]/a[2]/span/i","编辑按钮","点击编辑按钮","Bug--无法点击编辑按钮")
    go.Sname("ordermoney", "等级升级金额输入框", "201", "输入升级金额", "Bug--无法输入升级金额")
    go.Sname("levelname", "等级名称输入框", "自动会员等级改", "输入会员等级名称", "Bug--无法输入会员等级名称")
    go.Cxpath("/html/body/div[6]/div[2]/form/div[7]/div/input[1]", "提交按钮", "点击提交按钮", "Bug--无法点击提交按钮")


def vip_sousuo_panduan():
    go.STag_name_zidingyi("input","placeholder","可搜索昵称/姓名/手机号/ID","陈雅","搜索关键字","输入关键字","Bug--无法输入关键字")
    go.CTag_name_zidingyi("button","text","搜索","搜索按钮","点击搜索按钮","Bug--无法点击搜索按钮")

    try:
        c_s=go.llq.find_elements_by_class_name("nickname")
        x=0
        for i_c_s in c_s:
            if i_c_s.text=="陈雅":
                print(i_c_s.text)
                x+=1
        print("共搜索到了",x,"个结果")
    except:
        ee=traceback.format_exc()
        print("开始报错")
        print(ee)
        print("结束报错")
        print("未搜索到陈雅")
    if x>0:
        print("*********************************************************************会员搜索功能测试通过")

def vip_biaoqian_home():
    go.CTextS("标签组", "标签组超链接", "进入会员标签组管理页面", "Bug--无法进入会员标签组管理页面")
def vip_biaoqian_new():
    go.CTextS("添加标签组","添加会员标签组按钮","进入添加会员标签组页面","Bug--无法进入添加会员标签组页面")
    go.Sname("groupname","标签组名称输入框","自动会员标签组","输入会员标签组名称","Bug--无法输入会员标签组名称")
    go.Sname("description","标签组描述框", "自动添加的会员标签组描述",  "输入会员标签组描述", "Bug--无法输入会员标签组描述")
    go.CTag_name_zidingyi("button","text","提交","提交按钮","点击提交按钮","Bug--无法点击提交按钮")

def vip_biaoqian_sousuo():
    go.STag_name_zidingyi("input","placeholder","请输入关键词","自动会员标签组","关键字输入框","输入关键字","Bug--无法输入关键字")
    go.CTag_name_zidingyi("button","text","搜索","搜索按钮","点击搜索按钮","Bug--无法点击搜索按钮")
def vip_biaoqian_updata():
    #print("会员标签修改")
    #go.Cxpath("/html/body/div[6]/div[2]/form[2]/table/tbody/tr/td[7]/a[2]/span/i", "编辑按钮", "点击编辑按钮", "Bug--无法点击编辑按钮")
    go.CTag_name_zidingyi("span", "data-original-title", "修改", "修改按钮", "点击修改按钮", "Bug--无法点击修改按钮")
    go.Sname("groupname","标签名称输入框","自动会员标签组改","输入标签名称","Bug--无法输入标签名称")
    go.C_class_text("提交按钮","button","btn btn-primary","提交","点击提交按钮","Bug--无法点击提交按钮")
def vip_biaoqian_delete():
    go.CTag_name_zidingyi("span", "data-original-title", "删除", "删除按钮", "点击删除按钮", "Bug--无法点击删除按钮")
    go.C_class_text("确定按钮", "button", "btn btn-primary", "确 定", "点击确定按钮", "Bug--无法点击确定按钮")

def vip_card_home():
    go.Ctext("微信会员卡","微信会员卡超链接","点击微信会员卡超链接","Bug--无法点击微信会员卡超链接")
def vip_card_new():#无需调用
    go.Ctext("去添加","添加会员卡按钮","点击添加会员卡按钮","Bug--无法点击添加会员卡按钮")
    go.Sid("card_title","会员卡名称输入框","自动添加会员卡","输入会员卡名称","Bug--无法输入会员卡名称")
    #card_brand_name
    go.Sid("card_brand_name", "会员卡店铺名称输入框", "自动添加会员卡店铺", "输入会员卡店铺名称", "Bug--无法输入会员卡店铺名称")
    #card_totalquantity
    go.Sid("card_totalquantity", "会员卡库存总量输入框", "998", "输入会员卡库存总量", "Bug--无法输入会员卡库存总量")
    go.Cid("uploadlogo","上传图片按钮","点击上传图片","Big--无法点击上传图片")
    go.CText_partial_s("提取网络图片","网络照片按钮","点击提取网络照片","Big--无法点击提取网络照片")
    go.STag_name_zidingyi("input","placeholder","图片链接","http://mpimg.vdongchina.com/images/2040/2018/11/mGiEbXZAEzGxjwGAZXBIpC6rcij4R3.jpg","图片链接","输入图片链接","Bug--无法输入图片链接")
    go.C_class_text("转化按钮","button","btn btn-default","转化","点击转化按钮","Bug--无法点击转化按钮")
    #go.Cxpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[1]/div","第一张图片","点击第一张图片","Bug--无法点击第一张图片")
    go.CClassNameS_danxuan("radio-inline","使用","显示余额单选框","点击使用","Big--无法点击使用")
    go.Sname("prerogative","特权说明","这是一个很666的特权","输入特权说明","Bug--无法输入特权说明")
    go.Sname("card_description", "使用须知", "一日会员终生会员", "输入使用须知", "Bug--无法输入使用须知")
    go.CTag_name_zidingyi("input","value","提交","提交按钮","点击提交按钮","Bug--点击提交按钮")


'''
******************************************************************************************运行区域
'''

try:
    vip_home()
    vip_sousuo_panduan()
    vip_level_go()
    vip_level_new()
    vip_level_sousuo()
    vip_level_updata()
    vip_level_sousuo()
    vip_level_delete()
    time.sleep(5)
    vip_biaoqian_home()
    vip_biaoqian_new()
    vip_biaoqian_home()
    vip_biaoqian_sousuo()
    vip_biaoqian_updata()
    vip_biaoqian_home()
    vip_biaoqian_sousuo()
    vip_biaoqian_delete()
    vip_card_home()
    print("***************************************************测试通过")
except:
    print("***************************************************会员测试过程之中有Bug")
    bug_num += 1



