from tkinter import *

huiyuan_zehou = {
        "普通会员": 1,
        "钻石会员": 0.77,
        "白银会员": 1,
        "黄金会员": 1
    }


a=huiyuan_zehou["普通会员"]
a=float(a)
c=0.22
b=a*c
print(b)
root=Tk()
a="提示一下"
t=Listbox(root)
for i in a:
    t.insert(0,i)
t.pack()
root.mainloop()
