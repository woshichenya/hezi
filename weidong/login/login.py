class Login():
    def on(self,system_is_test_or_china_or_ceshi,user,username,password):
        if system_is_test_or_china_or_ceshi =="test":
            import login.pack.sso_test
            login_go=login.pack.sso_test.login_go()
        if system_is_test_or_china_or_ceshi == "china":
            import login.pack.sso_china
            login_go = login.pack.sso_china.login_go()
        if system_is_test_or_china_or_ceshi == "ceshi":
            import login.pack.sso_ceshi
            login_go = login.pack.sso_ceshi.login_go()
        go=login_go.on(user,username,password)
        return go
        
        
        
        
        
        
        



