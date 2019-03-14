import interface_all.interface_zonghe_Requests.baibaoxiang.baibaoxiangInterface
go=interface_all.interface_zonghe_Requests.baibaoxiang.baibaoxiangInterface.go()
excel=interface_all.interface_zonghe_Requests.baibaoxiang.excel_xlwt.a()

#定义一个起始值
on= 18100000080
url="https://test-sso.vdongchina.com/index/sendsns"
data={
    "tel":on,
    "type":2
}
headers={

}
for i in range(1,2):
    on+=1
    #print("第",i,"次")
    if i%2 ==0:
        # print("找回密码")
        data["tel"] =18871551774
        data["type"]=2
        t_g = go.post(url, data, headers, "sso忘记密码获取验证码接口")

    else:
        # print("注册")
        data["tel"] = on
        data.pop("type")
        t_g = go.post(url, data, headers, "sso注册获取验证码接口")


    if "图片验证码错误" in t_g.json()["msg"]:
        print("已出现验证码，当前第", i, "次")



def end():
    excel.end("sso验证码")
end()