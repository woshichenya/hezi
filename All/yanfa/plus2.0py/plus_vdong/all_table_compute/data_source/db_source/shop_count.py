from plus_vdong.tableModel.db_base_model import PlusShopCount

class PlusShopCountSource(object):
    def __init__(self):
        self._table = PlusShopCount


    def get_uniacid_type_data(self,uniacid,type):
        try:
            return self._table.select().where((self._table.uniacid == uniacid) & (self._table.type == type)).get()
        except Exception :
            return None
