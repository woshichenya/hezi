# -*- coding: UTF-8 -*-
# *******************************************************************************************
# **  文件名称：db_util.py
# **  功能描述：数据库工具类
# **
# **  创 建 者: tangyongchun
# **  创建日期: 2018-11-13
# ********************************************************************************************

from plusSpider.db.tableModel.db_base_model import *

database.connect()  # 建立连接


def insert(model, data_source):
    """ 每次批量插入100条 """
    for i in range(0, len(data_source), 100):
        model.insert_many(data_source[i:i + 1000]).on_conflict_replace().execute()
    database.close()
