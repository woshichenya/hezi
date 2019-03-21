import sys
kk=sys.platform
print(sys.api_version)
print(sys.argv)
print(sys.path)
print(sys.base_prefix)
if "win" in kk:
    print("这是windows系统",kk
          )
else:
    print("这是linux系统",kk)