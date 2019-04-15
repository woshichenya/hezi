class a:
    def __init__(self,name):
        print(name)
    def e(self,age):
        print("age is %s 岁"%age)

class b(a):
    def c(self):
        print(123)

d=b("this is my name")
d.c()
d.e("12")