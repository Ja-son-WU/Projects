# 1. 变量
x = 5
y = 2.5
name = "Jason"
print("x:", x, "y:", y, "name:", name)

# 2. 条件分支
if x > 3:
    print("x is big")
else:
    print("x is small")

# 3. 循环
for i in range(3):
    print("Lap", i + 1)

count = 3
while count > 0:
    print("count:", count)
    count -= 1

# 4. 函数
def greet(person):
    return "Hello, " + person

print(greet("Jason"))

# 5. 列表
fruits = ["apple", "banana", "mango"]
fruits.append("pear")
print("fruits:", fruits)

# 6. 字典
sailor = {"name": "Jason", "sport": "ILCA", "age": 16}
sailor["age"] += 1
print("sailor:", sailor)

# 7. 文件操作
with open("note.txt", "w", encoding="utf-8") as f:
    f.write("Day1 OK!\nLearning Python basics.")

with open("note.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("File content:", content)