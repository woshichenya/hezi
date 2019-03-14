import requests
import random
import time
from datetime import datetime
from datetime import timedelta

#################################

payload={}



#uu_val=15367330601652459489
#at_val=15378546936253853261
wsr_val='%7B%22path%22%3A%22pages%2Fbusiness%2Fbusiness%22%2C%22scene%22%3A1001%2C%22query%22%3A%7B%7D%7D'
#########ak_val='xulitest'
ev_val='page'
#st_val=1537854696572
dr_val=2
pp_val='pages%2Fscanning%2Fscanning'
life_val='show'
sc_val='undefined'
ec_val=0
nt_val='wifi'
pm_val='iPhone%205'
pr_val=2
ww_val=320
wh_val=456
lang_val='zh_CN'
wv_val='6.6.3'
lat_val='undefined'
lng_val='undefined'
spd_val='undefined'
v_val='6.1.2'
wsdk_val='1.9.91'
sv_val='iOS%2010.0.1'
wvv_val='devtools'
lp_val='pages%2Fbusiness%2Fbusiness'
#rq_c_val=4

###################################
#############获取n天前的时间戳
now = datetime.now()
delta=-timedelta(90) #90天前
final_time=str(now+delta)
final=final_time.split('.')
print('final is:{}'.format(final))
final_time=final[0]
print('final_time is:{}'.format(final_time))
timeArray = time.strptime(final_time, "%Y-%m-%d %H:%M:%S")
print('timeArray is:{}'.format(timeArray))
timeStamp = int(time.mktime(timeArray))
millis = int(round(timeStamp * 1000))
print('timeStamp is:{}'.format(millis))

#########################################
uu_list=[]
uu=15366368393675743707
for i in range(20):
    uu_list.append(uu)
    uu=uu+1
print('uu_list is:{}'.format(uu_list))

at_list=[]
at=15370928445783535415
for i in range(20):
    at_list.append(at)
    at=at+1
print('at_list is:{}'.format(at_list))

#################################

def interfaceGet(str):
    st_val = millis  # 时间戳是10位的,转换成了13位的时间戳
    ak_val=str
    rq_c_val = 0
    i2 = random.randint(3, 5)
    #i2 = 1
    print('该值表示的是uu的个数,即用户的个数:{}'.format(i2))
    for i in range(i2):
        uu_val = uu_list[i]
        i3 = random.randint(1, 3)
        #i3=1
        print('该值表示的是session个数或步数:{}'.format(i3))
        for i in range(i3):
            at_val = at_list[i]
            rq_c_val = i + 1

            st_val = st_val + random.randint(5, 20)    #时间递增步数是随机值

            payload = {
                'uu': uu_val,  #############用户唯一标示
                'at': at_val,  #############session标识,18或19位
                'wsr': wsr_val,  # 路径+参数场景值,目前设置为固定值
                'ak': ak_val,  #########32位,数字+字母组成
                'ev': ev_val,  # 跳转新页面显示page,本页面显示evernt
                'st': st_val,  ############时间戳,最好设置成递增值
                'dr': dr_val,  #########页面停留时间
                'pp': pp_val,  # 访问路径
                'life': life_val,  # 目前先固定为show,不知道啥意思
                'sc': sc_val,  # 正确的数量,目前先固定为undefined
                'ec': ec_val,  # 错误的数量,目前先固定为0
                'nt': nt_val,  # 网络类型,目前先固定为wifi
                'pm': pm_val,  # 手机型号
                'pr': pr_val,  # 像素点,目前先固定为3
                'ww': ww_val,  # 屏幕宽度,目前先固定为375
                'wh': wh_val,  # 屏幕高度,目前先固定为642
                'lang': lang_val,  # 浏览器语言,目前先固定为zh_CN
                'wv': wv_val,  # 微信版本号,目前先固定为6.6.3
                'lat': lat_val,  # 经度,目前先固定为undefined
                'lng': lng_val,  # 维度,目前先固定为undefined
                'spd': spd_val,  # 速度,目前先固定为undefined
                'v': v_val,  # sdk版本,目前先固定为6.1.2
                'wsdk': wsdk_val,  # sdk版本号,目前先固定为1.9.91
                'sv': sv_val,  # 系统版本,目前先固定为iOS%2010.0.1
                'wvv': wvv_val,  # 目前先固定为devtools
                'lp': lp_val,  # 访问来源,目前先固定为pages%2Fscanning%2Fscanning
                'rq_c': rq_c_val  ###############第几步,递增标识

            }

            print('payload is:{}'.format(payload))
            r = requests.get('http://47.93.51.52:5107/kafka/log', params=payload)
            #print(r.url)
            print('url is:{}'.format(r.url))
            #print(r.text)
            print('text is:{}'.format(r.text))

            time.sleep(2)


time.sleep(10)
interfaceGet('80d114e0c97f848e79ecef61a489a941')   #第一个小程序从90天到现在的数据
################################



#r=requests.post('http://47.93.51.52:5107/kafka/log',data=datas)
#print(r.content)
#print(r.status_code)





#r=requests.get('http://47.93.51.52:5107/kafka/log',params=payload)
#print(r.url)
#print(r.text)

