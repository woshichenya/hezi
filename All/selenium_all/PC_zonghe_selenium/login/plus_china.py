from beifen import baibaoxiang
import time
from selenium.webdriver.common.keys import Keys

GO= baibaoxiang.geturl
Go= baibaoxiang.geturl.llq
url="http://plus.vdongchina.com/"
go= baibaoxiang.geturl(url)
Go.maximize_window()
user_name="bosstao"
password="12345678"

go.CTextS("立即登录","转跳登录页按钮","转跳登录页中","Bug--无法转跳到登录页")
#go.Cxpath("/html/body/div/div[1]/div[2]/div/a","转跳登录页按钮","转跳登录页中","Bug--无法转跳到登录页")
go.Sxpath("//input[@name='username']","用户名输入框",user_name,"已经输入用户名","无法输入用户名")
go.Sxpath("//input[@name='password']","密码输入框",password,"已经输入密码","无法输入密码")
go.Cxpath("//input[@id='submit']","登录按钮","登录中，等待页面转跳","登录失败")

try:
    aaa=Go.find_element_by_xpath("//a[@class='dropdown-toggle']").text
    print("目前登录的人是：",aaa)
except:
    aaa=1
    time.sleep(1)
while aaa==1:
    try:
        aaa = Go.find_element_by_xpath("//a[@class='dropdown-toggle']").text
        print("目前登录的人是：", aaa)
    except:
        time.sleep(1)
        aaa = 1
if aaa==user_name:
    print("登录成功")


sss="/html/body/div/div[1]/div[2]/div/div/a[1]"
go.llq.find_element_by_xpath(sss).send_keys(Keys.END)
print ('将滚动条拉到底端')