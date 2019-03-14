import time

def inputbt(dbiaoti,shifouquan):
    gogo=2
    while gogo==2:
        try:
            bt="123123123"
            gogo=1
        except Exception as ee:
            time.sleep(1)
    if shifouquan==1:
        if bt!=dbiaoti:

            print("标题不完全一样，已发送邮件")
        else:
            print("标题是：", bt, "标题验证通过(一致)")
    if shifouquan!=1:
        if dbiaoti not in bt :

            print("标题不包含判断值,已发送邮件")
        else:
            print("标题是：", bt, "标题验证通过(包含)")
    return bt

inputbt("",0)