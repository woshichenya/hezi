import mobile_all.gongzhonghao30.Test

go= mobile_all.gongzhonghao30.Test.go
Go= mobile_all.gongzhonghao30.Test.Go
def jinrugongzhonghao():
    go.Ctext("公众号", "公众号超链接", "进入选择公众号页面中", "Bug-无法进入选择公众号页面")
    go.Cxpath("/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/a/div", "公众号产品中心5", "进入公众号", "Bug-无法进入公众号")

jinrugongzhonghao()