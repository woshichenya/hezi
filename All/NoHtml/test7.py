from selenium import webdriver
import time

wchen_vdong={
    "username":"vdongshops",
    "password":"1234567890",
}
url="http://sso.vdongchina.com"
go = webdriver.PhantomJS(executable_path='D:\job\software\phantomJs\phantomjs-2.1.1-windows\\bin\phantomjs.exe')#这里的executable_path填你phantomJS的路径
def paizhao_pc(zhaopian_name):
    zhaopian_name = zhaopian_name
    a = "D:\\img\\"
    b = ".png"
    Time = time.strftime("%Y-%m-%d--%H^%M^%S", time.localtime())
    png_name = a + Time + zhaopian_name + b
    go.get_screenshot_as_file(png_name)
    return png_name

go.get("https://xiao.vdongchina.com/web/index.php?c=index&a=wxapp&")
paizhao_pc("直接打开首页")
print(go.current_url)
go.get(url)
paizhao_pc("打开登录页")
print(go.current_url)

print(go.title)
print(go.current_url)
ho=wchen_vdong
sss=go.find_elements_by_tag_name("button")
for ss in sss:
    print(ss.text)
    if "登录" in ss.text :
        ss.click()
        paizhao_pc("点击登录0")
go.find_element_by_id("inphoneinput").clear()
go.find_element_by_id("inphoneinput").send_keys("3456")
sss=go.find_elements_by_tag_name("button")
for ss in sss:
    print(ss.text)
    if "登录" in ss.text :
        ss.click()
        paizhao_pc("点击登录1")
print(go.find_element_by_id("inphoneinput").get_attribute("value"))
print(go.find_element_by_id("inphoneinput").get_attribute("value"))
go.find_element_by_id("pasword").clear()
go.find_element_by_id("pasword").send_keys(ho["password"])
sss=go.find_elements_by_tag_name("button")
for ss in sss:
    print(ss.text)
    if "登录" in ss.text :
        ss.click()
        paizhao_pc("点击登录2")

sss=go.find_elements_by_tag_name("button")
for ss in sss:
    print(ss.text)
    if "登录" in ss.text :
        ss.click()
        paizhao_pc("点击登录3")
go.get("https://xiao.vdongchina.com/web/index.php?c=index&a=wxapp&")
paizhao_pc("登录打开首页")
print(go.current_url)


go.quit()