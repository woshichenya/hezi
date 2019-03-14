import mobile_all.gongzhonghao30.jinrugongzhonghao

go= mobile_all.gongzhonghao30.jinrugongzhonghao.go
Go= mobile_all.gongzhonghao30.jinrugongzhonghao.Go

def jinruxiugaiyemian():
    a="http://test-mp.vdongtx.com/web/index.php?c=site&a=entry&m=ewei_shopv2&do=web&r=goods.edit&id=113&tab=basic#tab_option"
    Go.llq.get(a)
    s=Go.llq.current_url
    while s!=a:
        Go.llq.get(a)
        s = Go.llq.current_url

def bianji():
    go.Cxpath("//input[@value='保存商品']", "保存按钮", "进入公众号", "Bug-无法进入公众号")
jinruxiugaiyemian()

'''
保存商品

'''