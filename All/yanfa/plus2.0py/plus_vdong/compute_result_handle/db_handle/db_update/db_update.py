# -*- coding: UTF-8 -*-
from plus_vdong.all_table_compute.data_table.plus_wxapp_member_active_keep import DbPlusWxappMemberActiveKeep
from plus_vdong.all_table_compute.data_table.plus_wxapp_member_keep import DbPlusWxappMemberKeep
from plus_vdong.tableModel.db_base_model import PlusWxappMemberKeep, PlusWxappMemberActiveKeep
from plus_vdong.utils import date_utils
from plus_vdong.common.static import public_args as p_a


class DbUpdate(object):


    def __init__(self, app_key, day, type):
        self.app_key = type + '-' + app_key
        self.day = day
        self.type = type

    def update_game_all(self):
        # 计算几天后留存
        self.update_plus_wxapp_member_keep()
        self.update_plus_wxapp_member_active_keep()

    def update_plus_wxapp_member_keep(self):
        try:
            plus_wxapp_member_keep = DbPlusWxappMemberKeep(self.app_key, self.day)
            data_user = plus_wxapp_member_keep.get_data_update()
            for i in range(0, len(data_user)):
                data = data_user[i]
                if data:
                    create_time = date_utils.param_day_yesterday(self.day, -(i + 1))
                    self.update_keep(PlusWxappMemberKeep, data, create_time)
        except Exception, e:
            p_a.logger.getLogger().error('update_user_keep_new 异常：%s', e)

    def update_plus_wxapp_member_active_keep(self):
        try:
            plus_wxapp_member_active_keep = DbPlusWxappMemberActiveKeep(self.app_key, self.day)
            data_active = plus_wxapp_member_active_keep.get_data_update()
            for i in range(0, len(data_active)):
                data = data_active[i]
                if data:
                    create_time = date_utils.param_day_yesterday(self.day, -(i + 1))
                    self.update_keep(PlusWxappMemberActiveKeep, data, create_time)
        except Exception, e:
            p_a.logger.getLogger().error('update_user_keep_new 异常：%s', e)

    def update_keep(self, keep, data, create_time):
        u_time = date_utils.system_time()
        col = data.keys()[0]
        if cmp(col, "one_day_later") == 0:
            keep.update(one_day_later=data["one_day_later"], update_date=u_time).where(keep.uniacid == self.app_key, keep.create_date == create_time).execute()
        elif cmp(col, "two_day_later") == 0:
            keep.update(two_day_later=data["two_day_later"], update_date=u_time).where(keep.uniacid == self.app_key, keep.create_date == create_time).execute()
        elif cmp(col, "three_day_later") == 0:
            keep.update(three_day_later=data["three_day_later"], update_date=u_time).where(keep.uniacid == self.app_key, keep.create_date == create_time).execute()
        elif cmp(col, "four_day_later") == 0:
            keep.update(four_day_later=data["four_day_later"], update_date=u_time).where(keep.uniacid == self.app_key, keep.create_date == create_time).execute()
        elif cmp(col, "five_day_later") == 0:
            keep.update(five_day_later=data["five_day_later"], update_date=u_time).where(keep.uniacid == self.app_key, keep.create_date == create_time).execute()
        elif cmp(col, "six_day_later") == 0:
            keep.update(six_day_later=data["six_day_later"], update_date=u_time).where(keep.uniacid == self.app_key,keep.create_date == create_time).execute()
        elif cmp(col, "seven_day_later") == 0:
            keep.update(seven_day_later=data["seven_day_later"], update_date=u_time).where(keep.uniacid == self.app_key, keep.create_date == create_time).execute()
        elif cmp(col, "fourteen_day_later") == 0:
            create_time = date_utils.param_day_yesterday(self.day, -14)
            keep.update(fourteen_day_later=data["fourteen_day_later"], update_date=u_time).where(keep.uniacid == self.app_key, keep.create_date == create_time).execute()
        elif cmp(col, "thirty_day_later") == 0:
            create_time = date_utils.param_day_yesterday(self.day, -30)
            keep.update(thirty_day_later=data["thirty_day_later"], update_date=u_time).where(keep.uniacid == self.app_key, keep.create_date == create_time).execute()





