from python_all.SQL import sql

s= sql.sql()

new_vip=[]

def panduanxinzengrenyuan():
    ixx = 1
    gongzhonghao_id="('1014')"
    #sql_yuju="SELECT DISTINCT openid FROM `ims_plus_chaselog` WHERE uniacid='1014'"
    sql_yuju2="SELECT DISTINCT openid FROM `ims_plus_chaselog` WHERE addtime>=1535731200 and addtime<=1538323199  and  uniacid in ('1014')"
    #sql_yuju3 = "SELECT DISTINCT openid FROM `ims_plus_chaselog` WHERE uniacid='1014' and addtime>=1535731200" #9-1以后的
    sql_yuju4 = "SELECT DISTINCT openid FROM `ims_plus_chaselog` WHERE uniacid='1014' and addtime<=1538323199" #9-30以前
    sql_yuju5 = "SELECT DISTINCT openid FROM `ims_plus_chaselog` WHERE uniacid='1014' and addtime<1535731200" #9-1以前
    sql_yuju6="SELECT DISTINCT openid FROM ims_ewei_shop_order where  status>0 and iswxappcreate=1 AND  createtime>=1535731200  AND createtime<=1538323199 and uniacid in(1014) AND `status`>0"

    openid_1014_old = s.lianjie_sql("39.107.239.18", "root", "wdtx.2016", "vd_mp_plus_shop_test", sql_yuju5)
    openid_1014_fangke=s.lianjie_sql("39.107.239.18", "root", "wdtx.2016", "vd_mp_plus_shop_test", sql_yuju2)
    openid_1014_fukuan = s.lianjie_sql("39.107.239.18", "root", "wdtx.2016", "vd_mp_plus_shop_test", sql_yuju6)
    #整数化9.1号以前的访问人数
    openid_1014_old_int=len(openid_1014_old)
    # 整数化9.30号以前的访问人数
    openid_1014_near_int=len(openid_1014_near)
    #计算新访问人数==新用户
    openid_1014_new=openid_1014_near_int-openid_1014_old_int
    #计算9.1-9.30之间的访问人数
    openid_1014_fangke_int=len(openid_1014_fangke)
    #计算9.1-9.30之间成功支付的人数
    openid_1014_fukuan_int=len(openid_1014_fukuan)
    print("9.1之前共有：",openid_1014_old_int,"人访问过")
    print("9.30之前共有：",openid_1014_near_int,"人访问过")
    print("9.1-9.30之间新增了：",openid_1014_new,"人访问")
    #老用户-新用户/老用户
    print("访问增长率：",(openid_1014_old_int-openid_1014_new)/openid_1014_old_int)
    print("访客人数：",openid_1014_fangke_int,"人")
    print("付款人数：",openid_1014_fukuan_int,"人")
    #付款人数/访客人数
    print("小程序购买转化率：",openid_1014_fukuan_int/openid_1014_fangke_int)

    #openid_1014_near=json.loads(openid_1014_near)
    #openid_1014=json.loads(openid_1014)
    #openid_1014_new=set(openid_1014_near).difference(set(openid_1014))
    #print(len(openid_1014_new))
    #print(openid_1014)


#panduanxinzengrenyuan()
'''
这里查询指定时间段内的公众号关注数量
'''
#sql_yuju="SELECT `name`,SUM(cumulate) as '累计',SUM(new) as '新增人数',SUM(cancel) as '取消关注人数' FROM `ims_plus_wechats` WHERE addtime > '1541174399' and addtime <= '1541692799' and  `name`  LIKE '%江小白%' GROUP BY `name` ORDER BY id DESC"
#sql_yuju="SELECT SUM(cumulate) as '累计',SUM(new) as '新增人数',SUM(cancel) as '取消关注人数',SUM(new)-SUM(cancel) as '净增关注人数' FROM `ims_plus_wechats` WHERE addtime >= '1541174399' and addtime <= '1541692799' and  `name`  LIKE '%江小白%' GROUP BY `addtime` ORDER BY id DESC"
sql_yuju="SELECT `name`,SUM(cumulate),SUM(new) ,SUM(cancel)  FROM `ims_plus_wechats` WHERE addtime > '1541174399' and addtime <= '1541692799' and  `name`  LIKE '%江小白%' GROUP BY `name` ORDER BY id DESC"

sql_get = s.lianjie_sql("39.107.239.18", "root", "wdtx.2016", "vd_mp_plus_shop_test", sql_yuju)
print("名称，累计人数，新增人数，取消人数")


for a in sql_get:
    print(a)



'''
def a():
    openid_1014_one="111"
    sql_yuju = "SELECT MAX(addtime) FROM `ims_plus_chaselog` WHERE openid ="+openid_1014_one
    #ss=sql_yuju+openid_1014_one
    print(sql_yuju)
    print(
        set(a).intersection(set(b))  # 交集
    )
    print
    set(a).union(set(b))  # 并集
    print
    set(a).difference(set(b))  # 差集，在a中但不在b中的元素
    print
    set(b).difference(set(a))  # 差集，在b中但不在a中的元素
'''