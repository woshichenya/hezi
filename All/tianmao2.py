from beifen import baibaoxiang, femail
import threading

email= femail.email
import time
url="https://detail.tmall.com/item.htm?id=586750895922&ut_sk=1.WS2NQGDD3RQDABrAF+sKkx4n_21380790_1551403955700.PanelQRCode.1&sourceType=item&price=199&suid=184110C6-48F2-46A7-AACA-D74A10C4C13D&un=11b7dc7b2f1a39340ece3c7aa15a835b&share_crt_v=1&sp_tk=77%20lTjNDeGJGQzQ5VzXvv6U=&cpp=1&shareurl=true&spm=a313p.22.28z.1013584011443&short_name=h.3w5o784&cv=N3CxbFC49W5&sm=4dff6f&app=firefox"
url2="https://www.tmall.com/?spm=a220o.1000855.a2226mz.1.25035819mQyNuy"








class b (threading.Thread):
    def __init__(self,jubing):
        threading.Thread.__init__(self)
        self.t=jubing

    def run(self):
        go = baibaoxiang.geturl(url2)
        go.Ctext("请登录", "请登录", "进入登录页面", "无法进入登录页面")
        go.llq.maximize_window()

        ss = 0
        while ss < 20:
            if go.llq.current_url == url2:
                break
            time.sleep(1)
        go.llq.get(url)
        while ss < 1000:
            # print("第",self.jubing,"个进程开始")
            try:
                jiaru = go.llq.find_elements_by_id("J_LinkBasket")
                for ii in jiaru:
                    print(ii.text)
                    if "加入购物车" in ii.text:
                        ii.click()
                        print("指定商品加入购物车成功")
                        # break
                        email("已抢购成功", "plain", "")

            except:
                go.llq.get(url)
            time.sleep(self.t)
            go.llq.get(url)



b(1).start()
b(0.3).start()


