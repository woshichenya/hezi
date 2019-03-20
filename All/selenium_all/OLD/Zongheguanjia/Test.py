from beifen import baibaoxiang

Go= baibaoxiang.geturl
go= baibaoxiang.geturl("https://test-xiao.vdongtx.com/")
#**************************************************************************************通用模块*********************************************************
def Denglu():
    username="vdongshopplus"
    password="vdongchina2018"
    go.Sxpath("//input[@name='username']","用户名输入框","vdongshopplus","成功输入用户名","输入用户名失败")
    go.Sxpath("//input[@name='password']","密码输入框","1234567890","成功输入密码","输入密码失败")
    try:
        go.Value("//input[@name='password']")
        cc=0
        if Go.value==password:
            go.Value("//input[@name='username']")
            cc=1
            if Go.value==username:
                print("账户密码输入正确，执行下一步")
                cc=2
    except:
        if cc==0:
            print("密码错误")
        elif cc==1:
            print("用户名错误")
    go.Cxpath("//*[@id='submit']","登陆按钮","登录中","无法点击登陆")

#**************************************************************************************通用模块*********************************************************
def Yingyonglan():
    go.Ctext("应用","应用超链接","进入应用页面中","Bug-无法进入应用页面")
    go.Cxpath("//div[@class='name namelist namelists text-over ng-binding']/../a/div","微动天下商城","进入应用中","Bug-无法进入应用")
    go.Cxpath("/html/body/div[2]/ul/li[9]/a","左侧应用栏","进入应用栏","Bug-无法进入应用栏")
def Jubing():
    Handler = Go.llq.window_handles
    s=0
    for i in Handler:
        s+=1
    if s>1:
        print(Handler)

#**************************************************************************************进入私用模块*********************************************************
def Fenxiao():
    '''进入分销商页面'''
    go.Cxpath("//div[@class='media-body ']","分销商应用","进入分销商应用","Bug-无法计入分销商应用")

'''进入一级菜单，分销商等级'''
def FenxiaoDengji():
    go.Ctext("分销商等级", "分销商等级页面", "进入分销商等级页面", "Bug-无法进入分销商等级页面")

def FenxiaoDengjiTianjia():
    go.Cxpath("//a[@class='btn btn-primary btn-sm']", "添加分销商等级按钮", "进入添加分销商等级页面", "Bug-无法进入添加分销商等级页面")
    Jubing()
    go.Cxpath("//button[@class='btn btn-default']", "取消按钮", "返回中", "Bug-无法点击取消按钮")
    '''到了这里无法继续点击添加按钮，所以要进行一个判断'''
    hy=0
    i=1
    while hy==0 and i<=30:
        try:
            Go.llq.find_element_by_xpath("//input[@name='levelname']").send_keys("白银会员")
            print("成功输入分销商等级")
            hy=1
        except:
            print("没有打开添加栏，第",i,"次点击添加按钮")
            go.Cxpath("//a[@class='btn btn-primary btn-sm']", "添加分销商等级按钮", "进入添加分销商等级页面", "Bug-无法进入添加分销商等级页面")
            i+=1
    if i==31:
        go.Sxpath("//input[@name='levelname']","会员等级输入框","白银会员","成功输入等级","Bug--无法输入等级")
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


'''执行登录脚本'''
Denglu()
'''执行进入应用页面'''
Yingyonglan()
#**************************************************************************************这里开始是执行区域*********************************************************
'''执行分销商应用的测试模块'''
Fenxiao()
FenxiaoDengji()
FenxiaoDengjiTianjia()
FenxiaoDengjiBianji()
FenxiaoDengjiShanchu()
#**************************************************************************************关闭浏览器*********************************************************
#Go.llq.quit()