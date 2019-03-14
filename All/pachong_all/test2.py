import re



r="message('您访问的功能模块不存在，请重新进入', '', 'info');"
html = r.content.decode('utf-8')
erweima = re.findall(r"util.message(.*?)",html,re.DOTALL)
print(erweima)