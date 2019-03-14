# -*- coding: UTF-8 -*-
# 每天0点清除前一天的实时数据
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))));
from plus_vdong.tableModel.db_base_model import database
cursor=database.cursor()
plus_shop_realtime_data = "truncate table plus_shop_realtime_data"
cursor.execute(plus_shop_realtime_data)
cursor.close()

