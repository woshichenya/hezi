# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from plusSpider.db.tables.db_ims_plus_hot_gzh import VdImsPlusHotGzh
from plusSpider.db.tables.db_ims_plus_hot_gzh_info import VdImsPlusHotGzhInfo
from plusSpider.db.tables.db_ims_plus_hot_word import VdImsPlusHotWord
from plusSpider.db.tables.db_ims_plus_hot_word_info import VdImsPlusHotWordInfo
from plusSpider.items import PlusspiderItem, PlusspiderlineItem, PlusspiderPieItem, PlusspiderPieUpdateItem, \
    PlusspiderGzhItem, PlusspiderGzhUpdateItem, PlusspiderGzhInfoItem, PlusspiderGzhInfoUpdateItem
from plusSpider.db.tables.db_ims_plus_hot_article import VdImsPlusHotArticle


class PlusspiderPipeline(object):
    """ 文章信息 """

    def process_item(self, item, spider):
        if isinstance(item, PlusspiderItem):
            VdImsPlusHotArticle(item).insert_article()
        return item


class PlusspiderPipelineIno(object):
    """ 热词图表信息 """

    def process_item(self, item, spider):
        if isinstance(item, PlusspiderlineItem):
            VdImsPlusHotWordInfo(item).insert_word_info()
        return item


class PlusspiderPipePieIno(object):
    """ 热词信息 """

    def process_item(self, item, spider):
        if isinstance(item, PlusspiderPieItem):
            VdImsPlusHotWord(item).insert_word()
        return item


class PlusspiderPipePieUpdateIno(object):
    """ 更新热词表中的热点排名字段 """

    def process_item(self, item, spider):
        if isinstance(item, PlusspiderPieUpdateItem):
            VdImsPlusHotWord(item).update_word()
        return item


class PlusspiderPipeGzh(object):
    """ 保存公众号 """

    def process_item(self, item, spider):
        if isinstance(item, PlusspiderGzhItem):
            VdImsPlusHotGzh(item).insert_gzh()
        return item


class PlusspiderPipeGzhUpdate(object):
    """ 更新公众号 """

    def process_item(self, item, spider):
        if isinstance(item, PlusspiderGzhUpdateItem):
            VdImsPlusHotGzh(item).update_gzh()
        return item


class PlusspiderPipeGzhInfo(object):
    """ 保存公众号信息 """

    def process_item(self, item, spider):
        if isinstance(item, PlusspiderGzhInfoItem):
            VdImsPlusHotGzhInfo(item).insert_gzh_info()
        return item


class PlusspiderPipeGzhInfoUpdate(object):
    """ 更新公众号信息 """

    def process_item(self, item, spider):
        if isinstance(item, PlusspiderGzhInfoUpdateItem):
            VdImsPlusHotGzhInfo(item).update_gzh_info()
        return item
