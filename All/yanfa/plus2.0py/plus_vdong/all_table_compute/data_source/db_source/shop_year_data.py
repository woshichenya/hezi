from plus_vdong.tableModel.db_base_model import PlusShopYearData


class PlusShopYearDataSource(object):
    def __init__(self):
        self._table = PlusShopYearData
        pass

    def get_someday_data(self, uniacid, type, date):
        try:
            return self._table().select().where(
                (self._table.uniacid == uniacid) & (self._table.type == type) & (self._table.create_date == date)).get()
        except Exception:
            return None


