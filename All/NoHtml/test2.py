from selenium import webdriver
import time

wchen_vdong={
    "username":"vdongshops",
    "password":"1234567890",
}
url="http://sso.vdongchina.com"
go = webdriver.PhantomJS(executable_path='D:\job\software\phantomJs\phantomjs-2.1.1-windows\\bin\phantomjs.exe')#这里的executable_path填你phantomJS的路径
print(go.current_url)
go.get(url)

print(go.title)
print(go.current_url)
ho=wchen_vdong
go.find_element_by_id("inphoneinput").send_keys(ho["username"])
print(go.find_element_by_id("inphoneinput").get_attribute("value"))
go.find_element_by_id("pasword").send_keys(ho["password"])
sss=go.find_elements_by_tag_name("button")
for ss in sss:
    print(ss.text)
    if "登录" in ss.text :
        ss.click()

print(go.current_url)


# print(go.page_source)

k_1=1
while k_1==1:

    i=1
    a=1
    for i in range (1,10):
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
            break
        elif a==1:
            print("没有进入小程序页面")
            print(go.current_url)
        time.sleep(1)

    autogo =1
    for autogo in range (1,5):
        try:
            go.find_element_by_id("autogo")
            time.sleep(3)
            go.find_element_by_id("autogo").click()

            break
        except:
            time.sleep(1)

print(go.current_url)



url_yes="https://xiao.vdongchina.com/addons/zjhj_mall/core/web/index.php?"
url_1=1
for url_1 in range (1,5):
    url_new=go.current_url
    if url_yes in url_new:
        print("已进入独立商城首页")
        break

    # go.CTag_name_zidingyi("div","class","btn-group float-left","独立商城下拉框","展开独立商城下拉框","无法展开独立商城下拉框")
    # go.Ctext("返回系统","返回系统按钮","点击返回系统","无法点击返回系统")
    # go.Jubing_go(2,1)
    # go.llq.close()
    # go.Jubing_go(1,1)
    # print(go.llq.window_handles)
    # print(go.llq.current_window_handle)
    k_1 += 1

go.quit()
