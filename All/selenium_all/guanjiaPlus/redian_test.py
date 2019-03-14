from math import log
from math import e
from python_all.SQL import sql

s= sql.sql()

sql_yuju = "SELECT DISTINCT openid FROM `ims_plus_chaselog` WHERE addtime>=1535731200 and addtime<=1538323199  and  uniacid in ('1014')"

openid_1014_near = s.lianjie_sql("39.107.239.18", "root", "wdtx.2016", "vd_mp_plus_shop_test", sql_yuju)


R=0           # R为评估时间段内所有文章（n）的阅读总数；
Z=0           # Z为评估时间段内所有文章（n）的点赞总数；
d=1           # d为评估时间段所含天数（一般周取7天，月度取30天，年度取365天，其他自定义时间段以真实天数计算）；
n=0           # n为评估时间段内账号所发文章数；
Rt=0
Zt=0
            # Rt和Zt为评估时间段内账号所发头条的总阅读数和总点赞数；
Rmax=100001
Zmax=15325
            # Rmax和Zmax为评估时间段内账号所发文章的最高阅读数和最高点赞数。



def ln(n):
  result =  log(n,e)
  return result

# a=ln(4)
# print(a)
def hh():
    a1=ln(R/d+1)
    a2=ln(10*Z/d+1)
    a3=ln(R/n+1)
    a4=ln(10*Z/n+1)
    a5=ln(Rt/d+1)
    a6=ln(10*Zt/d+1)
    a7=ln(Rmax+1)
    a8=ln(10*Zmax+1)
    wci={0.3*[0.85*a1+0.15*a2]+0.3*[0.85*a3+0.15*a4]+0.3*[0.85*a5+0.15*a6]+0.1*[0.85*a7+0.15*a8]}
    Wci=pow(wci,2)
    WCI=Wci*10
    print(WCI)

