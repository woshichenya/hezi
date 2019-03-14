import win32api
#启动雷电模拟器
win32api.ShellExecute(0, 'open', r'F:\雷电模拟器\dnplayer2\dnplayer.exe', '','',1)
print("雷电模拟器已启动")