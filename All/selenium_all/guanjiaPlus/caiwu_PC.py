from selenium.webdriver.support.select import Select
import traceback
from beifen import baibaoxiang
import time

GO= baibaoxiang.geturl
Go= baibaoxiang.geturl.llq
url="http://test-plus.vdongchina.com"
#url="http://plus.vdongchina.com"
go= baibaoxiang.geturl(url)
Go.maximize_window()
class Caiwu_pc:
    def login_shouye(self,username,userpsw):
        self.username=username
        self.userpsw=userpsw
        go.Cxpath("/html/body/div/div[1]/div[2]/div/a","转跳登录页按钮","转跳登录页中","Bug--无法转跳到登录页")
        go.Sxpath("//input[@name='username']","用户名输入框",self.username,"已经输入用户名","无法输入用户名")
        go.Sxpath("//input[@name='password']","密码输入框",self.userpsw,"已经输入密码","无法输入密码")
        go.Cxpath("//input[@id='submit']","登录按钮","登录中，等待页面转跳","登录失败")
    def denglurenxinxi_jc(self,name_dl):
        self.name_dl=name_dl
        try:
            aaa=Go.find_element_by_xpath("//a[@class='dropdown-toggle']").text
            if aaa==self.name_dl:
                print("登录信息正确，登录测试通过")
        except:
            aaa=1
            time.sleep(1)
        while aaa==1:
            try:
                aaa = Go.find_element_by_xpath("//a[@class='dropdown-toggle']").text
                print("登录信息正确，登录测试通过")
            except:
                time.sleep(1)
                aaa = 1
    def yebiaoqian_bug(self):
        go.Cxpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/ul/li[1]/a","直营管理超链接","转跳直营管理页面中...","Bug--无法转跳直营管理页面")
        go.Sxpath("/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/form/div/input","公司名称输入框","重庆江小白酒业有限责任公司","成功输入公司名称","Bug--无法输入")
        go.Cxpath("/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/form/div/span/button","公司搜索按钮","搜索中...","Bug--无法点击搜索功能")
        if Go.find_element_by_link_text("2"):
            print("bug测试未通过通过")
        else:
            print("bug测试通过")
    def zhiyingguanli_daochu(self):
        go.Cxpath("/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/div/a", "导入按钮","点击导入按钮...", "Bug--无法点击导入按钮")
        time.sleep(5)
        handles_all=Go.window_handles
        if len(handles_all)>1:
            print("多个句柄")
        else:
            print("单个句柄")
    def xinjian(self,denglu_zhanghao,denglu_mima,gongsi_name,gongsi_jiancheng,zizhanghao_denglu_mima,zhanghu_shuliang,gongzhonghao_shuliang,xiaochengxu_shuliang):
        self.denglu_zhanghao=denglu_zhanghao
        self.denglu_mima=denglu_mima
        self.gongsi_name=gongsi_name
        self.gongsi_jiancheng=gongsi_jiancheng
        self.zizhanghao_denglu_mima=zizhanghao_denglu_mima
        self.zhanghu_shuliang=zhanghu_shuliang
        self.gongzhonghao_shuliang=gongzhonghao_shuliang
        self.xiaochengxu_shuliang=xiaochengxu_shuliang
        go.Cxpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/ul/li[2]/a","代理商超链接","进入代理商页面","Bug--无法进入代理商页面")
        k=Go.find_elements_by_link_text("+新建")
        for i in k:
            print("这是文本",i.text)
            if i.text =="+新建":
                i.click()
                break
        go.Sxpath("//*[@id='username']","用户名输入框",self.denglu_zhanghao,"输入用户名","Bug--无法输入用户名")
        go.Sxpath("//*[@id='password']", "密码输入框", self.denglu_mima, "输入密码", "Bug--无法输入密码")
        go.Sxpath("//*[@id='repassword']", "确认密码输入框", self.denglu_mima, "输入确认密码", "Bug--无法输入确认密码")
        go.Sxpath("//*[@id='accountName']", "公司名称输入框", self.gongsi_name, "输入公司名称", "Bug--无法输入公司名称")
        go.Sxpath("//*[@id='company']", "公司简称输入框", self.gongsi_jiancheng, "输入公司简称", "Bug--无法输入公司简称")
        go.Sxpath("//*[@id='childrenPassword']", "子账号初始密码输入框", self.zizhanghao_denglu_mima, "输入子账号初始密码", "Bug--无法输入子账号初始密码")
        go.Sxpath("//*[@id='totalAccount']", "账户数量输入框", self.zhanghu_shuliang, "输入账户数量", "Bug--无法输入账户数量")
        go.Sxpath("//*[@id='publicAccount']", "绑定公众号商户数输入框", self.gongzhonghao_shuliang, "输入绑定公众号商户数", "Bug--无法输入绑定公众号商户数")
        go.Sxpath("//*[@id='smallAccount']", "绑定小程序商户数输入框", self.xiaochengxu_shuliang, "输入绑定小程序商户数", "Bug--无法输入绑定小程序商户数")
        try:
            Go.find_element_by_id("district").click()
            Go.find_element_by_name("reside[province]").click()
            Select(Go.find_element_by_name("reside[province]")).select_by_visible_text(u"辽宁省")
            Go.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='设置所属地区'])[2]/following::option[7]").click()
            Go.find_element_by_name("reside[city]").click()
            Select(Go.find_element_by_name("reside[city]")).select_by_visible_text(u"沈阳市")
            Go.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='设置所属地区'])[2]/following::option[38]").click()
            Go.find_element_by_name("reside[district]").click()
            Select(Go.find_element_by_name("reside[district]")).select_by_visible_text(u"沈河区")
            Go.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='设置所属地区'])[2]/following::option[54]").click()
            Go.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='设置所属地区'])[2]/following::button[1]").click()
        except Exception as e:
            ee=traceback.format_exc()
            print("设置区域出错，报错信息为：",ee)
        #submit
        go.Cxpath("//*[@id='submit']", "提交按钮",  "点击提交按钮", "Bug--无法点击提交按钮")
        time.sleep(5)
        try:
            aler=Go.switch_to_alert()
            time.sleep(2)
            print("提示信息：",aler.text)
            ass=1
        except:
            ass=2


        '''搜索新建的代理商'''
        go.Cxpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/ul/li[2]/a", "代理商超链接", "进入代理商页面","Bug--无法进入代理商页面")
        go.Sxpath("/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/form/div/input","搜索输入框",self.gongsi_name,"已输入公司名称","Bug--无法输入公司名称")
        go.Cxpath("/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/form/div/span/button","搜索按钮","点击搜索","Bug--无法点击搜索")
        try:

            if Go.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[4]").text == self.gongsi_name :
                print("公司名称正确")
                if Go.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[5]").text == self.denglu_zhanghao:
                    print("登录账户正确")
                    if Go.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[6]").text == self.zhanghu_shuliang :
                        print("账户数量正确")
                        print("新建完成")
        except Exception as e:
            ee=traceback.format_exc()
            print("报错信息",ee)





        '''
        go.Cid("date_demo1","日期控件","展开日期控件","Bug--无法展开日期控件")
        ss=Go.find_elements_by_link_text("21")
        print(ss)
        go.Cid("calendar_1537251943567_2018-8-1","日期2018-8-1","选择日期2018-8-1","Bug--无法选择日期2018-8-1")
        go.Cid("calendar_1537251943567_2018-9-30","日期2018-9-30","选择日期2018-9-30","Bug--无法选择日期2018-9-30")
        #calendar_1537251943567_2018 - 8 - 1
        #calendar_1537251943567_2018 - 8 - 1
        go.Cid("submit_1537251943567","确定按钮","提交选择日期","Bug--无法点击确认提交日期")
        '''



'''**************************************************************************执行方法*************************************************************************************'''
c=Caiwu_pc()
if url=="http://plus.vdongchina.com":
    c.login_shouye("vdong", "vdongchina2018")
if url=="http://test-plus.vdongchina.com":
    c.login_shouye("vdong","87654321")
c.denglurenxinxi_jc("vdong")
c.xinjian("python新建代理商","123456789","湖北自动化有限责任公司","hbzdh","123456789","12","23","34")