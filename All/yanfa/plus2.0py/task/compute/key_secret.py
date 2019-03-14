# -*- coding: UTF-8 -*-
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))));

# sys.path.append("../../")
from plus_vdong.utils.date_utils import system_time_befor
from plus_vdong.compute_result_handle.db_handle.db_insert.db_wechat_insert import DbInsertVipcn
from plus_vdong.compute_result_handle.db_handle.db_insert.db_wxapp_insert import DbInsertApplet
from plus_vdong.utils.db_util import query_all_wechats,query_all_wxapp
from plus_vdong.common.static import  public_args as p_a
def start(arg_day):
    pass
    wechat_all = query_all_wechats()
    for wechat in wechat_all:
        try:
            vipcn = DbInsertVipcn(str(wechat.uniacid), arg_day, wechat.key, wechat.secret)
            """公众号会员关注分析"""
            vipcn.wechats_member_analysis()
            """公众号阅读渠道"""
            vipcn.wechats_article_read_channel()
            """公众号阅读统计"""
            vipcn.wechats_article_read_count()

        except Exception,f:
            print f.message
            p_a.logger.getLogger().debug('%s uniacid:%s 没有写入任何数据, key:%s',f.message, wechat.uniacid.encode("utf-8"),wechat.key.encode("utf-8"))

    """小程序调用"""
    wxapp_all = query_all_wxapp()
    for wxapp in wxapp_all:
        try:
            app = DbInsertApplet(str(wxapp.uniacid), arg_day, wxapp.key, wxapp.secret)
            """小程序访问数据"""
            app.insert_wxapp_data()

        except Exception,f:
            p_a.logger.getLogger().debug('%s uniacid:%s 小程序没有写入任何数据, key:%s',f.message, wxapp.uniacid.encode("utf-8"),wxapp.key.encode("utf-8"))


# def start2():
#     key = 'wx7a9feb43846c1ce6'
#     secret = 'a5e4858c580eb4572e7c0cf0c0aded85'
#     uniacid = 1
#
#     date = get_date_by_datetime(1)
#     vipcn = DbInsertVipcn(uniacid, date, key, secret)
#
#     vipcn.plus_wechats_member_analysis()
#     pass
if __name__ == "__main__":
    try:
        arg_day = sys.argv[1]
    except IndexError, e:
        arg_day = system_time_befor(-1)
    start(arg_day)
