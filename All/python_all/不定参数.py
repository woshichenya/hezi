class a:
    def b(self,a,b,*c):
        print("a:%s\nb:%s\nc:%s\n"%(a,b,c))
        print(type(c))
        if len(c):
            print(11111111111)



go=a()
go.b(1,2,('aaa','bbb','ccc'))
go.b(1,2)