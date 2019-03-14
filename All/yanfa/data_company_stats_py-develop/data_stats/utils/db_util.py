# -*- coding: UTF-8 -*-
# **  文件名称：db_util.py
# **  功能描述：数据库工具类
# **
# **  创建者:   Yunlong.Zhao zhaoyunlong@vdongchina.com
# **  创建日期: 2018/10/25 21:04
import sys

sys.path.append("..")
from data_stats.tableModel.db_base_model import *

database.connect()


def insert(model, data_source):
    """ 插入 批量每次插入100条"""
    for i in range(0, len(data_source), 100):
        model.insert_many(data_source[i:i + 1000]).on_conflict_replace().execute()
    database.close()

def update_by_type_uniacid(model, data_source):

    for data in data_source:
        # print data
        model.update(data).where((model.type == data["type"]) & (model.uniacid == data["uniacid"])).execute()
    database.close()

def update_by_plus_versions_uniacid(model, data_source):

    for data in data_source:
        # print data
        model.update(data).where((model.uniacid == data["uniacid"]) & (model.plus_versions == data["plus_versions"]) ).execute()
    database.close()

#获取所有的小程序key
def query_all_wxapp():
    result = PlusWxappInfo.select(PlusWxappInfo.key,PlusWxappInfo.secret,PlusWxappInfo.uniacid).group_by(PlusWxappInfo.key)
    database.close()
    return result


def query_all_wechats():
    result = PlusWechatsInfo.select(PlusWechatsInfo.key, PlusWechatsInfo.secret, PlusWechatsInfo.uniacid).group_by(
        PlusWechatsInfo.key)
    database.close()
    return result



