from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import  time
import os

driver=webdriver.Firefox()

class Durl:
    d_url=0
    def D_url(self):
        Durl.d_url=driver.current_url

i=1
driver.get("http://39.107.239.18:5901/admin.php/user/publics/signin.html")
a=driver.find_element_by_id("login-username")
if a==1:
    print(1)
elif a==0:
    print(0)
driver.find_element_by_id("login-username").send_keys("admin")
driver.find_element_by_id("login-password").send_keys("vdongchina")
driver.find_element_by_xpath("//button[@type='submit']").click()
s="http://39.107.239.18:5901/admin.php/admin/index/index.html"
n="http://39.107.239.18:5901/admin.php/card/user/index.html"
Durl.D_url(1)
print("当前页面是：",Durl.d_url)
while Durl.d_url!=s:
    print("当前不是首页，等待第：",i,"秒")
    i +=1
    time.sleep(1)
    Durl.D_url(1)
i=1
while not driver.find_element_by_class_name("top-menu"):
    print("首页按钮不存在，等待第：",i,"秒")
    i += 1
    time.sleep(1)
i=1
driver.find_element_by_class_name("top-menu").click()
while not driver.find_element_by_xpath("//a[@class='active']"):
    print("后台首页按钮不存在，等待第：", i, "秒")
    i += 1
    time.sleep(1)
i=1
driver.find_element_by_xpath("//a[@class='active']").click()






