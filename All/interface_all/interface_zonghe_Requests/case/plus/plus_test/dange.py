from beifen import sql
import time

new_time="'"+time.strftime("%Y-%m-%d", time.localtime())+"'"
old_time="2019-01-01"
sql_go = sql.sql()
'''SQL语句们'''

#人员信息
user_id="in ('1203')"
print("后user——id是：",user_id)
uniacid_one='536'
#全部人员信息
all_user__id="in (SELECT user_id FROM `plus_users` as a WHERE group_id ='1016')"
# 公众号id
sql_gzh_id_list = "SELECT uniacid FROM plus2test.plus_shop_info WHERE user_id "+user_id
# 人员id
sql = "SELECT * FROM plus_store WHERE group_id = '1016'"
# 门店id
sql = "SELECT id FROM plus_store WHERE user_id  "+user_id
# 或者
sql = "SELECT COUNT(id),city FROM plus_store WHERE group_id ='1016'"
# 店铺id
sql = "SELECT id FROM plus_shop_info WHERE user_id "+user_id
# 今天商品信息
sql = "SELECT sum(a.new_goods_sum),sum(a.visit_goods_sum),sum(a.visit_goods_member_sum),sum(a.visit_goods_show_sum),sum(a.pay_person_sum),sum(a.total),sum(a.goods_sum) FROM plus_shop_realtime_data as a  WHERE uniacid in (" + sql_gzh_id_list + ")"

# 店铺数量：
sql = "SELECT COUNT(id) FROM plus_shop_info WHERE user_id "+user_id
print(sql)
all_shop_sum = sql_go.lianjie_sql("plus2test", sql)
print("店铺数量", int(all_shop_sum[0][0]))
# 小程序店铺数量：
sql = "SELECT COUNT(id) FROM plus_shop_info WHERE type = '1' AND user_id "+user_id
xiao_shop_sum = sql_go.lianjie_sql("plus2test", sql)
print("小程序店铺数量", int(xiao_shop_sum[0][0]))
# 公众号店铺数量：
sql = "SELECT COUNT(id) FROM plus_shop_info WHERE type = '2' AND user_id "+user_id
wxapp_shop_sum = sql_go.lianjie_sql("plus2test", sql)
print("公众号店铺数量", int(wxapp_shop_sum[0][0]))

if int(wxapp_shop_sum[0][0]) + int(xiao_shop_sum[0][0]) == int(all_shop_sum[0][0]):
    print("店铺数量取值正确，开始核对接口数据")
else:
    print("店铺数量错误****************************************************************************")

# 店铺城市
sql = "SELECT m.type,u.city FROM plus_shop_info as m INNER JOIN plus_users as u on m.user_id = u.user_id where u.user_id "+user_id+" GROUP BY m.type,u.city"
print(sql)
all_shop_city = sql_go.lianjie_sql("plus2test", sql)
print("店铺城市", all_shop_city)
sql = "SELECT * FROM `plus_users` WHERE user_id "+user_id+" GROUP BY city"
all_shop_city_sum = sql_go.lianjie_sql("plus2test", sql)
if all_shop_city_sum != "":
    all_shop_city_sum_len = len(all_shop_city_sum)
    print("一共覆盖了", all_shop_city_sum_len, "个城市")

# 店铺销售额数据
# 今天销售额：
sql = "SELECT SUM(sale_prices) FROM `plus_shop_realtime_data` where uniacid in (" + sql_gzh_id_list + ")"
print(sql)
all_goods_mai_new = sql_go.lianjie_sql("plus2test", sql)
try:
    print("今天店铺销售额数据\t", float(all_goods_mai_new[0][0]))
    all_goods_mai_new_f = float(all_goods_mai_new[0][0])
except:
    print("今天店铺销售额数据\t", 0)
# 平均每小时销售额：
sql = "SELECT SUM(sale_prices)/14 FROM `plus_shop_sale_count_hour` where `hour` < '23' AND create_date = "+new_time+" AND uniacid in (" + sql_gzh_id_list + ")"
all_goods_mai_h = sql_go.lianjie_sql("plus2test", sql)
try:
    print(new_time+"--23:00的每小时销售额数据\t", float(all_goods_mai_h[0][0]))
except:
    print(new_time+"--14:00的每小时销售额数据\t", 0)
# 小程序+今天销售额
sql = "SELECT SUM(sale_prices) FROM `plus_shop_realtime_data` where type = '1' AND uniacid in (" + sql_gzh_id_list + ")"
xiao_goods_mai_new = sql_go.lianjie_sql("plus2test", sql)
try:
    xiao_goods_mai_new_f = float(xiao_goods_mai_new[0][0])
    print("小程序今天店铺销售额数据\t", xiao_goods_mai_new_f)
except:
    print("小程序今天店铺销售额数据\t",0)
# 公众号+今天销售额
sql = "SELECT SUM(sale_prices) FROM `plus_shop_realtime_data` where type = '2' AND uniacid in (" + sql_gzh_id_list + ")"
wxapp_goods_mai_new = sql_go.lianjie_sql("plus2test", sql)
if wxapp_goods_mai_new != "":
    # wxapp_goods_mai_new_f = float(wxapp_goods_mai_new[0][0])
    print("公众号今天店铺销售额数据\t", wxapp_goods_mai_new[0][0])
# 昨天销售额
sql = "SELECT SUM(sale_prices) FROM `plus_shop_sale_visit` where uniacid in (" + sql_gzh_id_list + ")"
all_goods_mai_old = sql_go.lianjie_sql("plus2test", sql)
try:
    print("昨天店铺销售额数据\t", float(all_goods_mai_old[0][0]))
    all_goods_mai_old_f = float(all_goods_mai_old[0][0])
except:
    print("昨天店铺销售额数据\t", 0)
# 小程序+昨天销售额：
sql = "SELECT SUM(sale_prices) FROM `plus_shop_sale_visit` where type = '1' AND uniacid in (" + sql_gzh_id_list + ")"
xiao_goods_mai_old = sql_go.lianjie_sql("plus2test", sql)
try:
    xiao_goods_mai_old_f = float(xiao_goods_mai_old[0][0])
    print("小程序昨天店铺销售额数据\t", xiao_goods_mai_old_f)
except:
    print("小程序昨天店铺销售额数据\t", 0)
# 公众号+昨天销售额：
sql = "SELECT SUM(sale_prices) FROM `plus_shop_sale_visit` where type = '2' AND uniacid in (" + sql_gzh_id_list + ")"
wxapp_goods_mai_old = sql_go.lianjie_sql("plus2test", sql)

print("公众号昨天店铺销售数据\t", wxapp_goods_mai_old[0][0])
# if float(wxapp_goods_mai_new[0][0]) + float(xiao_goods_mai_new[0][0]) == float(all_goods_mai_new[0][0]) and float(
#         wxapp_goods_mai_old[0][0]) + float(xiao_goods_mai_old[0][0]) == float(all_goods_mai_old[0][0]):
#     print("店铺销售额数量取值正确，开始核对接口数据")
# else:
#     print("店铺销售额数量错误****************************************************************************")
# # 统计
# print("全部店铺销售额为\t", all_goods_mai_new_f + all_goods_mai_old_f, "\t元")
# print("全部小程序销售额为\t", xiao_goods_mai_new_f + xiao_goods_mai_old_f, "\t元")
# print("全部公众号销售额为\t", wxapp_goods_mai_new_f + wxapp_goods_mai_old_f, "\t元")
# 分计
# 每天销售额：
sql = "SELECT SUM(sale_prices),create_date FROM `plus_shop_sale_visit` where uniacid in (" + sql_gzh_id_list + ") GROUP BY create_date"
all_goods_mai_everday_all = sql_go.lianjie_sql("plus2test", sql)
print("该账号每天销售额：")
for all_goods_mai_everday_x_x in all_goods_mai_everday_all:
    print("\t", all_goods_mai_everday_x_x)
print("结束。。。")

sql = "SELECT SUM(sale_prices),create_date,IF(type='1','小程序','公众号') FROM `plus_shop_sale_visit` where uniacid in (" + sql_gzh_id_list + ") GROUP BY create_date,type"
all_goods_mai_everday = sql_go.lianjie_sql("plus2test", sql)
# print("111111111",all_goods_mai_everday)
print("该账号每天销售额：")
for all_goods_mai_everday_x in all_goods_mai_everday:
    print("\t", all_goods_mai_everday_x)
print("结束。。。")
# 店铺商品数量：
# 今天商品数量：
sql = "SELECT SUM(goods_sum) FROM plus_shop_realtime_data WHERE uniacid in(" + sql_gzh_id_list + ")"
all_goods_sum_new = sql_go.lianjie_sql("plus2test", sql)
try:
    print("今天店铺商品数量\t", float(all_goods_sum_new[0][0]))
except:
    print("今天店铺商品数量\t", all_goods_sum_new[0][0])
# 昨日商品数量：
sql = "SELECT goods_sum FROM plus_shop_sale_visit WHERE uniacid in(" + sql_gzh_id_list + ") ORDER BY create_date desc"
all_goods_sum_old = sql_go.lianjie_sql("plus2test", sql)
print("昨日店铺商品数量\t", all_goods_sum_old[0][0])
# 小程序+今天商品数量：
sql = "SELECT SUM(goods_sum) FROM plus_shop_realtime_data WHERE type = '1' AND uniacid in(" + sql_gzh_id_list + ")"
xiao_goods_sum_new = sql_go.lianjie_sql("plus2test", sql)
print("小程序今天店铺商品数量\t", xiao_goods_sum_new[0][0])
# 公众号+今天商品数量：
sql = "SELECT SUM(goods_sum) FROM plus_shop_realtime_data WHERE type = '2' AND uniacid in(" + sql_gzh_id_list + ")"
wxapp_goods_sum_new = sql_go.lianjie_sql("plus2test", sql)
try:
    print("公众号今天店铺商品数量\t", float(wxapp_goods_sum_new[0][0]))
except:
    print("公众号今天店铺商品数量\t0")
# 小程序+昨日商品数量：
sql = "SELECT SUM(goods_sum) FROM plus_shop_sale_visit WHERE type = '1' AND uniacid in(" + sql_gzh_id_list + ")"
xiao_goods_sum_old = sql_go.lianjie_sql("plus2test", sql)
print("小程序昨日店铺商品数量\t", xiao_goods_sum_old[0][0])
# 公众号+昨日商品数量：
sql = "SELECT SUM(goods_sum) FROM plus_shop_sale_visit WHERE type = '2' AND uniacid in(" + sql_gzh_id_list + ")"
wxapp_goods_sum_old = sql_go.lianjie_sql("plus2test", sql)
try:
    print("公众号昨日店铺商品数量\t", float(wxapp_goods_sum_old[0][0]))
except:
    print("公众号昨日店铺商品数量\t0")


# if int(wxapp_goods_sum_old[0][0]) + int(xiao_goods_sum_old[0][0]) == int(all_goods_sum_old[0][0]) and int(
#         wxapp_goods_sum_new[0][0]) + int(xiao_goods_sum_new[0][0]) == int(all_goods_sum_new[0][0]):
#     print("店铺商品数量取值正确，开始核对接口数据")
# else:
#     print("店铺商品数量错误****************************************************************************")

# 统计
all_goods_sum_and_f = float(all_goods_sum_new[0][0]) + float(all_goods_sum_old[0][0])
print("店铺商品数量累计\t", all_goods_sum_and_f, "\t个")
xiao_goods_sum_and_f = float(xiao_goods_sum_new[0][0]) + float(xiao_goods_sum_old[0][0])
print("小程序商品数量累计\t", xiao_goods_sum_and_f, "\t个")
wxapp_goods_sum_and_f = float(wxapp_goods_sum_old[0][0]) + float(wxapp_goods_sum_new[0][0])
print("公众号商品数量累计\t", wxapp_goods_sum_and_f, "\t个")

# 店铺访问量：
# 今天：
sql = "SELECT SUM(visit_person_sum) FROM plus_shop_realtime_data WHERE uniacid in(" + sql_gzh_id_list + ")"
print(sql)
all_visit_sum_new = sql_go.lianjie_sql("plus2test", sql)
all_visit_sum_new_f = all_visit_sum_new[0][0]
print("今天店铺访问量\t", all_visit_sum_new_f)
# 昨日：
sql = "SELECT SUM(visit_person_sum) FROM plus_shop_sale_visit WHERE uniacid in(" + sql_gzh_id_list + ")"
all_visit_sum_old = sql_go.lianjie_sql("plus2test", sql)
all_visit_sum_old_f = all_visit_sum_old[0][0]
print("昨日店铺访问量\t", all_visit_sum_old_f)
# 小程序+今天：
sql = "SELECT COUNT(uniacid) FROM plus_shop_realtime_data WHERE type = '1' AND uniacid in (SELECT uniacid FROM plus_shop_info WHERE  type='1' and user_id in (SELECT user_id FROM `plus_users` WHERE user_id "+user_id+") )"
xiao_visit_sum_new = sql_go.lianjie_sql("plus2test", sql)
print("小程序今天店铺访问量\t", xiao_visit_sum_new[0][0])
# 公众号+今天：
sql = "SELECT COUNT(uniacid) FROM plus_shop_realtime_data WHERE type = '2' AND uniacid in (SELECT uniacid FROM plus_shop_info WHERE  type='1' and user_id in (SELECT user_id FROM `plus_users` WHERE user_id "+user_id+") )"
wxapp_visit_sum_new = sql_go.lianjie_sql("plus2test", sql)
print("公众号今天店铺访问量\t", wxapp_visit_sum_new[0][0])
# 小程序+昨日：
sql = "SELECT SUM(visit_person_sum) FROM plus_shop_sale_visit WHERE type = '1' AND uniacid in(" + sql_gzh_id_list + ")"
print(sql)
xiao_visit_sum_old = sql_go.lianjie_sql("plus2test", sql)
print("小程序昨日店铺访问量\t", xiao_visit_sum_old[0][0])
# 公众号+昨日：
sql = "SELECT SUM(visit_person_sum) FROM plus_shop_sale_visit WHERE type = '2' AND uniacid in(" + sql_gzh_id_list + ")"
wxapp_visit_sum_old = sql_go.lianjie_sql("plus2test", sql)
print("公众号昨日店铺访问量\t", wxapp_visit_sum_old[0][0])
# 小程序+昨日+分析：
sql = "SELECT create_date,SUM(visit_person_sum) FROM plus_shop_sale_visit WHERE type = '1' AND uniacid in(" + sql_gzh_id_list + ")GROUP BY create_date"
xiao_visit_sum_old_fenxi = sql_go.lianjie_sql("plus2test", sql)
for xiao_visit_sum_old_fenxi_x in xiao_visit_sum_old_fenxi:
    print("时间：\t", xiao_visit_sum_old_fenxi_x[0], "\t访问量：\t", xiao_visit_sum_old_fenxi_x[1])
# 访问人数_统计
try:
    all_visit_sum_and_f = all_visit_sum_new_f + all_visit_sum_old_f
    print("店铺累计访问人数：\t", all_visit_sum_and_f, "\t人")
    print("小程序累计访问人数：\t", xiao_visit_sum_new[0][0] + xiao_visit_sum_old[0][0], "\t人")

    print("公众号累计访问人数：\t", wxapp_visit_sum_new[0][0] + wxapp_visit_sum_old[0][0], "\t人")
except:
    print("公众号累计访问人数：\t0\t人")

# 小程序数据汇总：
sql = "SELECT SUM(session_cnt) as '打开次数',SUM(visit_uv_new) as '新增访问人数',SUM(visit_total) as '累计用户数' ,SUM(share_uv) as '转发人数' FROM `plus_wxapp_visit` WHERE uniacid in(SELECT uniacid FROM plus_shop_info WHERE user_id in (SELECT user_id FROM plus_users WHERE user_id "+user_id+"))and create_date = "+new_time
xiao_all_fenxi = sql_go.lianjie_sql("plus2test", sql)
for xiao_all_fenxi_x in xiao_all_fenxi:
    print("\t小程序打开次数\t", xiao_all_fenxi_x[0], "\t小程序新增访问人数\t", xiao_all_fenxi_x[1], "\t小程序累计用户数\t", xiao_all_fenxi_x[2],
          "\t小程序转发人数\t", xiao_all_fenxi_x[3])
# 小程序数据排行汇总：
sql = "SELECT uniacid,session_cnt as '打开次数',visit_uv_new as '新增访问人数',visit_total as '累计用户数' ,share_uv as '转发人数' FROM `plus_wxapp_visit` WHERE uniacid in(SELECT uniacid FROM plus_shop_info WHERE user_id in (SELECT user_id FROM plus_users WHERE user_id "+user_id+"))and create_date = "+new_time+" ORDER BY visit_total DESC "
xiao_all_fenxi = sql_go.lianjie_sql("plus2test", sql)
paiming_xiaochengxu_fangwen = 0
for xiao_all_fenxi_x in xiao_all_fenxi:
    sql = "SELECT `name`,city FROM `plus_users` WHERE user_id in (SELECT user_id FROM `plus_shop_info` WHERE uniacid ='" + \
          xiao_all_fenxi_x[0] + "')"
    xiao_all_fenxi_guishudi = sql_go.lianjie_sql("plus2test", sql)
    paiming_xiaochengxu_fangwen += 1
    print("第%s名" % paiming_xiaochengxu_fangwen, "\t小程序id\t", xiao_all_fenxi_x[0], "\t小程序打开次数\t", xiao_all_fenxi_x[1],
          "\t小程序新增访问人数\t", xiao_all_fenxi_x[2], "\t小程序累计用户数\t", xiao_all_fenxi_x[3], "\t小程序转发人数\t", xiao_all_fenxi_x[4],
          "\t归属地：\t", xiao_all_fenxi_guishudi[0][1], "\t小程序负责人：\t", xiao_all_fenxi_guishudi[0][0])
    if paiming_xiaochengxu_fangwen >= 10:
        break
# 小程序数据补充：
sql = "SELECT create_date,SUM(visit_total) as '累计用户数',SUM(visit_uv) as '访问人数visit_uv相加',SUM(`visit_pv`) as '访问次数',SUM(`visit_uv_new`) as  '新增访问人数',AVG (stay_time_uv) as '人均停留 （秒）',AVG (stay_time_session) as '均次停留 （秒）' FROM `plus_wxapp_visit` WHERE uniacid in(SELECT uniacid FROM plus_shop_info WHERE user_id in (SELECT user_id FROM plus_users WHERE user_id "+user_id+"))GROUP BY create_date  "
xiao_all_fenxi_buchong = sql_go.lianjie_sql("plus2test", sql)
paiming_xiaochengxu_fangwen = 0
for xiao_all_fenxi_x_buchong in xiao_all_fenxi_buchong:
    print("\t日期：\t", xiao_all_fenxi_x_buchong[0], "\t小程序累计用户数\t", xiao_all_fenxi_x_buchong[1], "\t小程序访问人数visit_uv相加\t",
          xiao_all_fenxi_x_buchong[2], "\t小程序访问次数\t", xiao_all_fenxi_x_buchong[3], "\t小程序新增访问人数\t",
          xiao_all_fenxi_x_buchong[4], "\t小程序人均停留 （秒）\t", xiao_all_fenxi_x_buchong[5], "\t小程序均次停留 （秒）\t",
          xiao_all_fenxi_x_buchong[6])

if int(wxapp_visit_sum_old[0][0]) + int(xiao_visit_sum_old[0][0]) == int(all_visit_sum_old[0][0]):
    if int(wxapp_visit_sum_new[0][0]) + int(xiao_visit_sum_new[0][0]) == int(all_visit_sum_new[0][0]):
        print("店铺访问量取值正确，开始核对接口数据")
    else:
        print("店铺访问量错误****************************************************************************")
        print("进日销售额：\t", int(wxapp_visit_sum_new[0][0]) + int(xiao_visit_sum_new[0][0]))
else:
    print("昨日销售额:\t", int(wxapp_visit_sum_old[0][0]) + int(xiao_visit_sum_old[0][0]))

# 小程序数量：
sql = "SELECT COUNT(id) FROM plus_shop_info WHERE type = '1' AND uniacid in (" + sql_gzh_id_list + ")"
xiao_sum = sql_go.lianjie_sql("plus2test", sql)
xiao_sum_len = int(xiao_sum[0][0])
print("一共有个小程序:\t%s\t个" % xiao_sum_len)

# 公众号数量：
sql = "SELECT COUNT(id) FROM plus_shop_info WHERE type = '2' AND uniacid in (" + sql_gzh_id_list + ")"
wxapp_sum = sql_go.lianjie_sql("plus2test", sql)
wxapp_sum_len = int(wxapp_sum[0][0])
print("一共有公众号:\t%s\t个" % wxapp_sum_len)

# 今日订单数量
sql = "SELECT SUM(pay_order_sum) FROM plus_shop_realtime_data WHERE uniacid in (" + sql_gzh_id_list + ")"
all_order_sum_new = sql_go.lianjie_sql("plus2test", sql)
try:
    all_order_sum_new_i = int(all_order_sum_new[0][0])
    print("今日订单有:\t%s\t个" % all_order_sum_new_i)
except:
    print("今日订单有:\t0\t个" )
# 昨日订单数量
sql = "SELECT SUM(order_sum) FROM plus_shop_sale_visit WHERE uniacid in (" + sql_gzh_id_list + ")"
all_order_sum_old = sql_go.lianjie_sql("plus2test", sql)
try:
    all_order_sum_old_i = int(all_order_sum_old[0][0])
    print("昨日订单有:\t%s\t个" % all_order_sum_old_i)
except:
    print("昨日订单有:\t0\t个" )
# 小程序今日订单数量
sql = "SELECT SUM(pay_order_sum) FROM plus_shop_realtime_data WHERE type = '1' AND uniacid in (" + sql_gzh_id_list + ")"
xiao_order_sum_new = sql_go.lianjie_sql("plus2test", sql)
try:
    xiao_order_sum_new_i = int(xiao_order_sum_new[0][0])
    print("小程序今日订单数量有:\t%s\t个" % xiao_order_sum_new_i)
except:
    print("小程序今日订单数量有:\t0\t个")
# 公众号今日订单数量
sql = "SELECT SUM(pay_order_sum) FROM plus_shop_realtime_data WHERE type = '2' AND uniacid in (" + sql_gzh_id_list + ")"
wxapp_order_sum_new = sql_go.lianjie_sql("plus2test", sql)
# wxapp_order_sum_new_i = int(wxapp_order_sum_new[0][0])
print("公众号今日订单数量有:\t%s\t个" % wxapp_order_sum_new[0][0])
# 小程序昨日订单数量
sql = "SELECT SUM(order_sum) FROM plus_shop_sale_visit WHERE type = '1' AND uniacid in (" + sql_gzh_id_list + ")"
xiao_order_sum_old = sql_go.lianjie_sql("plus2test", sql)
try:
    xiao_order_sum_old_i = int(xiao_order_sum_old[0][0])
    print("小程序昨日订单数量有:\t%s\t个" % xiao_order_sum_old_i)
except:
    print("小程序昨日订单数量有:\t0\t个" )
# 公众号昨日订单数量
sql = "SELECT SUM(order_sum) FROM plus_shop_sale_visit WHERE type = '2' AND uniacid in (" + sql_gzh_id_list + ")"
wxapp_order_sum_old = sql_go.lianjie_sql("plus2test", sql)
# wxapp_order_sum_old_i = int(wxapp_order_sum_old[0][0])
print("公众号昨日订单数量有:\t%s\t个" % wxapp_order_sum_old[0][0])

# 统计
print("店铺一共有订单：\t", all_order_sum_new_i + all_order_sum_old_i, "\t个")
print("小程序一共有订单：\t", xiao_order_sum_new_i + xiao_order_sum_old_i, "\t个")
# print("公众号一共有订单：\t", wxapp_order_sum_new_i + wxapp_order_sum_old_i, "\t个")

# 今日支付人数
sql = "SELECT SUM(pay_person_sum) FROM plus_shop_realtime_data WHERE uniacid in (" + sql_gzh_id_list + ")"
all_zhifu_sum_new = sql_go.lianjie_sql("plus2test", sql)
try:
    all_zhifu_sum_new_f = all_zhifu_sum_new[0][0]
    print("今日支付人数:\t%s\t个" % all_zhifu_sum_new_f)
except:
    print("今日支付人数:\t0\t个")
# 昨日支付人数
sql = "SELECT SUM(pay_person_sum) FROM plus_shop_sale_visit WHERE uniacid in (" + sql_gzh_id_list + ")"
all_zhifu_sum_old = sql_go.lianjie_sql("plus2test", sql)
try:
    all_zhifu_sum_old_f = all_zhifu_sum_old[0][0]
    print("昨日支付人数:\t%s\t个" % all_zhifu_sum_old_f)
except:
    print("昨日支付人数:\t0\t个")
# 小程序今日支付人数
sql = "SELECT SUM(pay_person_sum) FROM plus_shop_realtime_data WHERE type = '1' AND uniacid in (" + sql_gzh_id_list + ")"
xiao_zhifu_sum_new = sql_go.lianjie_sql("plus2test", sql)
try:
    xiao_zhifu_sum_new_f = xiao_zhifu_sum_new[0][0]
    print("小程序今日支付人数:\t%s\t个" % xiao_zhifu_sum_new_f)
except:
    print("小程序今日支付人数:\t0\t个")
# 公众号今日支付人数
sql = "SELECT SUM(pay_person_sum) FROM plus_shop_realtime_data WHERE type = '2' AND uniacid in (" + sql_gzh_id_list + ")"
print(sql)
wxapp_zhifu_sum_new = sql_go.lianjie_sql("plus2test", sql)
# wxapp_zhifu_sum_new_f = wxapp_zhifu_sum_new[0][0])
print("公众号今日支付人数:\t%s\t个" % wxapp_zhifu_sum_new[0][0])
# 小程序昨日支付人数
sql = "SELECT SUM(pay_person_sum) FROM plus_shop_sale_visit WHERE type = '1' AND uniacid in (" + sql_gzh_id_list + ")"
xiao_zhifu_sum_old = sql_go.lianjie_sql("plus2test", sql)
try:
    xiao_zhifu_sum_old_f = float(xiao_zhifu_sum_old[0][0])
    print("小程序昨日支付人数:\t%s\t个" % xiao_zhifu_sum_old_f)
except:
    print("小程序昨日支付人数:\t0\t个")
# 公众号昨日支付人数
sql = "SELECT SUM(pay_person_sum) FROM plus_shop_sale_visit WHERE type = '2' AND uniacid in (" + sql_gzh_id_list + ")"
wxapp_zhifu_sum_old = sql_go.lianjie_sql("plus2test", sql)
# wxapp_zhifu_sum_old_f = float(wxapp_zhifu_sum_old[0][0])
print("公众号昨日支付人数:\t%s\t个" % wxapp_zhifu_sum_old[0][0])

# 统计
# all_zhifu_sum_and_f = all_zhifu_sum_new_f + all_zhifu_sum_old_f
# print("累计支付人数：\t", all_zhifu_sum_and_f, "\t人")
# print("小程序累计支付人数：\t", xiao_zhifu_sum_new_f + xiao_zhifu_sum_old_f, "\t人")
# print("公众号累计支付人数：\t", wxapp_zhifu_sum_new_f + wxapp_zhifu_sum_old_f, "\t人")
# if wxapp_zhifu_sum_new_f + wxapp_zhifu_sum_old_f + xiao_zhifu_sum_new_f + xiao_zhifu_sum_old_f == all_zhifu_sum_and_f:
#     print("店铺支付人数取值正确，开始核对接口数据")
# else:
#     print("店铺支付人数错误****************************************************************************")

# 今日新增支付人数
sql = "SELECT SUM(new_member_sum) as '今日新增消费人数' FROM plus_shop_realtime_data WHERE uniacid in (" + sql_gzh_id_list + ")"
wxapp_zhifu_sum_old = sql_go.lianjie_sql("plus2test", sql)
try:
    wxapp_zhifu_sum_old_f = float(wxapp_zhifu_sum_old[0][0])
    print("今日新增支付人数:\t%s\t个" % wxapp_zhifu_sum_old_f)
except:
    print("今日新增支付人数:\t0\t个")
# 小程序今日新增支付人数
sql = "SELECT SUM(new_member_sum) as '今日新增消费人数' FROM plus_shop_realtime_data WHERE type = '1' AND uniacid in (" + sql_gzh_id_list + ")"
wxapp_zhifu_sum_old = sql_go.lianjie_sql("plus2test", sql)
try:
    wxapp_zhifu_sum_old_f = float(wxapp_zhifu_sum_old[0][0])
    print("小程序今日新增支付人数:\t%s\t个" % wxapp_zhifu_sum_old_f)
except:
    print("小程序今日新增支付人数:\t0\t个")
# 公众号今日新增支付人数
sql = "SELECT SUM(new_member_sum) as '今日新增消费人数' FROM plus_shop_realtime_data WHERE type = '2' AND  uniacid in (" + sql_gzh_id_list + ")"
wxapp_zhifu_sum_old = sql_go.lianjie_sql("plus2test", sql)
# wxapp_zhifu_sum_old_f = float(wxapp_zhifu_sum_old[0][0])
print("公众号今日新增支付人数:\t%s\t个" % wxapp_zhifu_sum_old[0][0])

# 访问付款转化率
# visit_zhuanhuanlv = all_zhifu_sum_and_f / all_visit_sum_and_f
# print("访问付款转化率:\t", visit_zhuanhuanlv * 100, "%")

# 门店销售额Top10
# 有时间的
sql = "SELECT a.uniacid,if(a.type='1','小程序','公众号'),sum(a.sale_prices) FROM `plus_shop_sale_visit` as a where create_date >= '2019-01-15' AND create_date <= "+new_time+"  AND a.uniacid in (" + sql_gzh_id_list + ") GROUP BY a.uniacid,a.type ORDER BY SUM(a.sale_prices) DESC "
sql = "SELECT a.uniacid,if(a.type='1','小程序','公众号'),sum(a.sale_prices) FROM `plus_shop_sale_visit` as a where  a.uniacid in (" + sql_gzh_id_list + ") GROUP BY a.uniacid,a.type ORDER BY SUM(a.sale_prices) DESC "
top_all = sql_go.lianjie_sql("plus2test", sql)
top_s = 1
top_10 = {

}
print("门店销售top10排行榜开始排名")
for top in top_all:
    top_ho = "第" + str(top_s) + "名"
    top_10[top_ho] = top
    top_s += 1
    if top_s > 10:
        break
print(top_10)
# for top_one in top_10:
#     print(top_one)
print("结束。。。")

# 新增关注
sql = "SELECT SUM(new_user) as '新增关注' FROM `plus_wechats_member_analysis` WHERE uniacid in (" + sql_gzh_id_list + ")"
new_guanzhu = sql_go.lianjie_sql("plus2test", sql)
# new_guanzhu_f = float(new_guanzhu[0][0])
print("新增关注人数：\t", new_guanzhu[0][0], "\t人")
sql = "SELECT create_date,SUM(new_user) as '新增关注' FROM `plus_wechats_member_analysis` WHERE uniacid in (" + sql_gzh_id_list + ") GROUP BY create_date"
xinzeng_guanzhu_fenxi = sql_go.lianjie_sql("plus2test", sql)
for xinzeng_guanzhu_fenxi_x in xinzeng_guanzhu_fenxi:
    print("时间：\t", xinzeng_guanzhu_fenxi_x[0], "\t新增人数：\t", xinzeng_guanzhu_fenxi_x[1])

sql = "SELECT SUM(new_user) as '新增关注' FROM `plus_wechats_member_analysis` WHERE create_date >= '2019-01-01' AND  uniacid in (" + sql_gzh_id_list + ")"
new_guanzhu = sql_go.lianjie_sql("plus2test", sql)
# new_guanzhu_f = float(new_guanzhu[0][0])
print("2019年新增关注人数：\t", new_guanzhu[0][0], "\t人")

# 取消关注
sql = "SELECT SUM(cancel_user) as '取消用户' FROM `plus_wechats_member_analysis` WHERE uniacid in (" + sql_gzh_id_list + ")"
quxiao_guanzhu = sql_go.lianjie_sql("plus2test", sql)
# quxiao_guanzhu_f = float(quxiao_guanzhu[0][0])
print("取消关注人数：\t", quxiao_guanzhu[0][0], "\t人")
sql = "SELECT create_date,SUM(cancel_user) as '取消用户' FROM `plus_wechats_member_analysis` WHERE uniacid in (" + sql_gzh_id_list + ") GROUP BY create_date"
quxiao_guanzhu_fenxi = sql_go.lianjie_sql("plus2test", sql)
for quxiao_guanzhu_fenxi_x in quxiao_guanzhu_fenxi:
    print("时间：\t", quxiao_guanzhu_fenxi_x[0], "\t取消人数：\t", quxiao_guanzhu_fenxi_x[1])

sql = "SELECT SUM(cancel_user) as '取消用户' FROM `plus_wechats_member_analysis` WHERE create_date >= '2019-01-01' AND   uniacid in (" + sql_gzh_id_list + ")"
print(sql)
quxiao_guanzhu = sql_go.lianjie_sql("plus2test", sql)
# quxiao_guanzhu_f = float(quxiao_guanzhu[0][0])
print("2019年取消关注人数：\t", quxiao_guanzhu[0][0], "\t人")

# 累计关注
sql = "SELECT SUM(cumulate_user) as '累积用户' FROM `plus_wechats_member_analysis` WHERE uniacid in (" + sql_gzh_id_list + ")"
leiji_guanzhu = sql_go.lianjie_sql("plus2test", sql)
# leiji_guanzhu_f = float(leiji_guanzhu[0][0])
print("累计关注人数：\t", leiji_guanzhu[0][0], "\t人")
sql = "SELECT create_date,SUM(cumulate_user) as '累积用户' FROM `plus_wechats_member_analysis` WHERE uniacid in (" + sql_gzh_id_list + ") GROUP BY create_date"
leiji_guanzhu_fenxi = sql_go.lianjie_sql("plus2test", sql)
for leiji_guanzhu_fenxi_x in leiji_guanzhu_fenxi:
    print("时间：\t", leiji_guanzhu_fenxi_x[0], "\t累计人数：\t", leiji_guanzhu_fenxi_x[1])

sql = "SELECT SUM(cumulate_user) as '累积用户' FROM `plus_wechats_member_analysis` WHERE create_date >= '2019-01-01' AND   uniacid in (" + sql_gzh_id_list + ")"
leiji_guanzhu = sql_go.lianjie_sql("plus2test", sql)
# leiji_guanzhu_f = float(leiji_guanzhu[0][0])
print("2019年累计关注人数：\t", leiji_guanzhu[0][0], "\t人")

# 净增关注
sql = "SELECT SUM(incr_user) as '净增关注' FROM `plus_wechats_member_analysis` WHERE uniacid in (" + sql_gzh_id_list + ")"
jingzeng_guanzhu = sql_go.lianjie_sql("plus2test", sql)
# jingzeng_guanzhu_f = float(jingzeng_guanzhu[0][0])
print("净增关注人数：\t", jingzeng_guanzhu[0][0], "\t人")
sql = "SELECT SUM(incr_user) as '净增关注' FROM `plus_wechats_member_analysis` WHERE create_date >= '2019-01-01' AND   uniacid in (" + sql_gzh_id_list + ")"
jingzeng_guanzhu = sql_go.lianjie_sql("plus2test", sql)
# jingzeng_guanzhu_f = float(jingzeng_guanzhu[0][0])
print("2019年净增关注人数：\t", jingzeng_guanzhu[0][0], "\t人")
#
sql = "SELECT create_date,SUM(new_user) as '新增关注' FROM `plus_wechats_member_analysis` WHERE uniacid in (" + sql_gzh_id_list + ") GROUP BY create_date"
jingzeng_guanzhu_fenxi = sql_go.lianjie_sql("plus2test", sql)
for jingzeng_guanzhu_fenxi_x in jingzeng_guanzhu_fenxi:
    print("时间：\t", jingzeng_guanzhu_fenxi_x[0], "\t新增人数：\t", jingzeng_guanzhu_fenxi_x[1])

# 昨日关键指标
sql = "SELECT SUM(cumulate_user) as '累积用户',SUM(new_user) as '新增用户',SUM(cancel_user) as '取消用户',SUM(incr_user) as '净增关注' FROM `plus_wechats_member_analysis` WHERE create_date >= '2019-01-20' AND   uniacid in (" + sql_gzh_id_list + ")"
zuori_shuju_tongji = sql_go.lianjie_sql("plus2test", sql)
print("昨日关键指标：")
print("累计用户\t", zuori_shuju_tongji[0][0], "\t新增用户\t", zuori_shuju_tongji[0][1], "\t取消用户\t", zuori_shuju_tongji[0][2],
      "\t净增关注\t", zuori_shuju_tongji[0][3])

# 2019年消费总人数
sql = "" + sql_gzh_id_list + ""
print(sql)
all_shop_sum = sql_go.lianjie_sql("plus2test", sql)
jingzeng_guanzhu_f_and = 0
for i in all_shop_sum:
    sql = "SELECT COUNT(DISTINCT openid) as '人数' FROM plus2test_off.`plus_middle_shop_order`  WHERE is_pay = '1' and  pay_date >= '2019-01-01' and pay_date <= "+new_time+"  AND uniacid = '" + \
          i[0] + "' "
    print(sql)
    jingzeng_guanzhu = sql_go.lianjie_sql("plus2test_off", sql)
    jingzeng_guanzhu_f = float(jingzeng_guanzhu[0][0])
    jingzeng_guanzhu_f_and = jingzeng_guanzhu_f + jingzeng_guanzhu_f_and
print("2019年消费总人数：\t", jingzeng_guanzhu_f_and, "\t人")

jingzeng_guanzhu_f_and = 0
for i in all_shop_sum:
    sql = "SELECT COUNT(DISTINCT openid) as '人数' FROM `plus_middle_shop_order`  WHERE is_pay = '1' and   uniacid = '" + \
          i[0] + "' "
    jingzeng_guanzhu = sql_go.lianjie_sql("plus2test_off", sql)
    jingzeng_guanzhu_f = float(jingzeng_guanzhu[0][0])
    jingzeng_guanzhu_f_and = jingzeng_guanzhu_f + jingzeng_guanzhu_f_and
print("年消费总人数：\t", jingzeng_guanzhu_f_and, "\t人")

sql="SELECT	COUNT(DISTINCT openid) FROM	plus_middle_shop_order WHERE	openid NOT IN (SELECT 	DISTINCT openid FROM	plus_middle_shop_order where YEAR(pay_date) < Year(NOW())	) AND uniacid in ("+sql_gzh_id_list+")"
jingzeng_guanzhu_f_and = 0
for i in all_shop_sum:
    sql = "SELECT COUNT(DISTINCT openid) as '人数' FROM `plus_middle_shop_order`  WHERE is_pay = '1' and  pay_date >= '2019-01-01'  AND uniacid = '" + \
          i[0] + "' "
    jingzeng_guanzhu = sql_go.lianjie_sql("plus2test_off", sql)
    jingzeng_guanzhu_f = float(jingzeng_guanzhu[0][0])
    jingzeng_guanzhu_f_and = jingzeng_guanzhu_f + jingzeng_guanzhu_f_and
print("2019年新增消费总人数：\t", jingzeng_guanzhu_f_and, "\t人")

# 留存
sql = "SELECT SUM(active_member_save),create_date FROM `plus_wxapp_member_active_keep` WHERE uniacid in (" + sql_gzh_id_list + ") GROUP BY create_date"
liucun = sql_go.lianjie_sql("plus2test", sql)
try:
    liucun_f = float(liucun[0][0])
    print("活跃留存：\t", liucun_f, "\t人")
except:
    print("活跃留存：\t0\t人")

# 商品数量
# ;
sql = "SELECT COUNT(id) FROM `plus_middle_shop_goods` WHERE uniacid in (" + uniacid_one + ") GROUP BY create_date"
print(sql)
goods_sum = sql_go.lianjie_sql("plus2test_off", sql)
try:
    goods_sum_f = float(goods_sum[0][0])
    print("商品数量：\t", goods_sum_f, "\t个")
except:
    print("商品数量：\t0\t个")

# 商品销售数据top10
sql = "SELECT SUM(sales_price),good_id FROM plus2test.`plus_shop_goods_salevisit` WHERE good_id in (SELECT goodsid FROM plus2test_off.`plus_middle_shop_goods` WHERE uniacid in (" + sql_gzh_id_list + ") )GROUP BY good_id ORDER BY SUM(sales_price) DESC"
print(sql)
goods_sum_sales_price = sql_go.lianjie_sql("plus2test", sql)
# print(len(goods_sum_sales_price))
goods_paihang = 0
goods_lie = 0
for goods_sum_sales_price_x in goods_sum_sales_price:
    goods_paihang += 1
    print("排行榜第", goods_paihang, "名--商品id：\t", goods_sum_sales_price[goods_lie][1], "\t商品销售额是：\t",
          goods_sum_sales_price[goods_lie][0])
    goods_lie += 1
    if goods_lie >= 10:
        break

# 访问路径
sql_shouye = "SUM(first_sum) as '首页浏览人数',SUM(first_order_sum) as '首页到确认订单数量',SUM(first_order_sum)/SUM(first_sum)*100 as '首页-确认订单比例',"
sql_list = "SUM(good_list_sum) as '商品列表页浏览人数',SUM(good_list_order_sum) as '商品列表页到确认订单数量',SUM(good_list_order_sum)/SUM(good_list_sum)*100 as '商品列表页-确认订单比例',"
sql_shoping = "SUM(shopping_sum) as '购物车页面浏览人数',SUM(shopping_order_sum) as '购物车页面到确认订单数量',SUM(shopping_order_sum)/SUM(shopping_sum)*100 as '购物车页面-确认订单比例',"
sql_goods_xiangqing = "SUM(item_sum) as '商品详情页浏览人数',SUM(item_order_sum) as '商品详情页到确认订单数量',SUM(item_order_sum)/SUM(item_sum)*100 as '商品详情页-确认订单比例',"
sql_qita = "SUM(other) as '其他页浏览人数',SUM(other_order_sum) as '其他页到确认订单数量',SUM(other_order_sum)/SUM(other)*100 as '其他页-确认订单比例',"
# 到这里是15列，角标14
sql_1 = "SUM(first_order_sum)+SUM(good_list_order_sum)+SUM(shopping_order_sum)+SUM(item_order_sum)+SUM(other_order_sum) as '计算-确认订单次数',"
sql_2 = "SUM(order_sum) as '数据库-确认订单人数',"
sql_3 = "SUM(first_sum)+SUM(good_list_sum)+SUM(shopping_sum)+SUM(item_sum)+SUM(other) as '计算-访问次数',"
sql_4 = "SUM(visit_person_sum) as '数据库-访问人数',"
sql_5 = "SUM(visit_order_sum) as '数据库-访客下单人数',"
sql_6 = "SUM(visit_order_sum)/SUM(visit_person_sum)*100 as '访客到下单转化率',"
sql_7 = "SUM(visit_pay_sum) as '数据库-付款人数',"
sql_8 = "SUM(visit_pay_sum)/SUM(visit_person_sum)*100 as '访客到付款转化率',"
sql_9 = "SUM(visit_pay_sum)/SUM(visit_order_sum)*100 as '下单到付款转化率',"
sql_10 = "SUM(order_pay_sum) as '数据库-支付成功',"
sql_11 = "SUM(order_pay_sum)/SUM(order_sum)*100 as '确认订单到支付转化率',"
sql_12 = "SUM(order_exit) as '数据库-直接退出',"
sql_13 = "SUM(order_exit)/SUM(order_sum)*100 as '确认订单到退出转化率',"
sql_14 = "SUM(order_other) as '数据库-其他操作',"
sql_15 = "SUM(order_other)/SUM(order_sum)*100 as '确认订单到其他操作转化率'"

sql = "SELECT " + sql_shouye + sql_list + sql_shoping + sql_goods_xiangqing + sql_qita + sql_1 + sql_2 + sql_3 + sql_4 + sql_5 + sql_6 + sql_7 + sql_8 + sql_9 + sql_10 + sql_11 + sql_12 + sql_13 + sql_14 + sql_15 + "FROM `plus_shop_sdk_count` WHERE uniacid in (" + sql_gzh_id_list + ")"
# print(sql)
fangwen_all = sql_go.lianjie_sql("plus2test", sql)
for fangwen_x in fangwen_all:
    print("首页浏览人数\t", fangwen_x[0], "\t转化率：\t", fangwen_x[2], "%")
    print("商品列表页浏览人数\t", fangwen_x[3], "\t转化率：\t", fangwen_x[5], "%")
    print("购物车页面浏览人数\t", fangwen_x[6], "\t转化率：\t", fangwen_x[8], "%")
    print("商品详情页浏览人数\t", fangwen_x[9], "\t转化率：\t", fangwen_x[11], "%")
    print("其他页浏览人数\t", fangwen_x[12], "\t转化率：\t", fangwen_x[14], "%")
    print("确认订单人数\t", fangwen_x[16], )
    print("支付成功人数\t", fangwen_x[24], "\t确认订单到支付转化率：\t", fangwen_x[25], "%")
    print("直接退出人数\t", fangwen_x[26], "\t确认订单到退出转化率：\t", fangwen_x[27], "%")
    print("其他操作人数\t", fangwen_x[27], "\t确认订单到其他操作转化率：\t", fangwen_x[29], "%")
    print("访客人数\t", fangwen_x[18])
    print("访客下单人数\t", fangwen_x[19])
    print("付款人数\t", fangwen_x[21])
    print("访客到下单转化率：\t", fangwen_x[20], "%")
    print("访客到付款转化率：\t", fangwen_x[22], "%")
    print("下单到付款转化率：\t", fangwen_x[23], "%")

'''
访问路径的各种计算
SUM(first_sum) as '首页浏览人数',SUM(first_order_sum) as '首页到确认订单数量',SUM(first_order_sum)/SUM(first_sum)*100 as '首页-确认订单比例',
SUM(good_list_sum) as '商品列表页浏览人数',SUM(good_list_order_sum) as '商品列表页到确认订单数量',SUM(good_list_order_sum)/SUM(good_list_sum)*100 as '商品列表页-确认订单比例',
SUM(shopping_sum) as '购物车页面浏览人数',SUM(shopping_order_sum) as '购物车页面到确认订单数量',SUM(shopping_order_sum)/SUM(shopping_sum)*100 as '购物车页面-确认订单比例',
SUM(item_sum) as '商品详情页浏览人数',SUM(item_order_sum) as '商品详情页到确认订单数量',SUM(item_order_sum)/SUM(item_sum)*100 as '商品详情页-确认订单比例',
SUM(other) as '其他页浏览人数',SUM(other_order_sum) as '其他页到确认订单数量',SUM(other_order_sum)/SUM(other)*100 as '其他页-确认订单比例',
SUM(first_order_sum)+SUM(good_list_order_sum)+SUM(shopping_order_sum)+SUM(item_order_sum)+SUM(other_order_sum) as '计算-确认订单次数',
SUM(order_sum) as '数据库-确认订单人数',
SUM(first_sum)+SUM(good_list_sum)+SUM(shopping_sum)+SUM(item_sum)+SUM(other) as '计算-访问次数',
SUM(visit_person_sum) as '数据库-访问人数',SUM(visit_order_sum) as '数据库-访客下单人数',
SUM(visit_order_sum)/SUM(visit_person_sum)*100 as '访客到下单转化率',
SUM(visit_pay_sum) as '数据库-付款人数',
SUM(visit_pay_sum)/SUM(visit_person_sum)*100 as '访客到付款转化率',
SUM(visit_pay_sum)/SUM(visit_order_sum)*100 as '下单到付款转化率',
SUM(order_pay_sum) as '数据库-支付成功',
SUM(order_pay_sum)/SUM(order_sum)*100 as '确认订单到支付转化率',
SUM(order_exit) as '数据库-直接退出',
SUM(order_exit)/SUM(order_sum)*100 as '确认订单到退出转化率',
SUM(order_other) as '数据库-其他操作',
SUM(order_other)/SUM(order_sum)*100 as '确认订单到其他操作转化率'
'''

# 指定公众号数据看板--转化详情、转化趋势图
sql = "SELECT SUM(pay_person_sum)/SUM(visit_person_sum)*100 as '访客到付款转化率' FROM `plus_shop_sale_visit` WHERE uniacid = "+uniacid_one+" and type ='1' and create_date >= '2019-01-10' AND create_date <= "+new_time
fangwen_all3 = sql_go.lianjie_sql("plus2test", sql)
for fangwen_x3 in fangwen_all3:
    print("该公众号id访客到付款转化率\t", fangwen_x3[0], "%")
sql = "SELECT SUM(pay_person_sum) as '支付人数',SUM(visit_person_sum) as '访客人数',SUM(pay_person_sum)/SUM(visit_person_sum)*100 as '访客到付款转化率',create_date FROM `plus_shop_sale_visit` WHERE uniacid = "+uniacid_one+" and type ='1' and create_date >= '2019-01-10' AND create_date <= "+new_time+"  GROUP BY create_date"
fangwen_all2 = sql_go.lianjie_sql("plus2test", sql)
for fangwen_x2 in fangwen_all2:
    print("日期:\t", fangwen_x2[3], "该公众号id支付人数:\t", fangwen_x2[0], "人", "该公众号id访客人数:\t", fangwen_x2[1], "人",
          "该公众号id访客到付款转化率:\t", fangwen_x2[2], "%")

# 交易分析
sql = "SELECT SUM(sale_prices) as '付款金额',SUM(pay_order_sum) as '付款订单数',SUM(pay_person_sum) as '付款人数',SUM(pay_person_sum)/SUM(order_person_sum)*100 as '下单付款转化率',SUM(visit_person_sum) as '访客人数',SUM(pay_person_sum)/SUM(visit_person_sum)*100 as '访客付款转化率'," \
      "SUM(order_person_sum) as '下单人数',SUM(order_sum) as '下单次数',SUM(order_person_sum)/SUM(visit_person_sum)*100 as '访客下单转化率',SUM(order_prices) as '订单金额' FROM plus_shop_sale_visit where create_date >='2019-01-14' AND create_date <="+new_time+"  AND  uniacid in  (" + sql_gzh_id_list + ")"
jiaoyifenxi_all = sql_go.lianjie_sql("plus2test", sql)
for jiaoyifenxi_x in jiaoyifenxi_all:
    print("全部付款金额\t", jiaoyifenxi_x[0])
    print("全部付款订单数\t", jiaoyifenxi_x[1])
    print("全部付款人数\t", jiaoyifenxi_x[2])
    print("全部下单付款转化率\t", jiaoyifenxi_x[3])
    print("全部访客人数\t", jiaoyifenxi_x[4])
    print("全部访客付款转化率\t", jiaoyifenxi_x[5])
    print("全部下单人数\t", jiaoyifenxi_x[6])
    print("全部下单次数\t", jiaoyifenxi_x[7])
    print("全部访客下单转化率\t", jiaoyifenxi_x[8])
    print("全部订单金额\t", jiaoyifenxi_x[9])
    # all_xiaoshoue = float(jiaoyifenxi_x[0])

# 小程序交易分析
sql = "SELECT SUM(sale_prices) as '付款金额',SUM(pay_order_sum) as '付款订单数',SUM(pay_person_sum) as '付款人数',SUM(pay_person_sum)/SUM(order_person_sum)*100 as '下单付款转化率',SUM(visit_person_sum) as '访客人数',SUM(pay_person_sum)/SUM(visit_person_sum)*100 as '访客付款转化率'," \
      "SUM(order_person_sum) as '下单人数',SUM(order_sum) as '下单次数',SUM(order_person_sum)/SUM(visit_person_sum)*100 as '访客下单转化率',SUM(order_prices) as '订单金额' FROM plus_shop_sale_visit where create_date >='2019-01-14' AND create_date <="+new_time+"  AND type ='1' AND  uniacid in  (" + sql_gzh_id_list + ")"
jiaoyifenxi_all2 = sql_go.lianjie_sql("plus2test", sql)
for jiaoyifenxi_x_x in jiaoyifenxi_all2:
    print("小程序付款金额\t", jiaoyifenxi_x_x[0])
    print("小程序付款订单数\t", jiaoyifenxi_x_x[1])
    print("小程序付款人数\t", jiaoyifenxi_x_x[2])
    print("小程序下单付款转化率\t", jiaoyifenxi_x_x[3])
    print("小程序访客人数\t", jiaoyifenxi_x_x[4])
    print("小程序访客付款转化率\t", jiaoyifenxi_x_x[5])
    print("小程序下单人数\t", jiaoyifenxi_x_x[6])
    print("小程序下单次数\t", jiaoyifenxi_x_x[7])
    print("小程序访客下单转化率\t", jiaoyifenxi_x_x[8])
    print("小程序订单金额\t", jiaoyifenxi_x_x[9])
    # xiao_xiaoshoue = float(jiaoyifenxi_x_x[0])

# 公众号交易分析
sql = "SELECT SUM(sale_prices) as '付款金额',SUM(pay_order_sum) as '付款订单数',SUM(pay_person_sum) as '付款人数',SUM(pay_person_sum)/SUM(order_person_sum)*100 as '下单付款转化率',SUM(visit_person_sum) as '访客人数',SUM(pay_person_sum)/SUM(visit_person_sum)*100 as '访客付款转化率'," \
      "SUM(order_person_sum) as '下单人数',SUM(order_sum) as '下单次数',SUM(order_person_sum)/SUM(visit_person_sum)*100 as '访客下单转化率',SUM(order_prices) as '订单金额' FROM plus_shop_sale_visit where create_date >='2019-01-14' AND create_date <="+new_time+"  AND type ='2' AND  uniacid in  (" + sql_gzh_id_list + ")"
jiaoyifenxi_all3 = sql_go.lianjie_sql("plus2test", sql)
for jiaoyifenxi_x_g in jiaoyifenxi_all3:
    print("公众号付款金额\t", jiaoyifenxi_x_g[0])
    print("公众号付款订单数\t", jiaoyifenxi_x_g[1])
    print("公众号付款人数\t", jiaoyifenxi_x_g[2])
    print("公众号下单付款转化率\t", jiaoyifenxi_x_g[3])
    print("公众号访客人数\t", jiaoyifenxi_x_g[4])
    print("公众号访客付款转化率\t", jiaoyifenxi_x_g[5])
    print("公众号下单人数\t", jiaoyifenxi_x_g[6])
    print("公众号下单次数\t", jiaoyifenxi_x_g[7])
    print("公众号访客下单转化率\t", jiaoyifenxi_x_g[8])
    print("公众号订单金额\t", jiaoyifenxi_x_g[9])
    # wxapp_xiaoshoue = float(jiaoyifenxi_x_x[0])

# if wxapp_xiaoshoue + xiao_xiaoshoue == all_xiaoshoue:
#     print("交易分析数据正确，开始对比：")

#
# 交易皱势
sql = "SELECT SUM(sale_prices) as '付款金额',SUM(pay_order_sum) as '付款订单数',SUM(pay_person_sum) as '付款人数',SUM(pay_person_sum)/SUM(order_person_sum)*100 as '下单付款转化率',SUM(pay_person_sum)/SUM(visit_person_sum)*100 as '访客付款转化率',SUM(order_person_sum)/SUM(visit_person_sum)*100 as '访客下单转化率',create_date FROM plus_shop_sale_visit where uniacid in  (" + sql_gzh_id_list + ") GROUP BY create_date"
jiaoyizhoushi_all4 = sql_go.lianjie_sql("plus2test", sql)
for jiaoyizhoushi_x in jiaoyizhoushi_all4:
    print("日期:\t", jiaoyizhoushi_x[6])
    print("全部付款金额\t", jiaoyizhoushi_x[0])
    print("全部付款订单数\t", jiaoyizhoushi_x[1])
    print("全部付款人数\t", jiaoyizhoushi_x[2])
    print("全部下单付款转化率\t", jiaoyizhoushi_x[3])
    print("全部访客付款转化率\t", jiaoyizhoushi_x[4])
    print("全部访客下单转化率\t", jiaoyizhoushi_x[5])

sql = "SELECT SUM(sale_prices) as '付款金额',SUM(pay_order_sum) as '付款订单数',SUM(pay_person_sum) as '付款人数',SUM(pay_person_sum)/SUM(order_person_sum)*100 as '下单付款转化率',SUM(pay_person_sum)/SUM(visit_person_sum)*100 as '访客付款转化率',SUM(order_person_sum)/SUM(visit_person_sum)*100 as '访客下单转化率',create_date FROM plus_shop_sale_visit where type='1' AND uniacid in  (" + sql_gzh_id_list + ") GROUP BY create_date"
jiaoyizhoushi_all5 = sql_go.lianjie_sql("plus2test", sql)
for jiaoyizhoushi_x_x in jiaoyizhoushi_all5:
    print("日期:\t", jiaoyizhoushi_x_x[6])
    print("小程序付款金额\t", jiaoyizhoushi_x_x[0])
    print("小程序付款订单数\t", jiaoyizhoushi_x_x[1])
    print("小程序付款人数\t", jiaoyizhoushi_x_x[2])
    print("小程序下单付款转化率\t", jiaoyizhoushi_x_x[3])
    print("小程序访客付款转化率\t", jiaoyizhoushi_x_x[4])
    print("小程序访客下单转化率\t", jiaoyizhoushi_x_x[5])

sql = "SELECT SUM(sale_prices) as '付款金额',SUM(pay_order_sum) as '付款订单数',SUM(pay_person_sum) as '付款人数',SUM(pay_person_sum)/SUM(order_person_sum)*100 as '下单付款转化率',SUM(pay_person_sum)/SUM(visit_person_sum)*100 as '访客付款转化率',SUM(order_person_sum)/SUM(visit_person_sum)*100 as '访客下单转化率',create_date FROM plus_shop_sale_visit where type='2' AND uniacid in  (" + sql_gzh_id_list + ") GROUP BY create_date"
jiaoyizhoushi_all6 = sql_go.lianjie_sql("plus2test", sql)
for jiaoyizhoushi_x_g in jiaoyizhoushi_all6:
    print("日期:\t", jiaoyizhoushi_x_g[6])
    print("公众号付款金额\t", jiaoyizhoushi_x_g[0])
    print("公众号付款订单数\t", jiaoyizhoushi_x_g[1])
    print("公众号付款人数\t", jiaoyizhoushi_x_g[2])
    print("公众号下单付款转化率\t", jiaoyizhoushi_x_g[3])
    print("公众号访客付款转化率\t", jiaoyizhoushi_x_g[4])
    print("公众号访客下单转化率\t", jiaoyizhoushi_x_g[5])

# 交易构成-是否小程序
data = "create_date >='2019-01-01' AND create_date <="+new_time
sql = "SELECT SUM(sale_prices) as '付款金额',type FROM plus_shop_sale_visit where " + data + " and uniacid in (" + sql_gzh_id_list + ") GROUP BY type"
jiaoyigoucheng_all = sql_go.lianjie_sql("plus2test", sql)
sql = "SELECT SUM(sale_prices) as '付款金额',SUM(new_member_prices_sum) as '新客户销售额',SUM(old_member_prices_sum) as '老客户销售额',SUM(new_member_prices_sum)/(SUM(new_member_prices_sum)+SUM(old_member_prices_sum))*100 as '新客户销售额占比', SUM(old_member_prices_sum)/(SUM(new_member_prices_sum)+SUM(old_member_prices_sum))*100  as '老客户销售额占比' FROM plus_shop_sale_visit where " + data + " and uniacid in (" + sql_gzh_id_list + ") "
print("新老客户",sql)
jiaoyigoucheng_all_and = sql_go.lianjie_sql("plus2test", sql)

jiaoyigoucheng_all_and_xx = jiaoyigoucheng_all_and[0][0]


for jiaoyigoucheng_x_g in jiaoyigoucheng_all:
    if 1 == jiaoyigoucheng_x_g[1]:
        print("小程序付款金额：\t", jiaoyigoucheng_x_g[0], "\t比例是：\t", jiaoyigoucheng_x_g[0] / jiaoyigoucheng_all_and_xx * 100,
              "%")
    else:
        print("公众号付款金额：\t", jiaoyigoucheng_x_g[0], "\t比例是：\t", jiaoyigoucheng_x_g[0] / jiaoyigoucheng_all_and_xx * 100,
              "%")
print("新客户付款金额：\t", jiaoyigoucheng_all_and[0][1], "\t比例是：\t", jiaoyigoucheng_all_and[0][3], "%")
print("老客户付款金额：\t", jiaoyigoucheng_all_and[0][2], "\t比例是：\t", jiaoyigoucheng_all_and[0][4], "%")

# 省份排行：
data = "create_date >= '2019-01-01' AND create_date <= "+new_time+"  AND"
sql = "SELECT province,SUM(sale_prices) FROM `plus_province_sales` WHERE " + data + " uniacid in (" + sql_gzh_id_list + ")GROUP BY province ORDER BY SUM(sale_prices) desc"
paihang_all = sql_go.lianjie_sql("plus2test", sql)
paihang_s = 1
print("排行榜输出...")
for paihang_x in paihang_all:
    print("全部排行第", paihang_s, "的省份是：\t", paihang_x[0], "\t付款金额：\t", paihang_x[1])
    paihang_s += 1
print("输出结束......")

# data = "create_date >= '2019-01-11' AND create_date <= '2019-01-24' AND"
sql = "SELECT province,SUM(sale_prices) FROM `plus_province_sales` WHERE " + data + " type = '1' AND uniacid in (" + sql_gzh_id_list + ")GROUP BY province ORDER BY SUM(sale_prices) desc"
paihang_all_x = sql_go.lianjie_sql("plus2test", sql)
paihang_s = 1
print("小程序排行榜输出...")
for paihang_x_x in paihang_all_x:
    print("小程序排行第", paihang_s, "的省份是：\t", paihang_x_x[0], "\t付款金额：\t", paihang_x_x[1])
    paihang_s += 1
print("输出结束......")

# data = "create_date >= '2019-01-11' AND create_date <= '2019-01-24' AND"
sql = "SELECT province,SUM(sale_prices) FROM `plus_province_sales` WHERE " + data + " type = '2' AND uniacid in (" + sql_gzh_id_list + ")GROUP BY province ORDER BY SUM(sale_prices) desc"
paihang_all_g = sql_go.lianjie_sql("plus2test", sql)
paihang_s = 1
print("公众号排行榜输出...")
for paihang_x_g in paihang_all_g:
    print("公众号排行第", paihang_s, "的省份是：\t", paihang_x_g[0], "\t付款金额：\t", paihang_x_g[1])
    paihang_s += 1
print("输出结束......")

# 访问量日期
sql = "SELECT create_date,SUM(visit_person_sum) FROM `plus_shop_sale_visit` WHERE uniacid in (" + sql_gzh_id_list + ") GROUP BY create_date"
fangwenliang_riqi = sql_go.lianjie_sql("plus2test", sql)
print("访问量统计")
for fangwenliang_xiangjie in fangwenliang_riqi:
    print(fangwenliang_xiangjie)
print("结束统计...")

sql = "SELECT create_date,SUM(visit_person_sum),IF(type='1','小程序','公众号') FROM `plus_shop_sale_visit` WHERE uniacid in (" + sql_gzh_id_list + ") GROUP BY create_date,type"
fangwenliang_riqi_type = sql_go.lianjie_sql("plus2test", sql)
print("访问量统计")
for fangwenliang_xiangjie_type in fangwenliang_riqi_type:
    print(fangwenliang_xiangjie_type)
print("结束统计...")

# 店铺排行数据
# data = "create_date >= '2019-01-11' AND create_date <= '2019-01-24' AND"
sql = "SELECT uniacid,IF(type='1','小程序','公众号'),SUM(sale_prices) as '销售额',SUM(visit_person_sum) as '访问量' FROM `plus_shop_sale_visit` WHERE " + data + " uniacid in (" + sql_gzh_id_list + ")GROUP BY uniacid,type ORDER BY SUM(sale_prices) DESC"
dianpu_paihang_all = sql_go.lianjie_sql("plus2test", sql)
paihang_s = 1
for dianpu_paihang in dianpu_paihang_all:
    print("全部排行第", paihang_s, "的店铺是：\t", dianpu_paihang[0], "\t属于：\t", dianpu_paihang[1], "\t付款金额：\t",
          dianpu_paihang[2])
    paihang_s += 1

# 小程序排行榜
sql = "SELECT uniacid,visit_total as '累计用户数' ,session_cnt as '打开次数',visit_uv_new as '新增访问人数',share_uv as '转发人数' FROM `plus_wxapp_visit` WHERE uniacid in(SELECT uniacid FROM plus_shop_info WHERE user_id in (SELECT user_id FROM plus_users WHERE user_id "+user_id+"))and create_date = "+new_time+"  ORDER BY visit_total DESC "
dianpu_paihang_xiao_xiao = sql_go.lianjie_sql("plus2test", sql)
paihang_s = 1
for dianpu_paihang_xiao in dianpu_paihang_xiao_xiao:
    print("小程序排行第", paihang_s, "的店铺是：\t", dianpu_paihang_xiao[0], "\t累计用户数：\t", dianpu_paihang_xiao[1], "\t打开次数：\t",
          dianpu_paihang_xiao[2], "\t新增访问人数：\t", dianpu_paihang_xiao[2], "\t转发人数：\t", dianpu_paihang_xiao[2])
    paihang_s += 1
print("jieshu")
# 驻留
'''
SELECT SUM(visit_uv_new) FROM `plus_wxapp_visit` WHERE
uniacid in(
SELECT uniacid FROM plus_shop_info WHERE user_id in (
SELECT user_id FROM plus_users WHERE user_id "+user_id+"
))



'''