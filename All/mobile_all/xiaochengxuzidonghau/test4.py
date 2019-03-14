import traceback
import femail

email=femail.email



try:
    a="a"
    print(1+a)
except Exception as e:
    ee=traceback.format_exc()
    print(e)
    email(ee)
