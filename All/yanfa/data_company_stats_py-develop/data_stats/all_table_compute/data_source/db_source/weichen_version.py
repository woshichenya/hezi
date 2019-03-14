# -*- coding: UTF-8 -*-

from data_stats.tableModel.db_base_model import DataWeichenVersion


class DataWeichenVersionSource(object):

    def __init__(self):
        self._table = DataWeichenVersion

    def select_version_list(self,is_free):
        '''微尘付费版本列表'''
        return self._table().select().where(self._table.is_free==is_free)
