import psutil
import platform
version=platform.python_version()



sport = 80
status_list = ["LISTEN", "ESTABLISHED", "TIME_WAIT", "CLOSE_WAIT", "LAST_ACK", "SYN_SENT"]

status_temp = []
net_connections = psutil.net_connections()
for key in net_connections:
    if key.laddr[1] == sport:
        status_temp.append(key.status)

for status in status_list:
    print(status, status_temp.count(status))
