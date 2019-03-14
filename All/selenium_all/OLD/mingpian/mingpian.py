import baibaoxiang

'''打开火狐浏览器和小名片的后台主页'''
go= baibaoxiang.geturl("http://39.107.239.18:5901/admin.php/user/publics/signin.html")
'''进行登录操作'''
go.Sxpath("//input[@id='login-username']","用户名输入框","admin","成功输入用户名","Bug无法输入用户名")
go.Sxpath("//input[@id='login-password']","密码输入框","vdongchina","成功输入密码","无法输入密码")
go.Cxpath("//button[@type='submit']","登录按钮","成功点击登录，等待转跳页面","Bug无法点击登录按钮")
'''转跳到名片管理的页面,这里要先对地址进行判断，避免发生点击而未转跳的现象'''
aurl="http://39.107.239.18:5901/admin.php/card/user/index.html"
burl= baibaoxiang.geturl.llq.current_url
while aurl!=burl:
    go.Cxpath("//header[@id='header-navbar']/ul[2]/li[6]","名片管理超链接","点击名片管理，等待转跳页面","Bug无法点击名片管理超链接")
    burl = baibaoxiang.geturl.llq.current_url

go.Cxpath("//div[@id='sidebar-menu']/ul/li[6]","活动管理超链接","点击活动管理，等待转跳页面","Bug无法点击活动管理超链接")