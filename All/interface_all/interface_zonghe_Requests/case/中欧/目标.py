from baibaoxiang import sql
a=sql.sql()
sql="SELECT SUM(speed)/SUM(aims)*100 as '完成/目标' FROM `vd_plan` WHERE aims_time = '1554048000'"
sql="SELECT speed,aims FROM `vd_plan` WHERE aims_time = '1554048000';"
x=a.lianjie_sql("vd_183run",sql)
print(x)
mubiao=0
wancheng=0
for i in x:
    mubiao+=i[1]
    if i[0]>i[1]:
        wancheng+=i[1]
    else:
        wancheng+=i[0]
print("目标",mubiao,"完成",wancheng,"比例",wancheng/mubiao*100,"%")
