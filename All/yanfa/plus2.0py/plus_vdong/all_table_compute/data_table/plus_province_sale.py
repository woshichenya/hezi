# -*- coding: UTF-8 -*-

from plus_vdong.all_table_compute.data_compute.province_sale_compute import DbPlusProvinceSaleComputer, \
    EsPlusProvinceSaleComputer


class DbPlusProvinceSale(object):

    _result = {'uniacid':0,'province':'其他','sale_prices':0.00,'pay_person_sum':0,'visit_person_sum':0,'visit_pay_lv':0.00,'type':1,'create_date':'0000-00-00'}
    _result_province = {}

    def __init__(self,uniacid,type,date):
        self._data = []
        self._result['uniacid'] = uniacid
        self._result['type'] = type
        self._result['create_date'] = date
        self.PlusProvinceSaleComputer = DbPlusProvinceSaleComputer(uniacid, date,type)
        self.es_PlusProvinceSaleComputer = EsPlusProvinceSaleComputer(uniacid, date,type)

    def set_data(self):
        sale_pay_result =self.PlusProvinceSaleComputer.get_province_sale_and_pay_person()
        for item in sale_pay_result:
            result_copy = self._result.copy()
            result_copy['sale_prices'] = item.sale_prices
            result_copy['pay_person_sum'] = item.pay_person_sum
            if item.province:
                result_copy['province'] = item.province
            if self._result_province.has_key(result_copy['province']):
                self._result_province[result_copy['province']]['sale_prices'] += result_copy['sale_prices']
                self._result_province[result_copy['province']]['pay_person_sum'] += result_copy['pay_person_sum']
            else:
                self._result_province[result_copy['province']] = result_copy
        visit_person_sum = self.es_PlusProvinceSaleComputer.visit_person_sum()
        if  visit_person_sum is not None:
            for item in visit_person_sum['aggregations']['NAME']['buckets']:
                if self._result_province.has_key(item['key']) :
                    self._result_province[item['key']]['visit_person_sum'] = item['doc_count']
                    try:
                        self._result_province[item['key']]['visit_pay_lv'] = self._result_province[item['key']]['pay_person_sum'] / item['doc_count'] * 100
                    except Exception:
                        pass

        self._data = self._result_province.values()

    def get_data(self):
        self.set_data()
        return self._data

