# -*- coding: UTF-8 -*-
from data_stats.all_table_compute.data_source.db_source.weichen_app_module import DataWeichenAppModuleSource
from data_stats.all_table_compute.data_source.db_source.weichen_wxapp_module import DataWeichenWxappModuleSource
from data_stats.utils.date_utils import get_date_by_date

class DataWeichenModuleStatsCompute(object):

    def __init__(self,type,module_name,weichen_version):
        self.source = DataWeichenWxappModuleSource() if type == 1 else DataWeichenAppModuleSource()
        self.module_name = module_name
        self.weichen_version = weichen_version

    def total_user(self):
        return self.source.count_module_use(self.module_name,self.weichen_version)

