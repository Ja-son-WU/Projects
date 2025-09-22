s = "  ILCA sailor  "

print(s.strip())              # 去掉首尾空格
print(s.lower())              # 全部小写
print(s.upper())              # 全部大写
print(s.replace("ILCA", "ILCA-4"))   # 替换
print(s[0:4])                 # 切片（前4个字符）
print("Jason" in s)           # 判断子串
print(s.split())              # 拆分成列表