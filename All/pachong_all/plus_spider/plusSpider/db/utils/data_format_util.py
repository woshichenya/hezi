# -*- coding: UTF-8 -*-
# *******************************************************************************************
# **  创 建 者: tangyongchun
# **  创建日期: 2018-11-13
#
# **  文件名称：data_format_util.py
# **  功能描述：数据格式工具
# **
# ********************************************************************************************


def list_for_dict(coll, data):
    data_list = []
    for i in range(0, len(data)):
        data_source = dict(zip(coll, data[i]))
        data_list.append(data_source)
    return data_list
