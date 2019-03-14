import selenium_all.OLD.Zongheguanjia.ZongheguanjiaTest
'''执行进入应用页面'''
go= selenium_all.OLD.Zongheguanjia.ZongheguanjiaTest.go
Go= selenium_all.OLD.Zongheguanjia.ZongheguanjiaTest.Go
def Yingyonglan():
    go.Ctext("应用","应用超链接","进入应用页面中","Bug-无法进入应用页面")
    go.Cxpath("//div[@class='name namelist namelists text-over ng-binding']/../a/div","微动天下商城","进入应用中","Bug-无法进入应用")
    go.Cxpath("/html/body/div[2]/ul/li[9]/a","左侧应用栏","进入应用栏","Bug-无法进入应用栏")

Yingyonglan()