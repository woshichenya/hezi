import baibaoxiang
import time
import traceback

GO=baibaoxiang.geturl
Go= baibaoxiang.geturl.llq
#url="http://plus.vdongchina.com/"
url="http://test-plus.vdongchina.com"
go= baibaoxiang.geturl(url)
Go.maximize_window()


go.CTextS("体验demo","转跳登录页按钮","转跳登录页中","Bug--无法转跳到登录页")
url_new=Go.current_url
while url_new==url:
    print("还在首页，执行等待操作")
    time.sleep(1)
    url_new = Go.current_url
time.sleep(3)
kk={}
def xiagao():
    x=1
    while x<30:
        try:
            li=Go.find_elements_by_tag_name("a")
            for n in li:
                print(len(li),"个li控件")
                '''
                s=1
                a=Go.find_elements_by_tag_name("a")
                print("有", len(a), "个a标签")
                for i in a:
                    try:
                        if i in kk:
                            print("这个控件已经点过了")
                        if i not in kk:
                            print("第",s,"次")
                            print(i.get_attribute("value"))
                            i.click()
                            s+=1
                            try:
                                url_n=Go.find_element_by_partial_link_text("如果你的浏览器没有自动跳转，请点击此链接")
                                url_n.click()
                                kk.update[i]
                                print(kk)
                            except:
                                print("什么都么有发生")
                    except:
                        continue
                        s += 1


                s=1
                b=Go.find_elements_by_tag_name("button")
                print("有", len(b), "个button标签")
                for i in b:
                    try:
                        if i in kk:
                            print("这个控件已经点过了")
                        if i not in kk:
                            print("第",s, "次")
                            print(i.text)
                            i.click()
                            s += 1
                            try:
                                url_n=Go.find_element_by_partial_link_text("如果你的浏览器没有自动跳转，请点击此链接")
                                url_n.click()
                                kk.update[i]
                            except:
                                print("什么都么有发生")
                    except:
                        continue
                        s += 1
                '''

                try:
                    n.click()
                    print("点击")
                except:
                    print("不具备点击属性，调过")
                    continue
                try:
                    url_n = Go.find_element_by_partial_link_text("如果你的浏览器没有自动跳转，请点击此链接")
                    url_n.click()
                except:
                    ee=traceback.format_exc()
                    print(ee)
                    print("什么都么有发生")
        except Exception as e:
            ee=traceback.format_exc()
            print(ee)
            print("调过并等待3秒")
            time.sleep(3)
        x+=1


xiagao()