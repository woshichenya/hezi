# -*- coding: UTF-8 -*-

from data_stats.all_table_compute.data_compute.data_weichen_module_stats import DataWeichenModuleStatsCompute
from data_stats.all_table_compute.data_source.db_source.weichen_module import DataWeichenModuleSource
from data_stats.all_table_compute.data_source.db_source.weichen_module_stats import DataWeichenModuleStatsSource
from data_stats.utils.date_utils import get_date_by_date


class DataWeichenModuleStats(object):
    _data = []
    def __init__(self,query_date):
        self.query_date = query_date

    def _compute_field(self,field,type,module_name,weichen_version):
        field['type'] = type
        field['total_user'] = DataWeichenModuleStatsCompute(type, module_name, weichen_version).total_user()
        last_info = DataWeichenModuleStatsSource().get_module_info_someday(get_date_by_date(self.query_date),
                                                                           module_name, weichen_version, type) #上一天的数据
        last_total_user = 0
        if last_info is not None:
            last_total_user = last_info['total_user']

        field['new_user'] = (field['total_user'] - last_total_user) if (field['total_user'] - last_total_user)>0 else 0 #今天减去昨天的用户数为新增用户 如果值为负则算为0
        return field

    def set_data(self):
        module_list = DataWeichenModuleSource().select_module_list()
        for item in module_list:
            field = {
                'module_name': item.module_name,
                'module_title': item.module_title,
                'weichen_version': item.weichen_version,
                'create_date': self.query_date,
            }
            if item.app_support == 2: #如果该插件支持微信公众号
                self._data.append(self._compute_field(field,2,item.module_name,item.weichen_version))

            if item.wxapp_support == 2: #如果该插件支持小程序
                self._data.append(self._compute_field(field,1,item.module_name,item.weichen_version))

    def get_data(self):
        self.set_data()
        return self._data
