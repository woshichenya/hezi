from selenium import webdriver
from pyvirtualdisplay import Display
import time
a = Display(visible=0, size=(800, 600))
a.start()
b = webdriver.ChromeOptions()
b.add_argument('--headless')
go = webdriver.Chrome(chrome_options=b)
# go.get("http://www.baidu.com")
# print(go.page_source)


wchen_vdong={
    "username":"vdongshops",
    "password":"1234567890",
}
url="http://sso.vdongchina.com"

def paizhao_pc(zhaopian_name):
    zhaopian_name = zhaopian_name
    a = "home\\chenya\\"
    b = ".png"
    Time = time.strftime("%Y-%m-%d--%H^%M^%S", time.localtime())
    png_name = a + Time + zhaopian_name + b
    go.get_screenshot_as_file(png_name)
    return png_name


go.get(url)
paizhao_pc("打开页面")
print(go.title)
print(go.current_url)
ho=wchen_vdong
try:
    sss = go.find_elements_by_tag_name("button")
    for ss in sss:
        print(ss.text)
        if "登录" in ss.text :
            ss.click()
            paizhao_pc("首开点击登录")
    k=go.find_element_by_id("inphoneinput")
    k.send_keys(ho["username"])
    # k.send_keys("ddd")
    paizhao_pc("输入用户名")
    print(go.find_element_by_id("inphoneinput").get_attribute("value"))
    go.find_element_by_id("pasword").send_keys(ho["password"])
    paizhao_pc("输入密码")
    print(go.find_element_by_id("pasword").get_attribute("value"))
    print(go.current_url)
    sss=go.find_elements_by_tag_name("button")
    print(len(sss))
    for ss in sss:
        print(ss.text)
        if "登录" in ss.text :
            ss.click()
            # paizhao_pc("点击登录")
            # ss.send_keys(Keys.ENTER)
    paizhao_pc("点击div登录")
except:
    print("无法正常登录")


# print(go.current_url)
go.get("https://xiao.vdongchina.com/web/index.php?c=index&a=wxapp&")
time.sleep(2)
paizhao_pc("点击登录两秒后")
go.refresh()
# print(go.page_source)
print(go.window_handles)
# go.switch_to.windo)
print(go.current_url)

go.quit()
a.stop()