import selenium_all.OLD.Zongheguanjia.ZongheguanjiaTest

go= selenium_all.OLD.Zongheguanjia.ZongheguanjiaTest.go
Go= selenium_all.OLD.Zongheguanjia.ZongheguanjiaTest.Go

def SPyemian():
    go.Cxpath("//i[@class='icow icow-goods']/..","商品超链接","进入商品管理页面","Bug--无法点击商品超链接")
def SPtianjia():
    go.Ctext("添加商品", "添加商品超链接", "进入添加商品页面", "Bug--无法点击添加商品按钮")
    go.Sxpath("//input[@id='displayorder']", "排序输入框", "101", "输入排序中", "Bug-无法输入商品排序")
    go.Sxpath("//input[@id='goodsname']", "商品名输入框", "selenium自动手册", "输入商品名中", "Bug-无法输入商品名")
    go.Sxpath("//textarea[@name='subtitle']","副标题输入框","这是自动键入的副标题，可能会有一些不同","输入副标题","Bug--无法输入副标题")
    go.Sxpath("//input[@name='shorttitle']", "商品短标题输入框", "这是自动键入的商品短标题", "输入商品短标题", "Bug--无法输入商品短标题")
    go.Sxpath("//input[@name='keywords']", "关键字输入框", "学习", "输入商品关键字", "Bug--无法输入商品关键字")
    go.Danxuan("type", "商品类型单选框", 0, "选中实体商品单选项", "Bug--没有选中实体商品单选项")
    go.Danxuan("ispresell","预售设置",0,"选中否定预售","Bug--无法选中是否预售")
    go.Sid("")
    Go.llq.find_element_by_id("marketprice").send_keys("123123")
    Go.llq.find_element_by_id("marketprice").clear()
    Go.llq.find_element_by_id("marketprice").send_keys("1")
    Go.llq.find_element_by_xpath("//div[@id='tab_basic']/div/div[2]/div[2]/div[11]/div").click()
    Go.llq.find_element_by_xpath("//button[@type='button']").click()
    Go.llq.find_element_by_xpath("//div[@id='image']/div/div[2]/div[8]").click()
    Go.llq.find_element_by_xpath("(//button[@type='button'])[6]").click()
    Go.llq.find_element_by_id("sales").click()
    Go.llq.find_element_by_id("sales").clear()
    Go.llq.find_element_by_id("sales").send_keys("100")
    Go.llq.find_element_by_xpath("//div[@id='tab_basic']/div/div[2]/div[2]/div[19]/label").click()
    Go.llq.find_element_by_xpath("//div[@id='tab_basic']/div/div[2]/div[2]/div[19]/div").click()
    Go.llq.find_element_by_name("showsales").click()
    Go.llq.find_element_by_xpath("(//input[@name='status'])[2]").click()
    Go.llq.find_element_by_link_text(u"库存/规格").click()
    Go.llq.find_element_by_id("total").click()
    Go.llq.find_element_by_id("total").clear()
    Go.llq.find_element_by_id("total").send_keys("1000")
    Go.llq.find_element_by_id("showtotal").click()






SPyemian()
SPtianjia()


'''
这里是备注区域
"","","","",""
ispresell
"type"
s2id_cates
'''
