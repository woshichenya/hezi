import guanjiaPlus.Test


'''调用测试系统的登录脚本'''
go=guanjiaPlus.Test.go
Go=guanjiaPlus.Test.Go
GO=guanjiaPlus.Test.GO


'''进入多商户管理页面'''
Go.find_element_by_id("collapseListGroupHeading3").click()
Go.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='店铺'])[1]/following::li[1]").click()
Go.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='陈'])[3]/following::td[1]").click()

