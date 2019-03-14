go=Zongheguanjia.ZongheguanjiaTest.go
Go=Zongheguanjia.ZongheguanjiaTest.Go
def Fenxiao():
    '''进入分销商页面'''
    go.Cxpath("//div[@class='media-body ']","分销商应用","进入分销商应用","Bug-无法计入分销商应用")

'''进入一级菜单，分销商等级'''
def FenxiaoDengji():
    go.Ctext("分销商等级", "分销商等级页面", "进入分销商等级页面", "Bug-无法进入分销商等级页面")

def FenxiaoDengjiTianjia():
    go.Cxpath("//a[@class='btn btn-primary btn-sm']", "添加分销商等级按钮", "进入添加分销商等级页面", "Bug-无法进入添加分销商等级页面")
    go.Jubing()
    go.Cxpath("//button[@class='btn btn-default']", "取消按钮", "返回中", "Bug-无法点击取消按钮")
    go.Cxpath("//a[@class='btn btn-primary btn-sm']", "添加分销商等级按钮", "进入添加分销商等级页面", "Bug-无法进入添加分销商等级页面")
    go.Sxpath("//input[@name='levelname']","分销商等级输入框","白银会员","成功输入分销商等级","Bug-无法输入分销商等级")
    go.Sxpath("//input[@name='commission1']","佣金比例输入框","50","成功输入佣金比例","Bug-无法输入佣金比例")
    go.Sxpath("//input[@name='ordermoney']","升级金额输入框","10","成功输入升级金额","Bug-无法输入升级金额")
    go.Cxpath("//button[@type='submit']","提交按钮","提交中","Bug-无法点击提交")
def FenxiaoDengjiBianji():
    go.Cxpath("//td[@text='白银会员']/../td[4]/a[1]","编辑按钮","打开编辑页面中","Bug-无法点击编辑按钮")
    go.Cxpath("//button[@class='btn btn-default']", "取消按钮", "返回中", "Bug-无法点击取消按钮")
    go.Cxpath("//td[@text='白银会员']/../td[4]/a[1]", "编辑按钮", "打开编辑页面中", "Bug-无法点击编辑按钮")
    go.Sxpath("//input[@name='levelname']", "分销商等级输入框", "最高级会员", "成功输入分销商等级", "Bug-无法输入分销商等级")
    go.Sxpath("//input[@name='commission1']", "佣金比例输入框", "99.9", "成功输入佣金比例", "Bug-无法输入佣金比例")
    go.Sxpath("//input[@name='ordermoney']", "升级金额输入框", "1000", "成功输入升级金额", "Bug-无法输入升级金额")
    go.Cxpath("//button[@type='submit']", "提交按钮", "提交中", "Bug-无法点击提交")
def FenxiaoDengjiShanchu():
    go.Cxpath("//td[@text='最高级会员']/../td[4]/a[2]", "删除按钮", "执行删除提示", "Bug-无法点击删除按钮")
    go.Cxpath("//div[@class='buttons']/button[2]","取消按钮","取消删除中","Bug-无法取消删除")
    go.Cxpath("//td[@text='最高级会员']/../td[4]/a[2]", "删除按钮", "执行删除提示", "Bug-无法点击删除按钮")
    go.Cxpath("//div[@class='buttons']/button[1]", "确认按钮", "确认执行删除", "Bug-无法删除")

'''执行分销商应用的测试模块'''
Fenxiao()
FenxiaoDengji()
FenxiaoDengjiTianjia()
FenxiaoDengjiBianji()
FenxiaoDengjiShanchu()