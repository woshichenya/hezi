import login.login
import time

login_go=login.login.Login()
go=login_go.on("china","wchen_vdong","","")

k_1=1
while k_1==1:

    i=1
    a=1
    for i in range (1,10):
        try:
            span_t=go.llq.find_elements_by_tag_name("span")
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
        time.sleep(1)
        if i%3==0 and a==1:
            go.CTag_name_zidingyi("p", "text", "切换小程序", "切换小程序超链接", "进入小程序列表", "Bug--无法切换至小程序列表")


    autogo =1
    for autogo in range (1,5):
        try:
            go.llq.find_element_by_id("autogo")
            time.sleep(3)
            go.llq.find_element_by_id("autogo").click()
            # break
        except:
            time.sleep(1)


#进入小程序
    go.lonely_applet_input("独立商城")

    go.Jubing_go(2,2)

    url_yes="https://xiao.vdongchina.com/addons/zjhj_mall/core/web/index.php?"
    url_1=1
    for url_1 in range (1,5):
        url_new=go.llq.current_url
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