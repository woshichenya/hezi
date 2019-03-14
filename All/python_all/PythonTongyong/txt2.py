import os
import time

ft=open('D:\\text.txt')
s=ft.read()
print(s)

'''
#file_object = open('test.txt') 
#//不要把open放在try中，以防止打开失败，那么就不用关闭了
try:
    file_context = file_object.read() 
    //file_context是一个string，读取完后，就失去了对test.txt的文件引用
    #  file_context = open(file).read().splitlines() 
    // file_context是一个list，每行文本内容是list中的一个元素

finally:
    file_object.close()

//除了以上方法，也可用with、contextlib都可以打开文件，且自动关闭文件，
//以防止打开的文件对象未关闭而占用内存

'''

t=time.time()
t=int(t)
print(t)
ft=open('D:\\text.txt','w')
ft.write(str(t))
ft=open('D:\\text.txt')
ftt=ft.read()
print(ftt)
time.sleep(2)

def biaoji_time():
    t=time.strftime("%Y%m%d%H%M%S", time.localtime())
    t=time.time()
    t=int(t)
    ft=open('D:\\text.txt','w')
    ft.write(str(t))
    ft.close()

biaoji_time()