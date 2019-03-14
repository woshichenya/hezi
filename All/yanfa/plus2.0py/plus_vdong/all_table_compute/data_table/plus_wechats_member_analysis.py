# -*- coding: UTF-8 -*-

from plus_vdong.common.static import public_args as p_a
from plus_vdong.all_table_compute.data_compute.plus_wechats_member_analysis_compute import DbPlusWechatsMemberAnalysisCompute
class DbPlusWechatsMemberAnalysis(object):
    '''商品销售访问信息'''
    # mysql表名
    table_name = 'plus_wechats_member_analysis'

    # 列名                  COMMENT
    # id
    # uniacid
    # new_user              新关注人数
    # cancel_user           取消关注人数
    # cumulate_user         总人数
    # incr_user             增量关注人数
    # create_date           创建日期
    # compare               关注比率，包括同比环比

    compare = '''{"cumulate_user_huanbi": "--", "new_user_tongbi": "--", "cumulate_user_tongbi": "--", "new_user_huanbi": "--", "incr_user_tongbi": "--", "incr_user_huanbi": "--", "cancel_user_tongbi": "--", "cancel_user_huanbi": "--"}'''
    i_col = { 'uniacid':"", 'new_user':0, 'cancel_user':0, 'cumulate_user':0, 'incr_user':0, 'create_date':"",'compare':""}
    data_i = []

    def __init__(self,uniacid,date,key,sercet):
        self.i_col["uniacid"] = uniacid
        self.i_col["create_date"] = date
        self.i_col["compare"] = self.compare
        self.comute = DbPlusWechatsMemberAnalysisCompute(uniacid,date,key,sercet)
        pass
    def set_data_i(self):
         data = self.comute.get_data()
         if not data:
            data = self.i_col
         self.data_i = data
    def get_data(self):
        try:
           self.set_data_i()
        except Exception, e:
            self.data_i = self.i_col
            p_a.logger.getLogger().error('error %s' % str(e))
        return self.data_i
