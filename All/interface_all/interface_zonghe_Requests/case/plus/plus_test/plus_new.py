import interface_all.interface_zonghe_Requests.baibaoxiang.baibaoxiangInterface
import re
import sql
import requests
import interface_all.interface_zonghe_Requests.baibaoxiang.excel_xlwt
import time
time_new=time.strftime("%Y%m%d%H%M%S",time.localtime())
'''通用模块'''
excel=interface_all.interface_zonghe_Requests.baibaoxiang.excel_xlwt.a()
sql_url="SELECT id FROM `plus_user_position` where `name` like '新添加的职位'"

sql_go=sql.sql()
roles="1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40"
# username="188715517741"
username="18871551001"
# username="18811021797"
# pas="123456"
pas="123456789"
# pas="123456abc"



#新增成员接口  这个是通用值
#登录接口切换，登录token实时获取



'''
通用方法
'''
go= interface_all.interface_zonghe_Requests.baibaoxiang.baibaoxiangInterface.go()
url_qian="http://test-plus.moliyan.com.cn"
shouji=go.shoujihao()
'''
登录接口
'''
login_interface="/api/index/login"#旧
# login_interface="https://test-sso.vdongchina.com/index/logincheck"
# data={
#     "account":username,
#     "password":pas
# }#旧
# data={
#     "username":username,
#     "password":pas
# }
headers={

}
# r=go.post(url_qian+login_interface,data,headers,"登录接口")
url_sso="https://test-sso.vdongchina.com/index/logincheck"
# url2="http://test-plus.moliyan.com.cn/api/index/login"
data={
    "username":"18871551001",
    "password":"1234567a"}
r=go.post(url_sso,data,headers,"sso登录接口")
k2=re.findall("\"wd_token\":\"(.*?)\"",r.text)
data={
    "wd_token":k2[0]
}
r=go.post(url_qian+login_interface,data,headers,"登录接口")
k=re.findall("\"token\":\"(.*?)\"",r.text)#旧
data["token"]=k[0]
#**************************************************    User  接口   **********************************************
def user_go():

    '''
    User - 上传头像接口
    '''
    login_interface="/api/user/uploadheadurl"
    data={
         # "headpic":"G:\工作文件\截图\1.jpg",#头像文件
    }
    l = {
        "headpic": open("G:\\工作文件\\截图\\1.jpg", "rb")
    }
    data["token"]=k[0]
    headers={

    }
    kk = requests.post(url_qian + login_interface, data=data, files=l)
    if "\"msg\":\"ok\"" in kk.text and kk.status_code == 200:
        print("User - 上传头像接口成功")
        print(kk.json())


    '''
    User - 个人信息编辑接口
    '''
    login_interface="/api/user/edit"
    data={
        "username":"陈雅",#姓名
        "avatar":"/Uploads/2019-01-09/5c359b96cf9f0.jpg",#头像(不带域名)
    }
    data["token"]=k[0]
    headers={
    }
    r=go.post(url_qian+login_interface,data,headers,"User - 个人信息编辑接口")


    '''
    User - 修改密码接口
    '''
    login_interface="/api/user/edit"
    data={
        "new_password":"123456789",#新密码
        "password":"12456789",#旧密码
    }
    data["token"]=k[0]
    headers={
    }
    r=go.post(url_qian+login_interface,data,headers,"User - 修改密码接口")


    '''
    User - 忘记密码接口
    '''
    login_interface="/api/index/forgetpass"
    data={
        "mobile":username,#账号
        "password":"123456",#新密码
        "code":"1234",#验证码
    }
    data["token"]=k[0]
    headers={
    }
    r=go.post(url_qian+login_interface,data,headers,"User - 忘记密码接口")


    '''
    USER-成员列表 职位select 接口
    '''
    login_interface="/api/group/getpositionList"
    data={

    }
    data["token"]=k[0]
    headers={

    }
    r=go.post(url_qian+login_interface,data,headers,"USER-成员列表 职位select 接口")


    '''
    User - 注册接口
    '''
    login_interface="/api/index/register"
    data={
        "mobile":"188715517742",#账号
        "password":"123456",#新密码
        "code":"1234",#验证码
    }
    data["token"]=k[0]
    headers={
    }
    r=go.post(url_qian+login_interface,data,headers,"User - 注册接口")



    '''
    User - 组织构架接口
    '''
    login_interface="/api/user/organization"
    data={
    }
    data["token"]=k[0]
    headers={
    }
    r=go.post(url_qian+login_interface,data,headers,"User - 组织构架接口")
user_go()

#**************************************************    Group  接口   **********************************************
def group_go():
    '''
    Group  - 上传头像接口
    '''
    login_interface = "/api/group/Saveheadurl"
    # files={'files':open("G:\\工作文件\\截图\\1wheel.png","rb")}
    data = {
        "headpic": open("G:\\工作文件\\截图\\1wheel.png", "rb")#头像文件
    }
    data["token"] = k[0]
    headers = {

    }
    # requests.post(url_qian+login_interface,data=data,)
    r = go.post(url_qian + login_interface, data, headers, "User - 上传头像接口")


    '''
    Group - 修改成员接口
    '''
    login_interface="/api/group/edituser"
    data={
        "account":"18100000070",
        "group_user_id": "1059",  # 被修改用户id
        "headpic": "/Uploads/2019-01-25/5c4ab7294a7e7.jpg",  # 头像
        "pid": "1016",  # 所属上级
        "position_id": "163",  # 职位
        "remark": "group修改的简介",  # 职位简介
        "name": "group修改的名称",  # 姓名
        "province": "湖北",  # 省
        "city": "襄阳",  # 市
    }
    data["token"]=k[0]
    headers={

    }
    r=go.post(url_qian+login_interface,data,headers,"Group - 修改成员接口")


    '''
    Group - 修改用户状态接口
    '''
    login_interface="/api/group/Setstatus"
    data={
        "group_user_id":"1058",#修改用户user_id
        "status":"2",#状态值 status
    }
    data["token"]=k[0]
    headers={

    }
    r=go.post(url_qian+login_interface,data,headers,"Group - 修改用户状态接口")


    '''
    Group - 删除成员接口
    '''
    login_interface="/api/group/deluser"
    data={
        "del_group_userid":"1062",#用户user_id
    }
    data["token"]=k[0]
    headers={

    }
    r=go.post(url_qian+login_interface,data,headers,"Group - 删除成员接口")


    '''
    GROUP-成员列表 职位select 接口
    '''
    login_interface="/api/group/edit"
    data={

    }
    data["token"]=k[0]
    headers={

    }
    r=go.post(url_qian+login_interface,data,headers,"GROUP-成员列表 职位select 接口")




    '''
    Group - 换绑删除接口
    '''
    login_interface="/api/group/Transferdel"
    data={
        "group_user_id":"",#删除用户user_id
        "new_superior":"",#转绑用户 user_id
    }
    data["token"]=k[0]
    headers={

    }
    r=go.post(url_qian+login_interface,data,headers,"Group - 换绑删除接口")



    '''
    Group - 新增成员接口
    '''
    login_interface="/api/group/adduser"
    user_name="临时账号"+str(shouji)
    data={
        "account":shouji,#登录账号
        "password":"123456789",#密码
        "pid":"1016",#所属上级
        "position_id":"163",#职位
        "remark":"测试账号",#职位简介
        "name":user_name,#姓名
        "province":"北京市",#省
        "city":"北京市",#市
        "district":"",#县
    }
    data["token"]=k[0]
    headers={

    }
    r=go.post(url_qian+login_interface,data,headers,"Group - 新增成员接口")




    '''
    Group - 组员列表接口
    '''
    login_interface="/api/group/userlist"
    data={
        "size":"20",#一页获取多少条数
        "page":"1",#页码
        "position_id":"1",#角色id
        "status":"1",#状态值
    }
    data["token"]=k[0]
    headers={

    }
    r=go.post(url_qian+login_interface,data,headers,"Group - 组员列表接口")



    '''
    Group - 获取成员接口
    '''
    login_interface="/api/group/getuser"
    data={
        "group_user_id":"1016",#用户user_id
    }
    data["token"]=k[0]
    headers={

    }
    r=go.post(url_qian+login_interface,data,headers,"Group - 获取成员接口")
# group_go()

#**************************************************    Biasic  接口   **********************************************
def biasic_go():
    '''
    Biasic - 概况用户信息
    '''
    login_interface = "/api/basic/getuserinfo"
    data = {
    }
    data["token"] = k[0]
    headers = {

    }
    r = go.post(url_qian + login_interface, data, headers, "Biasic - 概况用户信息")

    '''
    Biasic - 概况销售额类别占比
    '''
    login_interface = "/api/basic/getcategorycount"
    data = {
        "type":"0",#类型 0全部 1小程序 2公众号
        "date":"2019-01-01~2019-01-07"#日期时间段 格式xxxx-xx-xx~xxxx-xx-xx
    }
    data["token"] = k[0]
    headers = {

    }
    r = go.post(url_qian + login_interface, data, headers, "Biasic - 概况销售额类别占比")
biasic_go()


#**************************************************    Display  接口   **********************************************
def display_go():
    '''
    Display - 数据看板->交易概况
    '''
    login_interface = "/api/Display/Year"
    data = {
        "year": "",#年份 默认当前时间年份
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Display - 数据看板->交易概况")

    '''
    Display - 数据看板->实时数据
    '''
    login_interface = "/api/Display/Realtime"
    data = {
        "type": "",#店铺类型 1小程序 2公众号
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Display - 数据看板->实时数据")

    '''
    Display - 数据看板->访问路径
    '''
    login_interface = "/api/Display/Viewpath"
    data = {
        "date":"2019-01-01~2019-01-07",#时间段
        "type":"0",#1小程序 2公众号 0全部
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Display - 数据看板->实时数据")



    '''
    Display - 数据看板->转化详情(门店列表)
    '''
    login_interface = "/api/Display/Payrate"
    data = {
        "date": "2019-01-01~2019-01-07",  # 时间段 xxxx-xx-xx~xxxx-xx-xx
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Display - 数据看板->转化详情(门店列表)")


    '''
    Display - 数据看板->转化详情(门店图表)
    '''
    login_interface = "/api/Display/Paytable"
    data = {
        "date": "2019-01-01~2019-01-07",  # 时间段 xxxx-xx-xx~xxxx-xx-xx
        "type": "1",  # 店铺类型 1小程序 2公众号
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Display - 数据看板->转化详情(门店图表)")

    '''
    Display - 数据看板->销售额走势
    '''
    login_interface = "/api/Display/Saletable"
    data = {
        "date": "2019-01-01~2019-01-10",  # 时间段 xxxx-xx-xx~xxxx-xx-xx
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Display - 数据看板->销售额走势")

    '''
       Display - 数据看板->门店销售额top10
       '''
    login_interface = "/api/Display/Salerank"
    data = {
        "date": "2019-01-01~2019-01-07",  # 时间段
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Display - 数据看板->门店销售额top10")
display_go()


#**************************************************    公众号  接口   **********************************************
def gzh_go():
    '''
    公众号图文分析->图文来源分析接口
    '''
    login_interface="/api/gzh/articlereadchannel"
    data={
        "date":"2019-01-01~2019-01-07",#日期时间段 格式xxxx-xx-xx~xxxx-xx-xx
        "uniacid ":"",#公众号唯一值,如果uniacid值不传则使用当前用户的所有公众号
    }
    data["token"]=k[0]
    headers={

    }
    #{host}/api/gzh/articlereadchannel?date=2018-12-01~2018-12-12&uniacid=10
    r=go.post(url_qian+login_interface,data,headers,"公众号图文分析->图文来源分析接口")



    '''
    公众号图文分析->昨日关键指标接口
    
    '''
    login_interface="/api/gzh/articleyesterdayindex"
    data={
        "uniacid ":"",#公众号唯一值,如果uniacid值不传则使用当前用户的所有公众号
    }
    data["token"]=k[0]
    headers={

    }
    r=go.post(url_qian+login_interface,data,headers,"公众号图文分析->昨日关键指标接口")



    '''
    公众号图文分析->趋势分析接口
    '''
    login_interface="/api/gzh/articletrendanalysis"
    data={
        "uniacid ":"",#公众号唯一值,如果uniacid值不传则使用当前用户的所有公众号
        "date":"2019-01-01~2019-01-07",#日期时间段 格式xxxx-xx-xx~xxxx-xx-xx
        "compare_date ":"2019-01-01~2019-01-07",#日期时间段 格式xxxx-xx-xx~xxxx-xx-xx
    }
    data["token"]=k[0]
    headers={

    }
    r=go.post(url_qian+login_interface,data,headers,"公众号图文分析->趋势分析接口")



    '''
    公众号图文页-》列表接口
    '''
    login_interface="/api/gzh/articlegzhlist"
    data={
        "uniacid": "",#公众号唯一值,如果uniacid值不传则使用当前用户的所有公众号
        "order": "",#int_page_read,send_article,cumulate_user
        "sort": "",#asc, desc
        "page": "",#页码
        "size": "",#返回数量
    }
    data["token"]=k[0]
    headers={

    }
    r=go.post(url_qian+login_interface,data,headers,"公众号图文页-》列表接口")



    '''
    公众号概况页-》列表接口
    '''
    login_interface = "/api/gzh/gzhlist"
    data = {
        "uniacid": "",#公众号唯一值,如果uniacid值不传则使用当前用户的所有公众号
        "order": "",#int_page_read,send_article,cumulate_user
        "sort": "",#asc, desc
        "page": "",#页码
        "size": "",#返回数量
    }
    data["token"] = k[0]
    headers = {

    }
    r = go.post(url_qian + login_interface, data, headers, "公众号概况页-》列表接口")


    '''
    公众号详情->昨日关键指标接口
    '''
    login_interface = "/api/gzh/yesterdayindex"
    data = {
        "uniacid": "",#公众号唯一值,如果uniacid值不传则使用当前用户的所有公众号
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "公众号详情->昨日关键指标接口")


    '''
    公众号详情->趋势分析接口
    '''
    login_interface = "/api/gzh/trendanalysis"
    data = {
        "uniacid": "",
        "date": "2019-01-01~2019-01-07",#日期时间段 格式xxxx-xx-xx~xxxx-xx-xx
        "compare_date ": "",#日期时间段 格式xxxx-xx-xx~xxxx-xx-xx
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "公众号详情->趋势分析接口")
    #{host}/api/gzh/trendanalysis?date=2018-12-01~2018-12-12
    #{host}/api/gzh/trendanalysis?date=2018-12-01~2018-12-05&compare_date=2018-12-01~2018-12-05
gzh_go()


#**************************************************    shop  接口   **********************************************
def shop_go():
    '''
    Shop - 交易分析-》交易分布
    '''
    login_interface = "/api/trade/province"
    data = {
        "uniacid":"",#公众号唯一值,如果uniacid值不传则使用当前用户的所有公众号
        "type":"",#店铺类型 1小程序店 2公众号店 不传获取所有类型的店
        "order":"",#sale_price, pay_person_sum, visit_sum,
        "sort":"",#1 asc,2 desc
        "page":"",#页码
        "size":"",#返回数量
        "date":"2019-01-01~2019-01-07",#日期时间段 格式xxxx-xx-xx~xxxx-xx-xx 或者 xxxx-xx-xx
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Display - 交易分析->交易分布")




    '''
    Shop - 交易分析-》交易构成
    '''
    login_interface = "/api/trade/Salefrom"
    data = {
        "uniacid":"",#公众号唯一值,如果uniacid值不传则使用当前用户的所有公众号
        "date":"2019-01-01~2019-01-07",#日期时间段 格式xxxx-xx-xx~xxxx-xx-xx 或者 xxxx-xx-xx
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Display - 数据看板->交易构成")



    '''
    Shop - 公众号店铺 小程序店铺概览
    '''
    login_interface = "/api/shop/Uniacidview"
    data = {
        "uniacid": "1",  # 公众号唯一值
        "type": "1",  # 店铺类型 1小程序店 2公众号店
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Shop - 公众号店铺 小程序店铺概览")



    '''
    Shop - 商品排行榜
    '''
    login_interface = "/api/shop/goodsrank"
    data = {
        "uniacid":"",#公众号唯一值,如果uniacid值不传则使用当前用户的所有公众号
        "type":"",#店铺类型 1小程序店 2公众号店 不传获取所有类型的店
        "order":"sales_price",#good_lv,pay_person_sum,visit_person_sum,sales_price
        "sort":"desc",#asc, desc
        "page":"1",#页码
        "size":"10",#返回数量
        "date":"2019-01-01~2019-01-10",#日期时间段 格式xxxx-xx-xx~xxxx-xx-xx
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Shop - 商品排行榜")
    # print(r.text)
    phb1=re.findall("\"sales_price\":\"(.*?)\"",r.text)
    phb2=re.findall("{\"good_id\":\"(.*?)\"",r.text)
    no_one_jiekou=float(phb1[0])
    no_one_goodsid=phb2[0]
    print(no_one_goodsid)
    print(no_one_jiekou)
    sql="SELECT SUM(pay_price) FROM plus2test_off.plus_middle_shop_order_goods where goodsid = '"+no_one_goodsid+"'"
    paihangbang_no_one_price_all=sql_go.lianjie_sql("plus2test", sql)
    no_one_sql=float(paihangbang_no_one_price_all[0][0])
    if no_one_jiekou == no_one_sql:
        print("第一名的销售额一致，可执行下一步测试")
    else:
        print("第一名的销售额两者不一致*****************************************************************")
        print("接口是：",no_one_jiekou)
        print("数据库是：",no_one_sql)
    #{host}/api/shop/goodsrank?date=2018-12-01~2018-12-18&token=&page=1&order=sales_price&sort=1&size=10



    '''
    Shop - 商品概况
    '''
    login_interface = "/api/shop/goodssketch"
    data = {
        "uniacid": "",  # 公众号唯一值,如果uniacid值不传则使用当前用户的所有公众号
        "type": "",  # 店铺类型 1小程序店 2公众号店 不传获取所有类型的店
        "date": "2018-01-01~2019-01-07",  # 日期时间段 格式xxxx-xx-xx~xxxx-xx-xx
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Shop - 商品概况")
    #{host}/api/shop/goodssketch?date=2018-11~2018-12&token=



    '''
    Shop - 商品趋势分析
    '''
    login_interface = "/api/shop/getgoodvisits"
    data = {
        "uniacid":"",#公众号唯一值,如果uniacid值不传则使用当前用户的所有公众号
        "type":"",#店铺类型 1小程序店 2公众号店 不传获取所有类型的店
        "fields":"",#goods_sum,new_goods_sum,visit_goods_sum,visit_goods_member_sum,visit_goods_show_sum,sale_prices,pay_person_sum,visit_pay_lv
        "date":"2019-01-01~2019-01-07",#日期时间段 格式xxxx-xx-xx~xxxx-xx-xx
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Shop - 商品趋势分析")
    # {host}/api/shop/goodssketch?date=2018-11~2018-12&token=



    '''
    Shop - 店铺
    '''
    login_interface = "/api/shop/list"
    data = {
        "uniacid":"",#公众号唯一值,如果uniacid值不传则使用当前用户的所有公众号
        "type":"",#店铺类型 1小程序店 2公众号店 不传获取所有类型的店
        "date":"2019-01-01~2019-01-07",#日期时间段 格式xxxx-xx-xx~xxxx-xx-xx
        "order":"",#排序字段
        "sort":"",#排序类型 asc , desc
        "size":"",#长度
        "page":"",#页码
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Shop - 店铺")




    '''
    Shop - 店铺实时数据
    '''
    login_interface = "/api/shop/shopcountinfo"
    data = {
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Shop - 店铺实时数据")




    '''
    Shop - 店铺概览 销售额趋势

    '''
    login_interface = "/api/shop/Tablerange"
    data = {
        "uniacid": "",  # 公众号唯一值,如果uniacid值不传则使用当前用户的所有公众号
        "type": "",  # 店铺类型 1小程序店 2公众号店 不传获取所有类型的店
        "date": "2019-01-01~2019-01-07",  # 日期时间段 格式xxxx-xx-xx~xxxx-xx-xx 或者 xxxx-xx~xxxx-xx
        "date_type": "",  # 日期统计格式 1按天 2按月（按月date字段传递xxxx-xx~xxxx-xx）
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Shop - 店铺概览 销售额趋势")



    '''
    Shop - 店铺概览 销售额趋势時間對比
    '''
    login_interface = "/api/shop/Tablecompare"
    data = {
        "uniacid": "",  # 公众号唯一值,如果uniacid值不传则使用当前用户的所有公众号
        "type": "",  # 店铺类型 1小程序店 2公众号店 不传获取所有类型的店
        "date": "2019-01-01~2019-01-07",  # 日期时间段 格式xxxx-xx-xx~xxxx-xx-xx 或者 xxxx-xx~xxxx-xx
        "compare_date": "2019-01-01~2019-01-07",  #  	日期时间段 格式xxxx-xx-xx~xxxx-xx-xx 或者 xxxx-xx~xxxx-xx
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Shop - 店铺概览 销售额趋势時間對比")



    '''
    Shop - 店铺详情
    '''
    login_interface = "/api/shop/info"
    data = {
        "uniacid": "",  # 公众号唯一值,如果uniacid值不传则使用当前用户的所有公众号
        "type": "",  # 店铺类型 1小程序店 2公众号店 不传获取所有类型的店
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Shop - 店铺详情")



    '''
    Shop - 概览
    '''
    login_interface = "/api/shop/Overview"
    data = {
        "type": "",  # 店铺类型 1小程序店 2公众号店 不传获取所有类型的店
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Shop - 概览")
shop_go()

#**************************************************    Store  接口   **********************************************
def store_go():
    '''
    Store - 添加门店接口
    '''
    login_interface = "/api/store/add"
    shouji=go.shoujihao()
    data = {
        "account":shouji,#账号
        "password":"123456789",#密码
        "name":"临时门店2",#门店名称
        "province":"北京",#省
        "city":"北京市",#市
        "address":"路边左拐",#详细地址
        "user_id":"1078",#绑定用户user_id
        "headpic":"https://test-plus.moliyan.com.cn/Uploads/2019-01-09/5c359b96cf9f0.jpg",#头像
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Store - 添加门店接口")


    '''
    Store - 门店修改接口
    '''
    sql_mendian_id_url = "SELECT id FROM `plus_store` WHERE account = '" + str(shouji) + "'"
    mendian_id = sql_go.lianjie_sql("plus2test", sql_mendian_id_url)
    login_interface = "/api/store/info"
    data = {
        "id":mendian_id[0],#门店id
        "account":shouji,#账号
        "password":"123456789",#密码
        "province":"湖北",#省
        "city":"襄阳",#市
        "address":"路边",#详细地址
        "user_id":"",#绑定用户user_id
        "headpic":"https://test-plus.moliyan.com.cn/Uploads/2019-01-09/5c359b96cf9f0.jpg",#头像
    }
    print("看这里",mendian_id[0])
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Store - 门店修改接口")

    '''
    Store - 门店列表接口
    '''
    login_interface = "/api/store/list"
    data = {
        "pageid ": "1",  # 分页id
        "size ": "1",  # 分页
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Store - 门店列表接口")

    '''
    Store - 门店绑定接口
    '''
    login_interface = "/api/store/bind"
    data = {
        "account":"18871551774",#账号
        "password":"123456789",#密码
        "name":"第一个4.0门店",#门店名称
        "province":"北京",#省
        "city":"北京",#市
        "address":"路边右转",#详细地址
        "user_id":"1067",#绑定用户user_id
        "headpic":"https://test-plus.moliyan.com.cn/Uploads/2019-01-09/5c359b96cf9f0.jpg",#头像
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Store - 门店绑定接口")

    '''
    Store - 门店删除接口
    '''

    login_interface = "/api/store/delete"
    data = {
        "id":mendian_id[0],
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Store - 门店删除接口")
store_go()

#**************************************************    UserPosition  接口   *******************************************
def userposition_go():




    '''
    UserPosition - 添加职位接口
    '''
    login_interface = "/api/userposition/add"
    data = {
        "name": "新添加的职位",  # 职位名称
        "roles":roles,  # 权限列表
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "UserPosition - 添加职位接口")
    # {host}/api/userposition/add?name=测试角色&roles=1,2,3,4,5

    zhiwei_id = sql_go.lianjie_sql("plus2test", sql_url)


    '''
    UserPosition - 用户编辑、修改、删除的职位选择接口
    '''
    login_interface = "/api/userposition/getcuruserall"
    data = {
        "is_show_users": "",  # 是否返回职位下的所有用户,默认为0
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "UserPosition - 用户编辑、修改、删除的职位选择接口")
    # {host}/api/userposition/getcuruserall


    '''
    UserPosition - 职位修改接口
    '''
    zhiwei_name="新添加的职位"+time_new
    login_interface = "/api/userposition/save"
    data = {
        "id":zhiwei_id,#职位ID
        "name":zhiwei_name,#职位名称
        "roles":roles,#权限列表
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "UserPosition - 职位修改接口")
    #{host}/api/userposition/save?name=测试角色&roles=1,2,3,4,5&id=1



    '''
    UserPosition - 职位列表接口
    '''
    login_interface = "/api/userposition/list"
    data = {
        "pageid":"1",#分页id
        "size":"1",#分页
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "UserPosition - 职位列表接口")
    #{host}/api/userposition/list


    '''
    UserPosition - 获取职位详情接口
    '''
    login_interface = "/api/userposition/getinfo"
    data = {
        "id": zhiwei_id,  # 职位id
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "UserPosition - 获取职位详情接口")
    # {host}/api/userposition/getinfo?id=1

    '''
    UserPosition - 删除职位接口
    '''
    login_interface = "/api/userposition/delete"
    data = {
        "id": zhiwei_id,  # 职位ID
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "UserPosition - 删除职位接口")
    # {host}/api/userposition/delete?id=2
userposition_go()
#OK

#**************************************************    Xiao   接口   *******************************************
def xiao_go():
    '''
    Xiao - 用户同步微尘公众号小程序及店铺刷新接口
    '''
    login_interface = "/api/xiao/refreshsync"
    data = {
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "Xiao - 用户同步微尘公众号小程序及店铺刷新接口")
xiao_go()

#**************************************************    company   接口   *******************************************
def company_go():
    '''
    company - 公司设置详情接口
    '''
    login_interface = "/api/company/edit"
    data = {
        "name": "",  # 公司名称
        "remark": "",  # 公司简介
        "province": "",  # 省
        "city": "",  # 市
        "district": "",  # 区
        "address": "",  # 街道地址
        "tel": "",  # 联系电话
        "headpic": "",  # 公司头像
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "company - 公司设置详情接口")


    '''
    company - 公司详情接口
    '''
    login_interface = "/api/company/info"
    data = {
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "company - 公司详情接口")
company_go()


#**************************************************    wxapp    接口   *******************************************
def wxapp_go():

    '''
    wxapp - 小程序信息
    '''
    login_interface = "/api/wxapp/info"
    data = {
        "wxapp_uniacid": "",  #  小程序id
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "wxapp - 小程序信息")

    '''
    wxapp - 小程序基本信息列表
    '''
    login_interface = "/api/wxapp/Select"
    data = {
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "wxapp - 小程序基本信息列表")

    '''
    wxapp - 小程序排名
    '''
    login_interface = "/api/wxapp/rank"
    data = {
        "wxapp_uniacid": "",  # 小程序id
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "wxapp - 小程序排名")


    '''
    wxapp - 小程序数据列表
    '''
    login_interface = "/api/wxapp/List"
    data = {
        "page":"",#页码默认值: 1
        "size":"",#一页多少条默认值: 10
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "wxapp - 小程序数据列表")



    '''
    wxapp - 小程序数据时间对比
    '''
    login_interface = "/api/wxapp/Tablerange"
    data = {
        "wxapp_uniacid":"",#小程序id
        "date":"2019-01-01~2019-01-07",#时间 eg:2018-10-10~2018-10-11
        "compare_date":"2019-01-01~2019-01-07",#时间 eg:2018-10-10~2018-10-11
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "wxapp - 小程序数据时间对比")



    '''
    wxapp - 小程序数据概览
    '''
    login_interface = "/api/wxapp/Overview"
    data = {
        "wxapp_uniacid": "",  # 小程序id
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "wxapp - 小程序数据概览")



    '''
    wxapp - 新增留存列表
    '''
    login_interface = "/api/wxapp/Keepnew"
    data = {
        "wxapp_uniacid":"",#小程序id
        "dayNums":"",#天，默认值: 7，允许值: 1, 7, 30
        "date":"2019-01-01~2019-01-07",#时间 eg:2018-10-10~2018-10-11
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "wxapp - 新增留存列表")


    '''
    wxapp - 活跃留存列表
    '''
    login_interface = "/api/wxapp/Keepactive"
    data = {
        "wxapp_uniacid":"1",#小程序id
        "dayNums":"7",#天，默认值: 7，允许值: 1, 7, 30
        "date":"2019-01-01~2019-01-07",#时间 eg:2018-10-10~2018-10-11
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "wxapp - 活跃留存列表")



    '''
    wxapp - 留存数据表格
    '''
    login_interface = "/api/wxapp/Keeptable"
    data = {
        "wxapp_uniacid":"",#小程序id
        "dayNums":"1",#天，默认值: 7，允许值: 1, 7, 30
        "date":"2019-01-01~2019-01-07",#时间 eg:2018-10-10~2018-10-11
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "wxapp - 留存数据表格")
wxapp_go()


#**************************************************    company   接口   **********************************************
def company_go():
    '''
    company  - 公司设置详情接口
    '''
    login_interface = "/api/company/edit"
    shouji=go.shoujihao()
    tel="010-"+str(shouji)
    data = {
        "name": "测公司名称",  # 公司名称
        "remark": "简简单单的介绍一下",  # 公司简介
        "province": "北京",  # 省
        "city": "北京",  # 市
        "district": "北京",  # 区
        "address": "102街道",  # 街道地址
        "tel": tel,  # 联系电话
        "headpic": "",  # 公司头像
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "company - 公司设置详情接口")

    '''
    company  - 公司详情接口
    '''
    login_interface = "/api/company/info"
    data = {
    }
    data["token"] = k[0]
    headers = {
    }
    r = go.post(url_qian + login_interface, data, headers, "company - 公司详情接口")
company_go()

def end():
    excel.end("plus接口运行结果")
end()