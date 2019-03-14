import guanjiaPlus.xiaochengxuguanliyemian
import time

'''调用进入小程序管理页面的脚本'''
go=guanjiaPlus.xiaochengxuguanliyemian.go
Go=guanjiaPlus.xiaochengxuguanliyemian.Go
GO=guanjiaPlus.xiaochengxuguanliyemian.GO

miaoshu="这是一个自动添加的商品分类，纯测试用分类，只在这次测试过程中使用，当脚本测试结束之后，本分类会被删除。"
miaoshu_g="这是一个自动添加的商品分类，纯测试用分类，只在这次测试过程中使用，当脚本测试结束之后，本分类会被删除--改。"
bug_num=0
def shangpin_home_go():
    go.CTextS("商品","商品超链接","进入商品页面","Bug--无法进入商品页面")
    go.CTextS("出售中","出售中超链接","进入出售中页面","Bug--无法进入出售中页面")

def shangpin_fenlei_go():
    go.CTextS("商品分类", "商品分类超链接", "进入商品分类页面", "Bug--无法进入商品分类页面")
    #x_text=Go.find_element_by_xpath("/html/body/div[6]/div[2]/form/div/ol/li[1]/div").text
    #print(x_text)



def shangpin_fenlei_new():
    go.CTextS("添加新分类", "添加商品分类按钮", "进入添加商品分类页面", "Bug--无法进入添加商品分类页面")
    #Go.find_element_by_name("displayorder").send_keys("输入的")
    go.Sname("displayorder","排序输入框","9999999","输入排序","Bug--无法输入排序")
    go.Sname("catename","分类名称","自动添加分类","输入商品分类","Bug--无法输入商品分类")
    go.Sname("description", "分类介绍", miaoshu, "输入商品分类描述", "Bug--无法输入商品分类描述")
    go.Cxpath("/html/body/div[6]/div[2]/form/div[5]/div/div[1]/span/button","选择图片插件","打开选择图片插件","Bug--无法打开选择图片插件")
    '''
    handers=go.Jubing()
    if handers>=3:
        print("这里有",handers,"个句柄")
    '''
    go.Cxpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[1]/div","第一张图片","点击第一张图片","Bug--无法点击第一张图片")
    go.Sid("advurl","分类广告链接","./index.php?i=1001&c=entry&m=ewei_shopv2&do=mobile","输入分类广告链接","Bug--无法输入分类广告链接")
    go.CClassNameS_danxuan("radio-inline","是","是_单选框","选择是","Bug--无法选择是")
    go.CTag_name("input","提交","提交按钮","点击提交按钮","Bug--无法点击提交按钮")

def shangpin_fenlei_updata():
    go.Cxpath("/html/body/div[6]/div[2]/form/div/ol/li[1]/div/span/a[1]/span/i","第一个商品分类的修改按钮","点击修改按钮","Bug--无法点击修改按钮")
    go.Sname("catename", "分类名称", "自动添加分类-改", "输入商品分类", "Bug--无法输入商品分类")
    go.Sname("description", "分类介绍", miaoshu_g, "输入商品分类描述", "Bug--无法输入商品分类描述")
    go.CTag_name("input", "提交", "提交按钮", "点击提交按钮", "Bug--无法点击提交按钮")


def shangpin_fenlei_delect():
    #/html/body/div[6]/div[2]/form/div/ol/li[1]/div/span/a[2]/span/i
    go.Cxpath("/html/body/div[6]/div[2]/form/div/ol/li[1]/div/span/a[2]/span/i", "第一个商品分类的删除按钮", "点击删除按钮","Bug--无法点击删除按钮")
    #go.CTextS("确 定","确定给删除按钮","点击确定删除按钮","Bug--无法点击确定删除按钮")
    go.Cxpath("/html/body/div[8]/div[2]/div/div/div/div/div[4]/button[1]","确定给删除按钮","点击确定删除按钮","Bug--无法点击确定删除按钮")


def shangpin_new():
    shangpin_home_go()
    go.CTextS("添加商品","添加商品按钮","进入添加商品页面","Bug--无法进入添加商品页面")
    go.Sxpath("//input[@id='displayorder']", "排序输入框", "99999", "输入排序中", "Bug-无法输入商品排序")
    go.Sxpath("//input[@id='goodsname']", "商品名输入框", "selenium自动手册", "输入商品名中", "Bug-无法输入商品名")
    #go.C_class_text("虚拟单选","label","radio-inline","虚拟商品","选择虚拟商品","Bug--无法选择虚拟商品")

    go.CClassNameS_danxuan("radio-inline","实体商品","实体商品单选框","点击实体商品单选框","Bug--无法点击实体商品单选框")
    go.Cid("s2id_autogen2","商品分类下拉框","展开商品分类下拉框","Bug--无法展开商品分类下拉框")
    #go.Cid("select2-result-label-12","上衣选项","选择上衣选项","Bug--无法选择上衣选项")
    go.CClassNameS_danxuan("select2-result-label","自动添加分类","商品分类-自动添加分类","选择商品分类-自动添加分类","Bug--无法选择商品分类-自动添加分类")
    go.CClassNameS_danxuan("checkbox-inline","推荐","推荐复选框","勾选推荐","Bug--无法勾选推荐")
    go.CClassNameS_danxuan("checkbox-inline", "新品", "新品复选框", "勾选新品", "Bug--无法勾选新品")
    go.CClassNameS_danxuan("checkbox-inline", "热卖", "热卖复选框", "勾选热卖", "Bug--无法勾选热卖")
    #go.CClassNameS_danxuan("checkbox-inline", "包邮", "包邮复选框", "勾选包邮", "Bug--无法勾选包邮")
    go.Sid("marketprice","价格","10","输入价格","Bug--无法输入价格")
    go.Sid("productprice", "原价", "101", "输入原价", "Bug--无法输入原价")
    go.Sid("costprice", "成本", "101", "输入成本", "Bug--无法输入成本")

    #go.CTextS("确定", "确定按钮", "点击确定按钮", "Bug--无法点击确定按钮")
    go.Sid("sales","已售出","10086","输入已售出数量","Bug--无法输入已售出数量")
    go.CClassNameS_danxuan("checkbox-inline", "正品保证", "正品保证复选框", "勾选正品保证", "Bug--无法勾选正品保证")
    go.CClassNameS_danxuan("radio-inline", "上架", "上架单选框", "勾选上架", "Bug--无法勾选上架")
    go.C_class_text("选择图片插件", "button", "btn btn-primary", "选择图片", "打开选择图片插件", "Bug--无法打开选择图片插件")
    # go.Cxpath("/html/body/div[5]/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[2]/div[15]/div/div[1]/span/button", "选择图片插件", "打开选择图片插件", "Bug--无法打开选择图片插件")
    go.Cxpath("/html/body/div[1]/div/div/div[2]/div[3]/div/div[1]/div", "第一张图片", "点击第一张图片", "Bug--无法点击第一张图片")
    go.C_class_text("确定按钮", "button", "btn btn-primary", "确定", "点击确定按钮", "Bug--无法点击确定按钮")

    #库存/规格
    go.CTextS_Key("库存/规格", "库存/规格超链接", "进入库存/规格模块", "Bug--无法进入库存/规格模块")
    go.Sid("weight","重量输入框","0.5","输入商品重量 ","Bug--无法输入商品重量")
    go.Sid("total","库存输入框","99999","输入库存 ","Bug--无法输入库存")
    go.Cid("showtotal","显示库存复选框","勾选显示库存","Bug--无法勾选显示库存")
    #btn btn-primary
    #go.C_class_text("保存按钮","button","btn btn-primary","保存商品","点击保存按钮","Bug--无法点击保存按钮")
    #/html/body/div[6]/div[2]/form/div[2]/div/input
    go.Cxpath("/html/body/div[6]/div[2]/form/div[2]/div/input","保存按钮","点击保存按钮","Bug--无法点击保存按钮")

def shangpin_sousuo():
    go.STag_name_zidingyi("input","placeholder","ID/名称/编号/条码/商户名称","selenium自动手册","搜索关键字输入框","输入关键字","Bug--无法输入关键字")
    go.CTag_name_zidingyi("button", "text", "搜索", "搜索按钮", "点击搜索按钮", "Bug--无法点击搜索按钮")

def shangpin_updata():
    go.Cxpath("/html/body/div[6]/div[2]/div[2]/div/table/tbody/tr/td[10]/a[1]/span/i", "编辑按钮", "点击编辑按钮", "Bug--无法点击编辑按钮")
    go.Sxpath("//input[@id='goodsname']", "商品名输入框", "selenium自动手册改", "输入商品名中", "Bug-无法输入商品名")
    #go.Cxpath("/html/body/div[6]/div[2]/form/div[2]/div/input", "保存按钮", "点击保存按钮", "Bug--无法点击保存按钮")
    #/html/body/div[5]/div[2]/form/div[2]/div/input
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
    go.llq.quit()
    print("***************************************************测试通过")
except:
    print("***************************************************商品测试过程之中有Bug")
    bug_num+=1