import baibaoxiang
import time

GO= baibaoxiang.geturl
Go= baibaoxiang.geturl.llq
url="http://test-plus.vdongchina.com"
go= baibaoxiang.geturl(url)
Go.maximize_window()

go.Cxpath("/html/body/div/div[1]/div[2]/div/a","转跳登录页按钮","转跳登录页中","Bug--无法转跳到登录页")
go.Sxpath("//input[@name='username']","用户名输入框","boss1808","已经输入用户名","Bug--无法输入用户名")
go.Sxpath("//input[@name='password']","密码输入框","123456789","已经输入密码","Bug--无法输入密码")
go.Cxpath("//input[@id='submit']","登录按钮","登录中，等待页面转跳","Bug--登录失败")
go.Cxpath("/html/body/div[2]/div[2]/div/div[1]/ul/li[4]/div[1]/h4","小程序列表","展开首页小程序列表","Bug--无法展开首页小程序列表")
go.Cxpath("/html/body/div[2]/div[2]/div/div[1]/ul/li[4]/div[2]/ul/li[1]","小程序概况列表","进入首页小程序概况列表","Bug--无法进入首页小程序概况列表")
go.Cxpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div[4]/div/table/tbody/tr[1]/td[7]/a","小程序管理按钮","进入小程序管理页面","Bug--无法进入小程序管理页面")
handles_all=Go.window_handles
while len(handles_all)<2:
    time.sleep(1)
    handles_all = Go.window_handles
if len(handles_all)==2:
    time.sleep(5)
    Go.switch_to.window(handles_all[1])



'''封装获取会员金额的方法'''
def huiyuanjine():
    go.Cxpath("/html/body/div[2]/ul/li[3]/a/span","会员列表","进入会员列表页面","Bug--无法进入会员列表页面")
    go.Sxpath("/html/body/div[6]/div[2]/form/div/div/input","搜索框","26378","成功输入会员编号","Bug--输入会员编号")
    go.Cxpath("/html/body/div[6]/div[2]/form/div/div/span[5]/button[1]","会员搜索按钮","点击会员搜索按钮","Bug--无法点击会员搜索按钮")
    time.sleep(3)
    huiyuanjines=Go.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div/table/tbody/tr/td[5]/span[2]/span").text
    return huiyuanjines


'''封装获取商品价格的方法'''
def shangpinjiage():
    go.Cxpath("/html/body/div[2]/ul/li[2]/a/span","商品超链接","进入商品页面","Bug--无法进入商品页面")
    names="冠琴手表男全自动机械表精钢防水男士手表真皮带男表镂空潮流腕表 钟表 白壳白面银网带"
    go.Sxpath("/html/body/div[6]/div[2]/form/div/div/input","搜索框",names,"成功输入商品名称","Bug--输入商品名称")
    go.Cxpath("/html/body/div[6]/div[2]/form/div/div/span[3]/button","商品搜索按钮","点击商品搜索按钮","Bug--无法点击商品搜索按钮")
    time.sleep(3)
    shangpinjiages=Go.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div/table/tbody/tr/td[5]/a").text
    return shangpinjiages



a=huiyuanjine()
a=float(a)
print(a)
b=shangpinjiage()
b=float(b)
print(b)
c=a-b
print(c)

baibaoxiang.geturl.tishi("123")
time.sleep(15)
d=huiyuanjine()
d=float(d)
if c==d:
    print("本次脚本执行正常")
if c!=d:
    print("本次执行失败")
print("剩余金额：",d)


