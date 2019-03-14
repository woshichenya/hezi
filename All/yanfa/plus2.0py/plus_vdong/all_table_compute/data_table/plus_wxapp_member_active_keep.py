# -*- coding: UTF-8 -*-
from plus_vdong.all_table_compute.data_compute.plus_wxapp_member_active_keep_compute import \
    EsPlusWxappMemberActiveKeepCompute
from plus_vdong.common.api import data_format
from plus_vdong.common.static import public_args as p_a


class DbPlusWxappMemberActiveKeep(object):

    """
    小程序活跃会员留存
    """

    # 列名             COMMENT
    # uniacid
    # active_member_save    活跃留存
    # one_day_later    1天后
    # two_day_later    2天后
    # three_day_later  3天后
    # four_day_later   4天后
    # five_day_later   5天后
    # six_day_later    6天后
    # seven_day_later  7天后
    # fourteen_day_later  14天后
    # thirty_day_later  30天后
    # create_date      入库日期
    # update_date      更新日期

    i_col = ['uniacid','active_member_save','create_date']

    def __init__(self,app_key,day):
        self.app_key = app_key
        self.day = day
        self.plus_wxapp_member_active_keep_compute = EsPlusWxappMemberActiveKeepCompute(self.app_key ,self.day)
        # 计算后数据
        self.i_data = []
        self.u_data = []

    def set_data_insert(self):
        self.i_data = self.plus_wxapp_member_active_keep_compute.active_member_save()

    def get_data(self):
        try:
            self.set_data_insert()
        except Exception, e:
            p_a.logger.getLogger().error('error %s' % str(e))
        return data_format.list_for_dict(self.i_col, [self.i_data])

    def set_data_update(self):
        self.u_data.append(self.plus_wxapp_member_active_keep_compute.one_day_later())
        self.u_data.append(self.plus_wxapp_member_active_keep_compute.two_day_later())
        self.u_data.append(self.plus_wxapp_member_active_keep_compute.three_day_later())
        self.u_data.append(self.plus_wxapp_member_active_keep_compute.four_day_later())
        self.u_data.append(self.plus_wxapp_member_active_keep_compute.five_day_later())
        self.u_data.append(self.plus_wxapp_member_active_keep_compute.six_day_later())
        self.u_data.append(self.plus_wxapp_member_active_keep_compute.seven_day_later())
        self.u_data.append(self.plus_wxapp_member_active_keep_compute.fourteen_day_later())
        self.u_data.append(self.plus_wxapp_member_active_keep_compute.thirty_day_later())

    def get_data_update(self):
        try:
            self.set_data_update()
        except Exception, e:
            p_a.logger.getLogger().error('error %s' % str(e))
        return self.u_data

    def get_day(self):
        return self.day

    def get_app_key(self):
        return self.app_key
