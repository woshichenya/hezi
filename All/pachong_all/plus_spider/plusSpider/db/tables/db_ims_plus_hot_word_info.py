# -*- coding: UTF-8 -*-
# *******************************************************************************************
# **  创 建 者: tangyongchun
# **  创建日期: 2018-11-13
#
# **  文件名称：db_ims_plus_hot_word_info.py
# **  功能描述：实现插入、更新功能
# **
# ********************************************************************************************

from plusSpider.db.tableModel.db_base_model import ImsPlusHotWordInfo
from plusSpider.db.utils import db_util


class VdImsPlusHotWordInfo(object):

    def __init__(self, data_source):
        self.data_source = data_source

    def insert_word_info(self):
        """ 插入热词信息 """
        try:
            db_util.insert(ImsPlusHotWordInfo, [self.data_source])
        except Exception as e:
            print 'VdImsPlusHotWordInfo 插入热词信息异常', e
