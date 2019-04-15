import login_all.zhongou_test
a=login_all.zhongou_test.Login_go()
go=a.on()


# go.CText_partial_s("183RUN","183RUN菜单","进入183RUN菜单","183RUN菜单报错")
go.CText_partial_s_key("183RUN","183RUN菜单","进入183RUN菜单","183RUN菜单报错")
go.CTag_name_zidingyi("span","text","用户管理","用户管理菜单","打开用户管理菜单","无法打开用户管理菜单")
go.CText_partial_s_key("会员用户","会员用户菜单","进入会员用户菜单","进入会员用户菜单报错")
go.CText_partial_s_key("新增","新增会员","进入新增会员","进入新增会员报错")
go.Sid("nickname","用户名输入框","测试陈","输入名称","无法输入名称")
#提交
go.CTag_name_zidingyi("button","type","submit","提交按钮","点击提交按钮","无法点击提交按钮")