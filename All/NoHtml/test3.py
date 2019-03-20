from selenium import webdriver
import time
from selenium.webdriver.common.keys import *

wchen_vdong={
    "username":"vdongshops",
    "password":"1234567890",
}
url="https://xiao.vdongchina.com/web/index.php?c=index&a=account&"
go = webdriver.PhantomJS(executable_path='D:\job\software\phantomJs\phantomjs-2.1.1-windows\\bin\phantomjs.exe')#这里的executable_path填你phantomJS的路径
print(go.current_url)
go.get(url)

print(go.title)
print(go.current_url)
ho=wchen_vdong
try:
    go.find_element_by_id("inphoneinput").send_keys(ho["username"])
    print(go.find_element_by_id("inphoneinput").get_attribute("value"))
    go.find_element_by_id("pasword").send_keys(ho["password"])
    print(go.find_element_by_id("pasword").get_attribute("value"))
    sss=go.find_elements_by_tag_name("button")
    print(len(sss))
    for ss in sss:
        print(ss.text)
        if "登录" in ss.text :
            ss.click()
            # ss.send_keys(Keys.ENTER)
    # go.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[6]/button").click()
    # go.find_element_by_xpath("/html/body/header/div/div/div/a").click()
except:
    print("无法正常登录")


print(go.current_url)

time.sleep(2)
go.refresh()
# print(go.page_source)
print(go.window_handles)
# go.switch_to.windo)
i=1
a=1

try:
    span_t=go.find_elements_by_tag_name("span")
    for x in span_t:
        if  "选择小程序" in x.text :
            a=2
            break
except Exception as e:
    print(e)

if a==2:
    print("进入小程序页面")
elif a==1:
    print("没有进入小程序页面")
    print(go.current_url)
time.sleep(1)

# autogo =1
# for autogo in range (1,5):
#     try:
#         go.find_element_by_id("autogo")
#         time.sleep(3)
#         go.find_element_by_id("autogo").click()
#
#         break
#     except:
#         time.sleep(1)

print(go.current_url)



go.quit()
