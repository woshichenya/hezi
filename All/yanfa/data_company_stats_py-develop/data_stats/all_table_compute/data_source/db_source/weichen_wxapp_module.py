# -*- coding: UTF-8 -*-

from data_stats.tableModel.db_base_model import DataWeichenWxappModule


class DataWeichenWxappModuleSource(object):

    def __init__(self):
        self._table = DataWeichenWxappModule

    def count_module_use(self,module_name,weichen_version):
        '''使用该插件的小程序数量'''
        return self._table().select().where((self._table.module_name == module_name) & (weichen_version == weichen_version)).count()

