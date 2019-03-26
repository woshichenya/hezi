for ss in sss:
    print(ss.text)
    if "登录" in ss.text:
        ss.click()
        paizhao_pc("点击登录")
