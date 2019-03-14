# -*- coding: UTF-8 -*-

from data_stats.tableModel.db_base_model import DataWeichenModule


class DataWeichenModuleSource(object):

    def __init__(self):
        self._table = DataWeichenModule

    def select_module_list(self):
        '''微尘插件列表'''
        return self._table().select()

    def count_module_total(self):
        '''微尘插件总数'''
        return self._table().select().count()

    def count_wxapp_module_total(self):
        '''微尘小程序插件总数'''
        return self._table().select().where(self._table.wxapp_support == 2).count()

    def count_app_module_total(self):
        '''微尘公众号插件总数'''
        return self._table().select().where(self._table.app_support == 2).count()