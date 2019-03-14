import guanjiaPlus.xiaochengxuguanliyemian
import traceback
import time
from selenium.webdriver.support.ui import Select

'''调用进入小程序管理页面的脚本'''
go=guanjiaPlus.xiaochengxuguanliyemian.go
Go=guanjiaPlus.xiaochengxuguanliyemian.Go
GO=guanjiaPlus.xiaochengxuguanliyemian.GO
bug_num=0

def yingyong_go():
    go.CTextS("应用","应用超链接","进入应用超链接","Bug--无法进入应用超链接")

def jifenshangcheng_home_go():
    go.CText_partial_s("积分商城","积分商城超链接","进入积分商城超链接","Bug--无法进入积分商城超链接")
    try:
        bt=Go.find_element_by_xpath("/html/body/div[3]/div/div[1]/a").text
        if "积分商城" in bt :
            print("已进入积分商城页面")
    except:
        ee=traceback.format_exc()
        go.error()

def jifenshangcheng_shangpinguanli_go():
    go.CTextS("商品管理","商品管理超链接","进入商品管理超链接","Bug--无法进入商品管理超链接")

def jifenshangcheng_shangpin_new():
    go.CText_partial_s("添加商品","添加商品超链接","进入添加商品超链接","Bug--无法进入添加商品超链接")
    go.Sname("displayorder","排序输入框","9999999","输入排序","Bug--无法输入排序")

    #Go.find_element_by_name("cate").
    time.sleep(4)
    go.C_class_text("选择商品按钮","button", "btn btn-primary", "选择商品", "展开选择商品窗口", "Bug--无法展开选择商品窗口")
    #selenium自动手册
    go.Sid("goodsid_input","商品名称输入框","selenium自动手册","输入商品名称","Bug--无法输入商品名称")
    #btn btn-default
    go.C_class_text("选择商品按钮", "button", "btn btn-default", "搜索", "搜索商品", "Bug--无法搜索商品")
    go.CTextS("选择","选择商品按钮","选择对应商品","Bug--无法选择对应商品")
    go.Sid("goodsname","商品标题输入框","清仓！！！！","输入商品标题","Bug--无法输入商品标题")
    go.Sname("credit","积分输入框","12","输入兑换积分","Bug--无法输入兑换积分")
    Select(Go.find_element_by_name("cate")).select_by_visible_text(u"自动打折区")
    go.CClassNameS_danxuan("radio-inline","开启","开启活动单选框","开启活动","Bug--无法开启活动")
    #/html/body/div[6]/div[2]/form/div[3]/div/input
    go.Cxpath("/html/body/div[6]/div[2]/form/div[3]/div/input", "提交按钮", "点击提交按钮", "Bug--无法点击提交按钮")

def jifenshangcheng_shangpin_fenlei_go():
    go.CTextS("分类管理","积分商品分类管理超链接","进入积分商品分类管理","Bug--无法进入积分商品分类管理")

def jifenshangcheng_shangpin_fenlei_new():
    go.CTextS("添加新商品分类", "添加新商品分类超链接", "进入添加新商品分类", "Bug--无法进入添加新商品分类")
    go.Sname("displayorder","排序输入框","99999","输入排序","Bug--无法输入排序")
    go.Sname("catename", "分类名称输入框", "自动打折区", "输入分类名称", "Bug--无法输入分类名称")
    go.CClassNameS_danxuan("radio-inline","是","各种是","选择是","Bug--无法选择是")
    #/html/body/div[6]/div[2]/form/div[7]/div/input[1]
    go.Cxpath("/html/body/div[6]/div[2]/form/div[7]/div/input[1]","提交按钮","点击提交","Bug--无法点击提交")



try:
    yingyong_go()
    jifenshangcheng_home_go()
    jifenshangcheng_shangpinguanli_go()
    jifenshangcheng_shangpin_new()
    jifenshangcheng_shangpin_fenlei_go()
    jifenshangcheng_shangpin_fenlei_new()
    print("***************************************************测试通过")
except:
    print("***************************************************门店管理测试过程之中有Bug")
    bug_num+=1



