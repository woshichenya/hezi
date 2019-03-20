from beifen import BaibaoxiangMobile
import time




gw_go=1
while gw_go==1:
    m= BaibaoxiangMobile.MGO()
    s=m.go()
    if s=="over":
        print("准备重来")
        time.sleep(80)
        continue


    def lj(png_name):
        print(png_name)
        time.sleep(30)
        png_names = m.paizhao(png_name)
        return png_names

    png_names=lj("打开微信")

    m.panduan_dakai_wechat()

    m.moblie_huadong()
    png_names=lj("下滑屏幕")

    m.xiaochengxu_id_on("com.tencent.mm:id/ge","微动天下官方")
    png_names=lj("打开官网小程序")

    m.inputbt("微动官网","打开官网小程序出现Bug",1,"html",png_names,"")
    png_names=lj("进入官网小程序主页")

    '''
    点击微尘模块
    '''
    m.dianji(63,638,181,745,500)
    png_names=lj("点击微尘模块")
    m.inputbt("微尘","进入官网小程序微尘模块出现Bug",1,"html",png_names,"")
    png_names=lj("进入微尘模块")

    '''
    立即咨询
    '''
    m.dianji(120,404,254,442,500)
    png_names=lj("点击立即咨询")
    m.inputbt("微动天下官方","进入官网小程序立即咨询公众号出现Bug",1,"html",png_names,"com.tencent.mm:id/hm")
    png_names=lj("进入咨询模块")


    m.Cid("com.tencent.mm:id/hl","返回按钮","点击返回按钮","Bug--无法点击返回按钮")
    m.inputbt("微尘","进入官网小程序微尘模块出现Bug",1,"html",png_names,"")
    png_names=lj("进入微尘模块")

    '''
    了解更多
    '''
    m.dianji(386,404,504,442,500)
    png_names=lj("点击了解更多")
    m.inputbt("微尘自由版","进入官网小程序立即咨询公众号出现Bug",1,"html",png_names,"")
    png_names=lj("进入了解更多模块")

    m.Cid("com.tencent.mm:id/kq","返回按钮","返回上一页","Bug--无法返回上一页")
    m.inputbt("微尘","进入官网小程序微尘模块出现Bug",1,"html",png_names,"")
    png_names=lj("进入微尘模块")

    '''
    返回上一页
    '''
    m.Cid("com.tencent.mm:id/kq","返回按钮","返回上一页","Bug--无法返回上一页")
    m.inputbt("微动官网","打开官网小程序出现Bug",1,"html",png_names,"")
    png_names=lj("返回官网小程序主页")


    '''
    点击管家plus模块
    '''
    m.dianji(297,638,425,745,500)
    png_names=lj("点击管家plus模块")
    m.inputbt("管家Plus","进入官网小程序管家plus模块出现Bug",1,"html",png_names,"")
    png_names=lj("进入管家plus模块")

    '''
    立即咨询
    '''
    m.dianji(289,490,421,526,500)
    png_names=lj("点击立即咨询")
    m.inputbt("微动天下官方","进入官网小程序立即咨询公众号出现Bug",1,"html",png_names,"com.tencent.mm:id/hm")
    png_names=lj("进入咨询模块")


    m.Cid("com.tencent.mm:id/hl","返回按钮","点击返回按钮","Bug--无法点击返回按钮")
    m.inputbt("管家Plus","进入官网小程序管家plus模块出现Bug",1,"html",png_names,"")
    png_names=lj("进入管家plus模块")

    '''
    返回上一页
    '''
    m.Cid("com.tencent.mm:id/kq","返回按钮","返回上一页","Bug--无法返回上一页")
    m.inputbt("微动官网","打开官网小程序出现Bug",1,"html",png_names,"")
    png_names=lj("返回官网小程序主页")


    '''
    点击魔力游模块
    
    m.dianji(533,638,657,745,500)
    png_names=lj("点击魔力游模块")
    m.inputbt("微尘","进入官网小程序魔力游模块出现Bug",1,"html",png_names,"")
    png_names=lj("进入魔力游模块")
    
    #返回上一页
    
    m.Cid("com.tencent.mm:id/kq","返回按钮","返回上一页","Bug--无法返回上一页")
    m.inputbt("微动官网","打开官网小程序出现Bug",1,"html",png_names,"")
    png_names=lj("进入官网小程序主页")
    '''



    '''
    点击微动动态模块
    '''
    m.dianji(63,903,181,1020,500)
    png_names=lj("点击微动动态模块")
    m.inputbt("微动动态","进入官网小程序微动动态模块出现Bug",1,"html",png_names,"")
    png_names=lj("进入微动动态模块")

    '''
    了解更多
    '''
    m.dianji(289,433,421,472,500)
    png_names=lj("点击了解更多")
    m.inputbt("微动天下官方","进入官网小程序立即咨询公众号出现Bug",1,"html",png_names,"com.tencent.mm:id/hm")
    png_names=lj("进入了解更多模块")


    m.Cid("com.tencent.mm:id/hl","返回按钮","点击返回按钮","Bug--无法点击返回按钮")
    m.inputbt("微动动态","进入官网小程序微动动态模块出现Bug",1,"html",png_names,"")
    png_names=lj("进入微动动态模块")

    '''
    热点分类
    '''
    m.dianji(57,725,275,869,500)
    png_names=lj("点击第一个热点分类")
    m.inputbt("微动官网","进入官网小程序微动官网出现Bug",1,"html",png_names,"")
    png_names=lj("进入微动官网模块")

    m.Cid("com.tencent.mm:id/kq","返回按钮","返回上一页","Bug--无法返回上一页")
    m.inputbt("微动动态","进入官网小程序微动动态模块出现Bug",1,"html",png_names,"")
    png_names=lj("进入微动动态模块")

    '''
    返回上一页
    '''
    m.Cid("com.tencent.mm:id/kq","返回按钮","返回上一页","Bug--无法返回上一页")
    m.inputbt("微动官网","打开官网小程序出现Bug",1,"html",png_names,"")
    png_names=lj("返回官网小程序主页")


    '''
    点击魔力橙模块
    '''
    m.dianji(297,903,425,1020,500)
    png_names=lj("点击魔力橙模块")
    m.inputbt("魔力橙","进入官网小程序魔力橙模块出现Bug",0,"html",png_names,"")
    png_names=lj("进入魔力橙模块")

    '''
    返回上一页
    '''
    m.Cid("com.tencent.mm:id/kq","返回按钮","返回上一页","Bug--无法返回上一页")
    m.inputbt("微动官网","打开官网小程序出现Bug",1,"html",png_names,"")
    png_names=lj("返回官网小程序主页")



    '''
    点击推天下模块
    '''
    m.dianji(533,903,657,1020,500)
    png_names=lj("点击推天下模块")
    m.inputbt("推天下","进入官网小程序推天下模块出现Bug",1,"html",png_names,"")
    png_names=lj("进入推天下模块")

    '''
    立即咨询
    '''
    m.dianji(289,457,421,490,500)
    png_names=lj("点击立即咨询")
    m.inputbt("微动天下官方","进入官网小程序立即咨询公众号出现Bug",1,"html",png_names,"com.tencent.mm:id/hm")
    png_names=lj("进入咨询模块")


    m.Cid("com.tencent.mm:id/hl","返回按钮","点击返回按钮","Bug--无法点击返回按钮")

    '''
    返回上一页
    '''
    m.Cid("com.tencent.mm:id/kq","返回按钮","返回上一页","Bug--无法返回上一页")
    m.inputbt("微动官网","打开官网小程序出现Bug",1,"html",png_names,"")
    png_names=lj("返回官网小程序主页")



    '''
    点击行业解决方案模块
    '''
    m.dianji(63,1118,181,1177,500)
    png_names=lj("点击行业解决方案模块")
    m.inputbt("行业解决方案","进入官网小程序行业解决方案模块出现Bug",1,"html",png_names,"")
    png_names=lj("进入行业解决方案模块")

    '''
    立即咨询
    '''
    m.dianji(289,430,421,460,500)
    png_names=lj("点击立即咨询")
    m.inputbt("微动天下官方","进入官网小程序立即咨询公众号出现Bug",1,"html",png_names,"com.tencent.mm:id/hm")
    png_names=lj("进入咨询模块")


    m.Cid("com.tencent.mm:id/hl","返回按钮","点击返回按钮","Bug--无法点击返回按钮")
    m.inputbt("行业解决方案","进入官网小程序行业解决方案模块出现Bug",1,"html",png_names,"")
    png_names=lj("进入行业解决方案模块")


    '''
    解决方案
    '''
    m.dianji(86,648,260,780,500)
    png_names=lj("点击第一个成功案例")
    m.inputbt("成功案例","进入官网小程序成功案例页面出现Bug",1,"html",png_names,"")
    png_names=lj("进入咨询模块")

    m.Cid("com.tencent.mm:id/kq","返回按钮","返回上一页","Bug--无法返回上一页")
    m.inputbt("行业解决方案","进入官网小程序行业解决方案模块出现Bug",1,"html",png_names,"")
    png_names=lj("进入行业解决方案模块")

    '''
    返回上一页
    '''
    m.Cid("com.tencent.mm:id/kq","返回按钮","返回上一页","Bug--无法返回上一页")
    m.inputbt("微动官网","打开官网小程序出现Bug",1,"html",png_names,"")
    png_names=lj("返回官网小程序主页")


    '''
    点击聚运营模块
    '''
    m.dianji(297,1118,425,1177,500)
    png_names=lj("点击聚运营模块")
    m.inputbt("聚运营","进入官网小程序聚运营模块出现Bug",1,"html",png_names,"")
    png_names=lj("进入聚运营模块")

    '''
    立即咨询
    '''
    m.dianji(289,415,421,459,500)
    png_names=lj("点击立即咨询")
    m.inputbt("微动天下官方","进入官网小程序立即咨询公众号出现Bug",1,"html",png_names,"com.tencent.mm:id/hm")
    png_names=lj("进入咨询模块")

    m.Cid("com.tencent.mm:id/hl", "返回按钮", "点击返回按钮", "Bug--无法点击返回按钮")
    m.inputbt("聚运营", "进入官网小程序聚运营模块出现Bug", 1, "html", png_names, "")
    png_names = lj("进入聚运营模块")
    '''
    返回上一页
    '''
    m.Cid("com.tencent.mm:id/kq","返回按钮","返回上一页","Bug--无法返回上一页")
    m.inputbt("微动官网","打开官网小程序出现Bug",1,"html",png_names,"")
    png_names=lj("返回官网小程序主页")



    '''
    点击子公司模块
    '''
    m.dianji(533,1118,657,1177,500)
    png_names=lj("点击子公司模块")
    m.inputbt("子公司","进入官网小程序子公司模块出现Bug",1,"html",png_names,"")
    png_names=lj("进入子公司模块")
    '''
    返回上一页
    '''
    m.Cid("com.tencent.mm:id/kq","返回按钮","返回上一页","Bug--无法返回上一页")
    m.inputbt("微动官网","打开官网小程序出现Bug",1,"html",png_names,"")
    png_names=lj("返回官网小程序主页")


    bug_num=m.bug_num
    try:
        if bug_num>0:
            print("************************************************************************************有Bug")
            print("************************************************************************************有Bug%d个"%bug_num)
        else:
            print("*********************************************************************测试通过")
            print("等待100秒，开始下一轮")
    except:
        print("*********************************************************************测试通过")
        print("等待100秒，开始下一轮")

    time.sleep(100)
