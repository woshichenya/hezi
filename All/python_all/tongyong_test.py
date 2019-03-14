class a:
    k=0
    l=0
    def leiji(self):
        print(a.k,",",a.l)
        a.l+=1
        if a.l>=3:
            a.k+=1
            a.l=0
