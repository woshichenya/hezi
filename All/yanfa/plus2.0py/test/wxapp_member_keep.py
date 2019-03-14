# -*- coding: UTF-8 -*-
from plus_vdong.common.api import data_format
from controller.wxapp.member_keep import MemberKeepActive,MemberKeepNew
from plus_vdong.tableModel.db_base_model import PlusWxappMemberActiveKeep,PlusWxappMemberKeep
from plus_vdong.utils import query_all_wxapp,insert
from plus_vdong.utils import get_date_by_datetime
import sys
sys.path.append("..")


def start(arg_date):
    wxapps = query_all_wxapp()
    active_list = []
    new_list = []
    for item in wxapps:
        user_keep_new = MemberKeepNew(item.uniacid, arg_date)
        data_new = user_keep_new.get_data()
        data_source_new = data_format.list_for_dict(data_new[1], data_new[2])
        new_list.append(data_source_new)

        user_keep_active = MemberKeepActive(item.uniacid, arg_date)
        data_active = user_keep_active.get_data()
        data_source_active= data_format.list_for_dict(data_active[1], data_active[2])
        active_list.append(data_source_active)
    insert(PlusWxappMemberActiveKeep,active_list)
    insert(PlusWxappMemberKeep,new_list)



if __name__ == "__main__":
    try:
        arg_day = sys.argv[1]
    except IndexError, e:
        arg_day = get_date_by_datetime(1)

    start(arg_day)

