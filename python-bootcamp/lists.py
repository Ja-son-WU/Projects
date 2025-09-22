scores = [89, 93, 77, 78]

print("Length:", len(scores))
print("Average:", sum(scores) / len(scores))

print("升序", sorted(scores))
print("降序", sorted(scores, reverse = True))

scores.append(100)      # 在末尾加一个 100
scores[1] = 95          # 把第二个元素改成 95
scores.remove(78)       # 删除值为 78 的元素
print("修改后的列表:", scores)

# 4) 遍历（逐个打印）
for s in scores:
    print("Score:", s)