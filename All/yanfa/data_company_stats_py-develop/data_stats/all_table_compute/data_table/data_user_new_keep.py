# -*- coding: UTF-8 -*-

from data_stats.all_table_compute.data_compute.data_user_new_keep import DataUserNewKeepCompute


class DataUserNewKeep(object):
    _data = []

    def __init__(self,query_date):
        self.query_date = query_date

    def set_data(self):
        field = {
            'new_user' : DataUserNewKeepCompute(self.query_date).new_user(),
            'create_date' : self.query_date
        }
        self._data.append(field)

        next_save = DataUserNewKeepCompute(self.query_date).next_save_user()
        if next_save is not None:
            self._data.append(next_save)

        third_save = DataUserNewKeepCompute(self.query_date).third_save_user()
        if third_save is not None:
            self._data.append(third_save)

        seventh_save = DataUserNewKeepCompute(self.query_date).seventh_save_user()
        if seventh_save is not None:
            self._data.append(seventh_save)

        thirtieth_save = DataUserNewKeepCompute(self.query_date).thirtieth_save_user()
        if thirtieth_save is not None:
            self._data.append(thirtieth_save)

    def get_data(self):
        self.set_data()
        return self._data
