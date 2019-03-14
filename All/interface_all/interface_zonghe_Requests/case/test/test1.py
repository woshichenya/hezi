import sql
import interface_all.interface_zonghe_Requests.baibaoxiang.baibaoxiangInterface
import re
import sql
import requests
import interface_all.interface_zonghe_Requests.baibaoxiang.excel_xlwt
import time
go= interface_all.interface_zonghe_Requests.baibaoxiang.baibaoxiangInterface.go()

time_new=time.strftime("%Y%m%d%H%M%S",time.localtime())
'''通用模块'''
excel=interface_all.interface_zonghe_Requests.baibaoxiang.excel_xlwt.a()
sql_url="SELECT id FROM `plus_user_position` where `name` like '新添加的职位'"
sql_go=sql.sql()
'''SQL语句们'''
sql_gzh_id_list="SELECT uniacid FROM plus_shop_info WHERE user_id in (SELECT user_id FROM `plus_users` as a WHERE group_id ='1016')"






roles="1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40"
username="18000000312"
pas="1234567a"
#新增成员接口  这个是通用值
#登录接口切换，登录token实时获取
'''
通用方法
'''
go= interface_all.interface_zonghe_Requests.baibaoxiang.baibaoxiangInterface.go()
url_qian="http://test-plus.moliyan.com.cn"
'''
登录接口
'''
login_interface="/api/index/login"
headers={

}
url_sso="https://test-sso.vdongchina.com/index/logincheck"
data={
    "username":"18000000339",
    "password":"1234567a"}
r=go.post(url_sso,data,headers,"sso登录接口")
k2=re.findall("\"wd_token\":\"(.*?)\"",r.text)
data={
    "wd_token":k2[0]
}
r=go.post(url_qian+login_interface,data,headers,"登录接口")
k=re.findall("\"token\":\"(.*?)\"",r.text)
data["token"]=k[0]
go= interface_all.interface_zonghe_Requests.baibaoxiang.baibaoxiangInterface.go()
url_qian="http://test-plus.moliyan.com.cn"

for i in range (1,2):
    shouji=go.shoujihao()
    '''
    Group - 新增成员接口
    '''
    login_interface = "/api/group/adduser"
    user_name = "人" + str(shouji)
    data = {
        "account": shouji,  # 登录账号
        "password": "1234567a",  # 密码
        "pid": "1296",  # 所属上级
        "position_id": "2001",  # 职位
        "remark": "简介"+str(shouji),  # 职位简介
        "name": user_name,  # 姓名
        "province": "北京市",  # 省
        "city": "北京市",  # 市
        "district": "",  # 县
    }
    data["token"] = k[0]
    headers = {

    }
    r = go.post(url_qian + login_interface, data, headers, "Group - 新增成员接口")

