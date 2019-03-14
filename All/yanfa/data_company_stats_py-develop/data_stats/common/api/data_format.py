# -*- coding: UTF-8 -*-
# **  文件名称：data_format.py
# **  功能描述：list转dict
# **
# **  创建者:   Yunlong.Zhao zhaoyunlong@vdongchina.com
# **  创建日期: 2018/10/25 20:49


def list_for_dict(coll,data):
    data_list = []
    for da in range(0,len(data)):
        data_source = dict(zip(coll,data[da]))
        data_list.append(data_source)
    return data_list

