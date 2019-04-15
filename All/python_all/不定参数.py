class a:
    def b(self,a,b,*c):
        print("a:%s\nb:%s\nc:%s\n"%(a,b,c))



go=a()
go.b(1,2,('aaa','bbb','ccc'))