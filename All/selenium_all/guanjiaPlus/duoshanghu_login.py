from beifen import baibaoxiang

GO= baibaoxiang.geturl
Go= baibaoxiang.geturl.llq
url="http://test-plus.vdongchina.com/web/merchant.php?c=site&a=entry&m=ewei_shopv2&do=web&r=login&i=248"
go= baibaoxiang.geturl(url)
Go.maximize_window()

go.Sxpath("//input[@name='username']","用户名输入框","testm1","已经输入用户名","无法输入用户名")
go.Sxpath("//input[@name='pwd']","密码输入框","123456789","已经输入密码","无法输入密码")
go.Cxpath("//input[@id='btn-login']","登录按钮","登录中，等待页面转跳","登录失败")



go.Cxpath("/html/body/div[2]/ul/li[3]/a/span","订单超链接","进入订单页面","Bu--无法进入订单页面")
'''
go.Cxpath("/html/body/div[3]/div/ul[1]/li/a","发货超链接","进入发货页面","Bu--无法进入发货页面")
go.Sxpath("/html/body/div[6]/div[2]/form/div/div/div/input","搜索条件",u"陈雅","成功输入姓名","Bug无法正常输入")
'''

