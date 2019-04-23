from baibaoxiang import sys_powel
import os

aa=os.system("netstat -nat|grep 80|wc -l")
sys_powel.powel_go().print_cpu("")