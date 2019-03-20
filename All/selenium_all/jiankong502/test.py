import baibaoxiangInterface
go=baibaoxiangInterface.go()
data={}
k=go.post("https://serverplus.vdongchina.com/admin/user/userlist",data,"","name")
kk=k.status_code
print(kk)
if 200 in kk:
    print(111111111111)
if "200" in kk:
    print(22222222222)