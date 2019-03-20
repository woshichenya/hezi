from beifen import baibaoxiang

go= baibaoxiang.geturl("http://test-sso-xiao.vdongchina.com/")
Go=go.llq


Go.maximize_window()
go.Sid("inphoneinput","用户名","testquanxian1","输入用户名","Bug--无法输入用户名")
go.Sid("pasword","密码","123456789","输入密码","Bug--无法输入密码")
go.CTag_name("button","登录","登录按钮","点击登录按钮","Bug--无法点击登录按钮")

#print(Go.find_element_by_class_name("manger-small").get_attribute("xpath"))

#'''开始进入公众号管理页面'''


'''
进入独立小程序管理页面

go.CClass("manger-small","管理小程序","进入小程序管理页面","Bug--无法进入小程序管理页面")


'''   '''
go.CText_partial_s("餐饮小程序","餐饮小程序超链接","进入餐饮管理页面","Bug--无法进入餐饮管理页面")
#go.CText_partial_s("门店列表","门店列表超链接","进入门店列表页面","Bug--无法进入门店列表页面")
#go.C_class_text("门店列表","li","list-group-item active","门店列表","进入门店列表","Bug--无法进入门店列表")
''''''
try:
    xt=Go.find_element_by_xpath("/html/body/div[1]/div[1]/span").text
except:
    xt="1"
while xt!="餐饮小程序":
    time.sleep(1)
    print("等")
    try:
        xt = Go.find_element_by_xpath("/html/body/div[1]/div[1]/span").text
    except:
        xt = "1"
aa = Go.find_elements_by_tag_name("li")
print("共", len(aa), "个", "li", "控件")
for a in aa:
    a_kw=a.get_attribute("kw")
    print(a_kw)
'''
#订单管理
'''
go.CText_partial_s("订单管理","订单管理超链接","进入订单管理页面","Bug--无法进入订单管理页面")
go.CText_partial_s("广告管理","广告管理超链接","进入广告管理页面","Bug--无法进入广告管理页面")
go.CText_partial_s("门店区域","门店区域超链接","进入门店区域页面","Bug--无法进入门店区域页面")
go.CText_partial_s("门店类型","门店类型超链接","进入门店类型页面","Bug--无法进入门店类型页面")
go.CText_partial_s("入驻管理","入驻管理超链接","进入入驻管理页面","Bug--无法进入入驻管理页面")
go.CText_partial_s("签到管理","签到管理超链接","进入签到管理页面","Bug--无法进入签到管理页面")
go.CText_partial_s("会员管理","会员管理超链接","进入会员管理页面","Bug--无法进入会员管理页面")
go.CText_partial_s("财务管理","财务管理超链接","进入财务管理页面","Bug--无法进入财务管理页面")
go.CText_partial_s("系统管理","系统管理超链接","进入系统管理页面","Bug--无法进入系统管理页面")
go.CText_partial_s("门店管理","门店管理超链接","进入门店管理页面","Bug--无法进入门店管理页面")


go.CTag_name_zidingyi("li","kw","门店列表","门店列表超链接","进入门店列表页面","Bug--无法进入门店列表页面")




'''
#添加门店
'''
go.CTextS("门店添加","添加门店按钮","点击添加门店","Bug--无法点击添加门店")
'''

''''''
#新建公众号
#go.CTag_name_zidingyi("p","text","创建公众号","创建公众号超链接","点击创建公众号","Bug--无法点击创建公众号")
go.CText_partial_s_key("切换公众号","切换公众号超链接","点击切换公众号","Bug--无法点击切换公众号")
go.CText_partial_s_key("创建公众号","创建公众号超链接","点击创建公众号","Bug--无法点击创建公众号")

cname=1811101
while cname<1811105 :
    go.Sname("cname","公众号名称",cname,"输入名称","无法输入名称")
    cname+=1
    go.Sname("account","公众号账号",cname,"输入账号","无法输入账号")
    go.CTag_name_zidingyi("input", "value", "下一步", "下一步超链接", "点击下一步", "Bug--无法点击下一步")
    go.CTag_name_zidingyi("a", "text", "返回公众号列表", "返回公众号列表超链接", "点击返回公众号列表", "Bug--无法返回公众号列表")
    #添加公众号
    go.CTag_name_zidingyi("a", "text", "添加公众号", "添加公众号超链接", "点击添加公众号", "Bug--无法点击添加公众号")
    #go.CTag_name_zidingyi("a", "text", "手动添加公众号", "手动添加公众号超链接", "点击手动添加公众号", "Bug--无法点击手动添加公众号")
    go.C_class_text("手动添加公众号超链接","a","btn btn-primary","手动添加公众号","点击手动添加公众号","Bug--无法点击手动添加公众号")


'''
go.CText_partial_s_key("创建小程序","创建小程序超链接","点击创建小程序","Bug--无法点击创建小程序")
cname=18110501
while cname<18110599 :
    go.Sname("cname", "小程序名称", cname, "输入小程序名称", "Bug--无法输入小程序名称")
    go.STag_name_zidingyi("input","placeholder","版本描述",cname,"小程序描述","输入小程序描述","Bug--无法输入小程序描述")
    go.STag_name_zidingyi("input", "placeholder", "版本描述", cname, "小程序描述", "输入小程序描述", "Bug--无法输入小程序描述")
    
'''
