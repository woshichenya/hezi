# -*- coding: UTF-8 -*-
from plus_vdong.all_table_compute.data_compute.goods_sale_visit_compute import DbGoodsSaleVisitCompute
from plus_vdong.common.static import public_args as p_a
class DbGoodsSaleVisit(object):
    '''商品销售访问信息'''
    # mysql表名 只是备注
    table_name = 'plus_shop_goods_salevisit'

    # 列名                  COMMENT
    # id
    # good_id                商品id
    # sales_price            商品销售额
    # visit_person_sum       商品访问人数
    # pay_person_sum         商品付款人数
    # good_lv                商品转化率
    # create_date            创建日期
    # create_time
    # uniacid
    # type                   类型 1小程序 2公众号
    # total                  商品销售数量
    i_col = ['id', 'good_id', 'sales_price', 'visit_person_sum', 'pay_person_sum', 'good_lv', 'create_date','uniacid','type','total']
    data_i = []

    def __init__(self,uniacid,type,date):
        self.comute = DbGoodsSaleVisitCompute(uniacid, type, date)
        pass
    def set_data_i(self):

        self.data_i = self.comute.get_all_rows()

    def get_data(self):
        try:
           self.set_data_i()

        except Exception, e:
            pass
            p_a.logger.getLogger().error('error %s' % str(e))
        return self.data_i
