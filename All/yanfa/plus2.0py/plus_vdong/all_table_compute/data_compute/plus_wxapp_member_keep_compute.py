# -*- coding: UTF-8 -*-
from plus_vdong.all_table_compute.data_source.es_source import general_template as g_t
from plus_vdong.common.static import public_args as p_a
from plus_vdong.utils import date_utils

class EsPlusWxappMemberKeepCompute(object):
    index_name_user = p_a.index_dict["applet"][3]

    def __init__(self, app_key, day):
        self.app_key = app_key
        self.day = day
        new_user = g_t.query_id(self.app_key, self.index_name_user, self.day, "all")
        self.active_user_list = set([])
        self.new_user_num = 0
        if new_user is not None:
            self.new_user_num = new_user["_source"]["new_user_num"]
            self.active_user_list = set(new_user["_source"]["active_user_list"])
        self.dict_7_14_30 = self.get_7_14_30()

    def get_7_14_30(self):
        dict_7_14_30 = {}
        _ids = []
        for i in range(1, 8):
            befor_day = date_utils.param_day_yesterday(self.day, -i)
            dict_7_14_30[befor_day] = {}
            _ids.append(befor_day)
        _ids.append(date_utils.param_day_yesterday(self.day, -14))
        dict_7_14_30[date_utils.param_day_yesterday(self.day, -14)] = {}
        _ids.append(date_utils.param_day_yesterday(self.day, -30))
        dict_7_14_30[date_utils.param_day_yesterday(self.day, -30)] = {}
        req_json = g_t.query_ids(self.app_key, self.index_name_user, "all", _ids)
        if req_json is None:
            return dict_7_14_30
        for hit in req_json['hits']['hits']:
            dict_7_14_30[hit['_id']] = hit
        return dict_7_14_30


    def new_member_save(self):
        return [self.app_key, self.new_user_num, self.day]

    def one_day_later(self):
        day = date_utils.param_day_yesterday(self.day, -1)
        req_json = self.dict_7_14_30[day]
        if not req_json: # 时空的情况
            return {}
        new_user_list = set(req_json["_source"]["new_user_list"])
        new_user_num = req_json["_source"]["new_user_num"]
        percent = 0.0
        if new_user_num != 0:
            percent = (len(new_user_list & self.active_user_list)/float(new_user_num)) * 100
        update_d = {"one_day_later": float('%.2f' % percent)}
        # update_condition = {"create_time": day,"app_key": self.app_key}
        return update_d

    def two_day_later(self):
        day = date_utils.param_day_yesterday(self.day, -2)
        req_json = self.dict_7_14_30[day]
        if not req_json:  # 时空的情况
            return {}
        new_user_list = set(req_json["_source"]["new_user_list"])
        new_user_num = req_json["_source"]["new_user_num"]
        percent = 0.0
        if new_user_num != 0:
            percent = (len(new_user_list & self.active_user_list) / float(new_user_num)) * 100
        update_d = {"two_day_later": float('%.2f' % percent)}
        # update_condition = {"create_time": day,"app_key": self.app_key}
        return update_d

    def three_day_later(self):
        day = date_utils.param_day_yesterday(self.day, -3)
        req_json = self.dict_7_14_30[day]
        if not req_json:  # 时空的情况
            return {}
        new_user_list = set(req_json["_source"]["new_user_list"])
        new_user_num = req_json["_source"]["new_user_num"]
        percent = 0.0
        if new_user_num != 0:
            percent = (len(new_user_list & self.active_user_list) / float(new_user_num)) * 100
        update_d = {"three_day_later": float('%.2f' % percent)}
        # update_condition = {"create_time": day,"app_key": self.app_key}
        return update_d

    def four_day_later(self):
        day = date_utils.param_day_yesterday(self.day, -4)
        req_json = self.dict_7_14_30[day]
        if not req_json:  # 时空的情况
            return {}
        new_user_list = set(req_json["_source"]["new_user_list"])
        new_user_num = req_json["_source"]["new_user_num"]
        percent = 0.0
        if new_user_num != 0:
            percent = (len(new_user_list & self.active_user_list) / float(new_user_num)) * 100
        update_d = {"four_day_later": float('%.2f' % percent)}
        # update_condition = {"create_time": day,"app_key": self.app_key}
        return update_d

    def five_day_later(self):
        day = date_utils.param_day_yesterday(self.day, -5)
        req_json = self.dict_7_14_30[day]
        if not req_json:  # 时空的情况
            return {}
        new_user_list = set(req_json["_source"]["new_user_list"])
        new_user_num = req_json["_source"]["new_user_num"]
        percent = 0.0
        if new_user_num != 0:
            percent = (len(new_user_list & self.active_user_list) / float(new_user_num)) * 100
        update_d = {"five_day_later": float('%.2f' % percent)}
        # update_condition = {"create_time": day,"app_key": self.app_key}
        return update_d

    def six_day_later(self):
        day = date_utils.param_day_yesterday(self.day, -6)
        req_json = self.dict_7_14_30[day]
        if not req_json:  # 时空的情况
            return {}
        new_user_list = set(req_json["_source"]["new_user_list"])
        new_user_num = req_json["_source"]["new_user_num"]
        percent = 0.0
        if new_user_num != 0:
            percent = (len(new_user_list & self.active_user_list) / float(new_user_num)) * 100
        update_d = {"six_day_later": float('%.2f' % percent)}
        # update_condition = {"create_time": day,"app_key": self.app_key}
        return update_d

    def seven_day_later(self):
        day = date_utils.param_day_yesterday(self.day, -7)
        req_json = self.dict_7_14_30[day]
        if not req_json:  # 时空的情况
            return {}
        new_user_list = set(req_json["_source"]["new_user_list"])
        new_user_num = req_json["_source"]["new_user_num"]
        percent = 0.0
        if new_user_num != 0:
            percent = (len(new_user_list & self.active_user_list) / float(new_user_num)) * 100
        update_d = {"seven_day_later": float('%.2f' % percent)}
        # update_condition = {"create_time": day,"app_key": self.app_key}
        return update_d

    def fourteen_day_later(self):
        day = date_utils.param_day_yesterday(self.day, -14)
        req_json = self.dict_7_14_30[day]
        if not req_json:  # 时空的情况
            return {}
        new_user_list = set(req_json["_source"]["new_user_list"])
        new_user_num = req_json["_source"]["new_user_num"]
        percent = 0.0
        if new_user_num != 0:
            percent = (len(new_user_list & self.active_user_list) / float(new_user_num)) * 100
        update_d = {"fourteen_day_later": float('%.2f' % percent)}
        # update_condition = {"create_time": day,"app_key": self.app_key}
        return update_d

    def thirty_day_later(self):
        day = date_utils.param_day_yesterday(self.day, -30)
        req_json = self.dict_7_14_30[day]
        if not req_json:  # 时空的情况
            return {}
        new_user_list = set(req_json["_source"]["new_user_list"])
        new_user_num = req_json["_source"]["new_user_num"]
        percent = 0.0
        if new_user_num != 0:
            percent = (len(new_user_list & self.active_user_list) / float(new_user_num)) * 100
        update_d = {"thirty_day_later": float('%.2f' % percent)}
        # update_condition = {"create_time": day,"app_key": self.app_key}
        return update_d