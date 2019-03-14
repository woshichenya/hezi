from plus_vdong.tableModel.db_base_model import PlusShopSalevisit

class PlusShopSaleVisitSource(object):
    def __init__(self):
        self._table = PlusShopSalevisit
        pass
    def get_shop_rank(self,uniacids,create_date,type):
        # print uniacids
        # print create_date
        # print type

        if type:
            data = self._table().select(self._table.uniacid, self._table.type, self._table.sale_prices).where((self._table.uniacid.in_(uniacids)) & (self._table.type == type) & (self._table.create_date == create_date)).order_by(self._table.sale_prices.desc()).dicts()
        else:
            data = self._table().select(self._table.uniacid, self._table.type, self._table.sale_prices).where((self._table.uniacid.in_(uniacids))& (self._table.create_date == create_date)).order_by(self._table.sale_prices.desc()).dicts()

        pdata = []
        for item in data:
            pdata.append(item)
        return pdata

    def get_someday_data(self,uniacid,type,date):
        try:
            return self._table().select().where((self._table.uniacid == uniacid) & (self._table.type == type) & (self._table.create_date == date)).get()
        except Exception:
            return None

    def get_history_data(self,uniacid,type):
        try:
            sql = "SELECT \
            IFNULL(SUM(sale_prices),0) AS sale_prices,\
            IFNULL(SUM(visit_person_sum),0) AS visit_person_sum,\
            IFNULL(SUM(visit_sum),0) AS visit_sum,\
            IFNULL(SUM(pay_person_sum),0) AS pay_person_sum,\
            IFNULL(SUM(pay_order_sum),0) AS pay_order_sum\
            FROM\
                plus_shop_sale_visit\
            where uniacid = '%s' and type = %d"%(uniacid,int(type))
            return self._table().raw(sql).get()
        except Exception as e:
            return None


    def get_year_data(self,uniacid,type,year):
        try:
            sql = "SELECT \
            IFNULL(SUM(sale_prices),0) AS sale_prices,\
            IFNULL(SUM(visit_person_sum),0) AS visit_person_sum,\
            IFNULL(SUM(visit_sum),0) AS visit_sum,\
            IFNULL(SUM(pay_person_sum),0) AS pay_person_sum,\
            IFNULL(SUM(pay_order_sum),0) AS pay_order_sum\
            FROM\
                plus_shop_sale_visit\
            where uniacid = '%s' and type = %d and YEAR(create_date) = %s "%(uniacid,int(type),year)
            return self._table().raw(sql).get()
        except Exception as e:
            return None





