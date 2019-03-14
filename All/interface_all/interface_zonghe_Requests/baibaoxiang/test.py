shouji_txt = open(r'..\case\shoujihao.txt')
shouji = int(shouji_txt.read())

print(shouji)
t = shouji + 1
shouji_txt.close()
shouji_txt = open("..\case\shoujihao.txt", 'w')
x = str(t)
shouji_txt.write(x)
shouji_txt.close()
