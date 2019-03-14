import os
f=open('E:\\123\操作步骤.docx','w')
k="abcdefg"
f.write(str(k))
f.close()
f=open('E:\\123\操作步骤.docx')
t=f.read()
print(str(t))
f.close()