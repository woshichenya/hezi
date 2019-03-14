import selenium_all.OLD.Zongheguanjia.ZongheguanjiaTest

go= selenium_all.OLD.Zongheguanjia.ZongheguanjiaTest.go
Go= selenium_all.OLD.Zongheguanjia.ZongheguanjiaTest.Go

def jinru():
    go.Cxpath("/html/body/div[2]/ul/li[2]/a/span","商品超链接","进入商品页面","Bug-无法点击商品超链接")
def tianjiashangping():
    go.Cxpath("/html/body/div[6]/div[2]/form/div/span/a[1]/i", "添加商品按钮", "进入添加商品页面", "Bug-无法进入添加商品页面")
    go.Sxpath("//input[@id='displayorder']", "排序输入框",  "101","输入排序中", "Bug-无法输入商品排序")
    go.Sxpath("//input[@id='goodsname']", "商品名输入框", "selenium自动手册", "输入商品名中", "Bug-无法输入商品名")
'''
添加商品


'''

jinru()
tianjiashangping()
try:
    Go.llq.find_element_by_link_text(" 实体商品")
    print("存在")
except:
    print(123)