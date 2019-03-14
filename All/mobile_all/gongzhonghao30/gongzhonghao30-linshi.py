from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
import time


def tishi( ts):
    root = Tk()
    li = [ts]
    ts = Listbox(root)
    for item in li:
        ts.insert(0, item)
    ts.pack()
    root.mainloop()

#登录操作
llq = webdriver.Firefox()
llq.get("https://mp.vdongchina.com")
llq.maximize_window()

llq.find_element_by_name("username").send_keys("微动销售中心")
llq.find_element_by_name("password").send_keys("Vdongchina")
tishi("在这里输入验证码，输入完成后，关闭该弹出框")
llq.find_element_by_id("submit").click()
#进入微动销售中心公众号
llq.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/a/div").click()
#进入大转盘应用
llq.find_element_by_link_text(u"大转盘").send_keys(Keys.ENTER)
#切换句柄到新打开的页面
time.sleep(3)
handles=llq.window_handles
print(handles)
llq.switch_to.window(handles[1])
handles=llq.window_handles
print(handles)
llq.switch_to.window(handles[1])
llq.close()

#下面是实验步骤
handles=llq.window_handles
print(handles)
llq.switch_to.window(handles[0])
llq.find_element_by_link_text(u"大转盘").send_keys(Keys.ENTER)