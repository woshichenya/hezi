import selenium_all.jiankong502.login_china
import time
go=selenium_all.jiankong502.login_china.go


name_qun=['系统管理','小程序管理','商品管理','订单管理','用户管理','分销中心','内容管理','营销管理','应用专区','操作员管理','系统工具']
for name_qun_go in name_qun:
    go.Ctext(name_qun_go, name_qun_go + "菜单", "进入" + name_qun_go + "菜单", "无法进入" + name_qun_go + "菜单")
    # ss=go.llq.find_elements_by_tag_name("span")
    t_name = []
    ss=go.llq.find_elements_by_xpath("//div[@class = 'sidebar-content']/a/span")
    for sss in ss:
        name_n = sss.text
        if name_n !="":
            t_name.append(name_n)
    for name in t_name:

        if name != "":
            if name not in name_qun :
                go.Ctext(name,name+"菜单","进入"+name+"菜单","无法进入"+name+"菜单")
                time.sleep(2)
    t_name=[]




