import psutil
import time
for i in range (1,20):
    print(" CPU:"+str(psutil.cpu_percent(0.5))+"%")