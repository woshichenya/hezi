# -*- coding: UTF-8 -*-

from data_stats.all_table_compute.data_compute.data_user_province import DataUserProvinceCompute


class DataUserProvince(object):
    _data = []

    def set_data(self):
        data = []
        list = DataUserProvinceCompute().user_province_list()
        for key in list:
            field = {'province':key,'user_count':list[key]}
            data.append(field)
        self._data.append(data)

    def get_data(self):
        self.set_data()
        return self._data
