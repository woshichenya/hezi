import guanjiaPlus.Test
import time
from python_all.SQL import sql

s= sql.sql()
'''
Go=guanjiaPlus.China.Go
go=guanjiaPlus.China.go
GO=guanjiaPlus.China.GO
'''
Go=guanjiaPlus.Test.Go
go=guanjiaPlus.Test.go
GO=guanjiaPlus.Test.GO

def jinru_kpi():
    go.Cxpath("/html/body/div[2]/div[2]/div/div[1]/ul/li[2]/div[2]/ul/li[2]","KPI设置超链接","进入KPI设置页面","Big--无法进入KPI设置页面")

def new_muban_qianti():
    go.Cxpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/span[2]/a", "查看考核模板按钮", "进入考核模板页面","Bug--无法进入考核模板页面")
def muban_qianti_new_html():
    go.Cxpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/span[2]/a","新建考核模板按钮","进入新建考核模板页面","Bug--无法进入新建考核模板页面")
def new_muban():
    a="考核模板"
    i = 18101801
    while i<=18101802:
        go.Sxpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div[1]/div[1]/div/input","考核模板名称",a+str(i),"输入考核模板名称","Bug--无法输入考核模板名称")
        #GO.llq.find_element_by_id("dropdownMenu3").find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div[1]/ul/li[1]/a").click()
        time.sleep(3)
        go.Cxpath("//*[@id='dropdownMenu3']","指标下拉框","展开指标选项","Bug--无法展开指标选项")
        go.Cxpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div[1]/ul/li[1]/a","销售额选项","选中销售额","Bug--无法选中销售额选项")
        text_a=GO.llq.find_element_by_id("dropdownMenu3").text
        print(text_a)


        go.Sxpath("//*[@id='valueAfter']","考核区间输入框",i,"输入考核区间","Bug--无法输入考核区间")
        go.Sxpath("//*[@id='valueAccount']","考核分数输入框","90","输入考核分数","Bug--无法输入考核分数")
        go.Cxpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div[3]/span[1]","添加区间按钮","添加区间","Bug--无法添加区间")
        go.Cxpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div[3]/input","保存考核模板按钮","保存考核模板","Bug--无法保存考核模板")
        i+=1
def del_muban():
    i=1
    while i<2:
        go.Cxpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/table/tbody/tr[4]/td[3]/span","第4个模板的删除按钮","删除第4个模板","么有第4个模板了")
        i+=1


def kaohe_new():
    #
    go.Cxpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/span[1]/a", "新建考核按钮", "进入新建考核页面","Bug--无法进入新建考核页面")
    time.sleep(2)
    a = "考核"
    i = 18101803
    while i <= 18101809:
        #//*[@id="dropdownMenu1"]
        go.Cxpath("//*[@id='dropdownMenu1']", "审核对象下拉框", "展开审核对象选项", "Bug--无法展开审核对象选项")
        #go.Cxpath("//*[@id='1']","西南区域总监", "选中西南区域总监", "Bug--无法选中西南区域总监选项")
        #//*[@id="1"]
        #go.Cxpath("//*[@id='1']", "华南区域总监", "选中华南区域总监", "Bug--无法选中华南区域总监选项")
        llq_dx_beikaoheren=GO.llq.find_elements_by_id("1")
        for ii in llq_dx_beikaoheren:
            ii.click()
        go.Sxpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div[1]/div[1]/div/input", "考核模板名称",a + str(i), "输入考核模板名称", "Bug--无法输入考核模板名称")
        # GO.llq.find_element_by_id("dropdownMenu3").find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div[1]/ul/li[1]/a").click()
        time.sleep(3)
        go.Cxpath("//*[@id='dropdownMenu3']", "指标下拉框", "展开指标选项", "Bug--无法展开指标选项")
        go.Cxpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div[1]/ul/li[1]/a","销售额选项", "选中销售额", "Bug--无法选中销售额选项")
        text_a = GO.llq.find_element_by_id("dropdownMenu3").text
        print(text_a)

        go.Sxpath("//*[@id='valueAfter']", "考核区间输入框", i, "输入考核区间", "Bug--无法输入考核区间")
        go.Sxpath("//*[@id='valueAccount']", "考核分数输入框", "90", "输入考核分数", "Bug--无法输入考核分数")
        go.Cxpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div[3]/span[1]","添加区间按钮", "添加区间", "Bug--无法添加区间")
        go.Cxpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div[3]/input", "保存考核按钮", "保存考核",
                  "Bug--无法保存考核")
        i += 1




GO.llq.quit()