# 用集合存储所有结尾
with open('del.ini', 'r') as f:
    endings = {l.strip() for l in f}

# 打开 bn.txt 文件并读取所有行
with open('bn.txt', 'r') as b:
    lines = b.readlines()

# 使用列表推导式过滤不满足条件的行
new_lines = [l for l in lines if not any(l.strip().endswith(e) for e in endings)]

# 把符合条件的行写入 bn.txt 文件中
with open('bn.txt', 'w') as b:
    b.writelines(new_lines)
