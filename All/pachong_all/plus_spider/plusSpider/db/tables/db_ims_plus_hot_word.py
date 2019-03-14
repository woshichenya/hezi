# -*- coding: UTF-8 -*-
# *******************************************************************************************
# **  创 建 者: tangyongchun
# **  创建日期: 2018-11-13
#
# **  文件名称：db_ims_plus_hot_word.py
# **  功能描述：实现插入、更新功能
# **
# ********************************************************************************************


from plusSpider.db.tableModel.db_base_model import ImsPlusHotWord
from plusSpider.db.utils import db_util


class VdImsPlusHotWord(object):

    def __init__(self, data_source):
        self.data_source = data_source

    def insert_word(self):
        """ 插入热词数据 """
        try:
            if self.select_word(self.data_source['title']) == 0:
                db_util.insert(ImsPlusHotWord, [self.data_source])
            else:
                word = db_util.ImsPlusHotWord
                word.update(gzh_class=self.data_source['gzh_class'],
                            gzh_article_read=self.data_source['gzh_article_read']) \
                    .where(word.title == self.data_source['title']).execute()
        except Exception as e:
            print 'VdImsPlusHotWord 插入热词数据异常', e

    def update_word(self):
        """ 更新热词数据 """
        try:
            if self.select_word(self.data_source['title']) == 0:
                db_util.insert(ImsPlusHotWord, [self.data_source])
            else:
                word = db_util.ImsPlusHotWord
                word.update(hot_rank=self.data_source['hot_rank']).where(
                    word.title == self.data_source['title']).execute()
        except Exception as e:
            print 'VdImsPlusHotWord 更新热词数据异常', e

    def select_word(self, keyword):
        """ 查询热词信息 """
        try:
            word = db_util.ImsPlusHotWord
            word_list = word.select().where(word.title == keyword)
            return len(word_list)
        except Exception as e:
            print 'VdImsPlusHotWord 查询热词数据异常', e
