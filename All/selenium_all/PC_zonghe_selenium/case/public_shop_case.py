import PC_zonghe_selenium.into.into_public
import traceback
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

'''调用进入小程序管理页面的脚本'''
f=PC_zonghe_selenium.into.into_public
go=f.go
Go=f.Go
GO=f.GO
object_on=f.object_on
type_on=f.type_on
'''定义一些固定的值'''
bug_num=0
miaoshu="这是一个自动添加的商品分类，纯测试用分类，只在这次测试过程中使用，当脚本测试结束之后，本分类会被删除。"
miaoshu_g="这是一个自动添加的商品分类，纯测试用分类，只在这次测试过程中使用，当脚本测试结束之后，本分类会被删除--改。"


'''*******************************************************************会员测试'''
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
    try:
        print(Go.find_element_by_xpath("/html/body/div[6]/div[2]/form[2]/table/tbody/tr/td[7]/a[3]").text)
    except:
        go.error()
    go.Cxpath("/html/body/div[6]/div[2]/form[2]/table/tbody/tr/td[7]/a[3]/span/i", "第一个商品分类的删除按钮", "点击删除按钮","Bug--无法点击删除按钮")
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
        go.error()
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
    go.Sid("card_brand_name", "会员卡店铺名称输入框", "自动添加会员卡店铺", "输入会员卡店铺名称", "Bug--无法输入会员卡店铺名称")
    go.Sid("card_totalquantity", "会员卡库存总量输入框", "998", "输入会员卡库存总量", "Bug--无法输入会员卡库存总量")
    go.Cid("uploadlogo","上传图片按钮","点击上传图片","Big--无法点击上传图片")
    go.CText_partial_s("提取网络图片","网络照片按钮","点击提取网络照片","Big--无法点击提取网络照片")
    go.STag_name_zidingyi("input","placeholder","图片链接","http://mpimg.vdongchina.com/images/2040/2018/11/mGiEbXZAEzGxjwGAZXBIpC6rcij4R3.jpg","图片链接","输入图片链接","Bug--无法输入图片链接")
    go.C_class_text("转化按钮","button","btn btn-default","转化","点击转化按钮","Bug--无法点击转化按钮")
    go.CClassNameS_danxuan("radio-inline","使用","显示余额单选框","点击使用","Big--无法点击使用")
    go.Sname("prerogative","特权说明","这是一个很666的特权","输入特权说明","Bug--无法输入特权说明")
    go.Sname("card_description", "使用须知", "一日会员终生会员", "输入使用须知", "Bug--无法输入使用须知")
    go.CTag_name_zidingyi("input","value","提交","提交按钮","点击提交按钮","Bug--点击提交按钮")

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
    print("***************************************************会员测试通过")
except:
    print("***************************************************会员测试过程之中有Bug")
    bug_num += 1



'''*******************************************************************商品测试'''
def shangpin_home_go():
    go.CTextS("商品","商品超链接","进入商品页面","Bug--无法进入商品页面")
    go.CTextS("出售中","出售中超链接","进入出售中页面","Bug--无法进入出售中页面")
def shangpin_fenlei_go():
    go.CTextS("商品分类", "商品分类超链接", "进入商品分类页面", "Bug--无法进入商品分类页面")
def shangpin_fenlei_new():
    go.CTextS("添加新分类", "添加商品分类按钮", "进入添加商品分类页面", "Bug--无法进入添加商品分类页面")
    go.Sname("displayorder","排序输入框","9999999","输入排序","Bug--无法输入排序")
    go.Sname("catename","分类名称","自动添加分类","输入商品分类","Bug--无法输入商品分类")
    go.Sname("description", "分类介绍", miaoshu, "输入商品分类描述", "Bug--无法输入商品分类描述")
    go.Cxpath("/html/body/div[6]/div[2]/form/div[5]/div/div[1]/span/button","选择图片插件","打开选择图片插件","Bug--无法打开选择图片插件")
    if object_on=="plus":
        go.Cxpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[1]/div", "第一张图片", "点击第一张图片", "Bug--无法点击第一张图片")
    if object_on=="wchen":
        go.Cxpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]","第一张图片","点击第一张图片","Bug--无法点击第一张图片")
    if object_on=="wchen":
        go.Cxpath("/html/body/div[1]/div/div/div[3]/button[1]","确定按钮","点击确定","Bug--无法点击确定")
    go.Sid("advurl","分类广告链接","./index.php?i=1001&c=entry&m=ewei_shopv2&do=mobile","输入分类广告链接","Bug--无法输入分类广告链接")
    go.CClassNameS_danxuan("radio-inline","是","是_单选框","选择是","Bug--无法选择是")
    go.CTag_name("input","提交","提交按钮","点击提交按钮","Bug--无法点击提交按钮")
def shangpin_fenlei_updata():
    go.Cxpath("/html/body/div[6]/div[2]/form/div/ol/li[1]/div/span/a[1]/span/i","第一个商品分类的修改按钮","点击修改按钮","Bug--无法点击修改按钮")
    go.Sname("catename", "分类名称", "自动添加分类-改", "输入商品分类", "Bug--无法输入商品分类")
    go.Sname("description", "分类介绍", miaoshu_g, "输入商品分类描述", "Bug--无法输入商品分类描述")
    go.CTag_name("input", "提交", "提交按钮", "点击提交按钮", "Bug--无法点击提交按钮")
def shangpin_fenlei_delect():
    go.Cxpath("/html/body/div[6]/div[2]/form/div/ol/li[1]/div/span/a[2]/span/i", "第一个商品分类的删除按钮", "点击删除按钮","Bug--无法点击删除按钮")
    go.Cxpath("/html/body/div[8]/div[2]/div/div/div/div/div[4]/button[1]","确定给删除按钮","点击确定删除按钮","Bug--无法点击确定删除按钮")
def shangpin_new():
    shangpin_home_go()
    go.CTextS("添加商品","添加商品按钮","进入添加商品页面","Bug--无法进入添加商品页面")
    go.Sxpath("//input[@id='displayorder']", "排序输入框", "99999", "输入排序中", "Bug-无法输入商品排序")
    go.Sxpath("//input[@id='goodsname']", "商品名输入框", "selenium自动手册", "输入商品名中", "Bug-无法输入商品名")
    go.CClassNameS_danxuan("radio-inline","实体商品","实体商品单选框","点击实体商品单选框","Bug--无法点击实体商品单选框")
    go.Cid("s2id_autogen2","商品分类下拉框","展开商品分类下拉框","Bug--无法展开商品分类下拉框")
    go.CClassNameS_danxuan("select2-result-label","自动添加分类","商品分类-自动添加分类","选择商品分类-自动添加分类","Bug--无法选择商品分类-自动添加分类")
    go.CClassNameS_danxuan("checkbox-inline","推荐","推荐复选框","勾选推荐","Bug--无法勾选推荐")
    go.CClassNameS_danxuan("checkbox-inline", "新品", "新品复选框", "勾选新品", "Bug--无法勾选新品")
    go.CClassNameS_danxuan("checkbox-inline", "热卖", "热卖复选框", "勾选热卖", "Bug--无法勾选热卖")
    go.Sid("marketprice","价格","10","输入价格","Bug--无法输入价格")
    go.Sid("productprice", "原价", "101", "输入原价", "Bug--无法输入原价")
    go.Sid("costprice", "成本", "101", "输入成本", "Bug--无法输入成本")
    go.llq.find_element_by_id("sales").send_keys(Keys.DOWN)
    go.C_class_text("选择图片插件", "button", "btn btn-primary", "选择图片", "打开选择图片插件", "Bug--无法打开选择图片插件")
    if object_on=="plus":
        go.Cxpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[1]/div", "第一张图片", "点击第一张图片", "Bug--无法点击第一张图片")
    if object_on=="wchen":
        go.Cxpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]","第一张图片","点击第一张图片","Bug--无法点击第一张图片")
    go.C_class_text("确定按钮", "button", "btn btn-primary", "确定", "点击确定按钮", "Bug--无法点击确定按钮")

    go.Sid("sales","已售出","10086","输入已售出数量","Bug--无法输入已售出数量")
    go.CClassNameS_danxuan("checkbox-inline", "正品保证", "正品保证复选框", "勾选正品保证", "Bug--无法勾选正品保证")
    go.CClassNameS_danxuan("radio-inline", "上架", "上架单选框", "勾选上架", "Bug--无法勾选上架")

    #库存/规格
    go.CTextS_Key("库存/规格", "库存/规格超链接", "进入库存/规格模块", "Bug--无法进入库存/规格模块")
    go.Sid("weight","重量输入框","0.5","输入商品重量 ","Bug--无法输入商品重量")
    go.Sid("total","库存输入框","99999","输入库存 ","Bug--无法输入库存")
    go.Cid("showtotal","显示库存复选框","勾选显示库存","Bug--无法勾选显示库存")
    go.Cxpath("/html/body/div[6]/div[2]/form/div[2]/div/input","保存按钮","点击保存按钮","Bug--无法点击保存按钮")
def shangpin_sousuo():
    go.STag_name_zidingyi("input","placeholder","ID/名称/编号/条码/商户名称","selenium自动手册","搜索关键字输入框","输入关键字","Bug--无法输入关键字")
    go.CTag_name_zidingyi("button", "text", "搜索", "搜索按钮", "点击搜索按钮", "Bug--无法点击搜索按钮")
def shangpin_updata():
    go.Cxpath("/html/body/div[6]/div[2]/div[2]/div/table/tbody/tr/td[10]/a[1]/span/i", "编辑按钮", "点击编辑按钮", "Bug--无法点击编辑按钮")
    go.Sxpath("//input[@id='goodsname']", "商品名输入框", "selenium自动手册改", "输入商品名中", "Bug-无法输入商品名")
    sss=go.llq.find_element_by_xpath("/html/body/div[5]/div[2]/form/div[2]/div/input").get_attribute("value")
    print("value是",sss)
    go.CTag_name_zidingyi("input","value","保存商品","保存商品按钮","点击保存商品按钮","Bug--无法点击保存商品按钮")
def shangpin_delete():
    go.Cxpath("/html/body/div[6]/div[2]/div[2]/div/table/tbody/tr/td[10]/a[2]/span/i","删除按钮","点击删除按钮","Bug--无法点击删除按钮")
    go.CTag_name_zidingyi("button","text","确 定","确定删除按钮","点击确定删除按钮","Bug--无法点击确定删除按钮")

try:
    shangpin_home_go()
    shangpin_fenlei_go()
    shangpin_fenlei_new()
    shangpin_home_go()
    shangpin_new()
    shangpin_home_go()
    shangpin_sousuo()
    shangpin_updata()
    shangpin_home_go()
    shangpin_sousuo()
    shangpin_delete()
    shangpin_home_go()
    shangpin_fenlei_go()
    shangpin_fenlei_updata()
    shangpin_home_go()
    shangpin_fenlei_go()
    shangpin_fenlei_delect()
    print("***************************************************商品测试通过")
except:
    print("***************************************************商品测试过程之中有Bug")
    bug_num+=1

'''*******************************************************************门店管理测试'''
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
    go.llq.find_element_by_xpath("/html/body/div[6]/div[2]/form/div[1]/div[1]/div[16]/div/div/input[1]").send_keys(Keys.END)
    time.sleep(4)
    go.C_class_text("选择商品按钮","button", "btn btn-primary", "选择商品", "展开选择商品窗口", "Bug--无法展开选择商品窗口")
    go.Sid("goodsid_input","商品名称输入框","积分商品","输入商品名称","Bug--无法输入商品名称")
    go.C_class_text("选择商品按钮", "button", "btn btn-default", "搜索", "搜索商品", "Bug--无法搜索商品")
    go.CTextS("选择","选择商品按钮","选择对应商品","Bug--无法选择对应商品")
    go.Sid("goodsname","商品标题输入框","清仓！！！！","输入商品标题","Bug--无法输入商品标题")
    go.Sname("credit","积分输入框","12","输入兑换积分","Bug--无法输入兑换积分")
    Select(Go.find_element_by_name("cate")).select_by_visible_text(u"自动打折区")
    go.CClassNameS_danxuan("radio-inline","开启","开启活动单选框","开启活动","Bug--无法开启活动")
    go.Cxpath_cler("/html/body/div[6]/div[2]/form/div[3]/div/input", "提交按钮", "点击提交按钮", "Bug--无法点击提交按钮")
def jifenshangcheng_shangpin_fenlei_go():
    go.CTextS("分类管理","积分商品分类管理超链接","进入积分商品分类管理","Bug--无法进入积分商品分类管理")
def jifenshangcheng_shangpin_fenlei_new():
    go.CTextS("添加新商品分类", "添加新商品分类超链接", "进入添加新商品分类", "Bug--无法进入添加新商品分类")
    go.Sname("displayorder","排序输入框","99999","输入排序","Bug--无法输入排序")

    go.Sname("catename", "分类名称输入框", "自动打折区", "输入分类名称", "Bug--无法输入分类名称")
    go.CClassNameS_danxuan("radio-inline","是","各种是","选择是","Bug--无法选择是")

    go.Cxpath("/html/body/div[6]/div[2]/form/div[7]/div/input[1]","提交按钮","点击提交","Bug--无法点击提交")

try:
    yingyong_go()
    jifenshangcheng_home_go()
    jifenshangcheng_shangpin_fenlei_go()
    jifenshangcheng_shangpin_fenlei_new()
    jifenshangcheng_shangpinguanli_go()
    jifenshangcheng_shangpin_new()

    print("***************************************************积分商城测试通过")
except:
    print("***************************************************门店管理测试过程之中有Bug")
    bug_num+=1





def shop_home():
    go.Ctext("门店","门店超链接","点击门店超链接","Bug--点击门店超链接")
def shop_new():
    go.CText_partial_s("添加门店","添加门店超链接","点击添加门店超链接","Bug--无法点击添加门店超链接")
    go.Sname("storename","门店名称输入框","selenium自动门店","输入名店名称","Bug--无法输入名店名称")
    go.C_class_text("选择图片插件", "button", "btn btn-primary", "选择图片", "打开选择图片插件", "Bug--无法打开选择图片插件")
    if object_on=="plus":
        go.Cxpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[1]/div", "第一张图片", "点击第一张图片", "Bug--无法点击第一张图片")
    if object_on=="wchen":
        go.Cxpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]","第一张图片","点击第一张图片","Bug--无法点击第一张图片")
    if object_on=="wchen":
        go.Cxpath("/html/body/div[1]/div/div/div[3]/button[1]","确定按钮","点击确定","Bug--无法点击确定")
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
    #go.llq.find_element_by_xpath("/html/body/div[6]/div[2]/form/div[1]/div[1]/div[16]/div/div/input[1]").send_keys(Keys.END)
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

print("不通过的模块共有%d个" % bug_num)