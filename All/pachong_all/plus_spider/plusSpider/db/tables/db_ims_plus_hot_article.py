# -*- coding: UTF-8 -*-
# *******************************************************************************************
# **  创 建 者: tangyongchun
# **  创建日期: 2018-11-13
#
# **  文件名称：db_ims_plus_hot_article.py
# **  功能描述：实现插入、更新功能
# **
# ********************************************************************************************

from plusSpider.db.tableModel.db_base_model import ImsPlusHotArticle
from plusSpider.db.utils import db_util


class VdImsPlusHotArticle(object):

    def __init__(self, data_source):
        self.data_source = data_source

    def insert_article(self):
        """ 插入文章信息 """
        try:
            db_util.insert(ImsPlusHotArticle, [self.data_source])
        except Exception as e:
            print 'VdImsPlusHotArticle 插入文章信息异常', e

    def update_article(self):
        """ 更新文章信息 """
        try:
            data_source = self.data_source
            article = db_util.ImsPlusHotArticle
            for i in range(0, len(data_source)):
                data = data_source[i]
                article.update(url=data[1], read_sum=data[3], agree_sum=data[4], is_first=data[5], hot_word_id=data[6],
                               article_class=data[7], create_time=data[8]) \
                    .where(article.title == data[0]).execute()
        except Exception as e:
            print 'VdImsPlusHotArticle 更新文章信息异常', e
