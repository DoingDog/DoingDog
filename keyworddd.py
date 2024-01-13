with open('bdfin.txt', 'r') as f:
    lines = f.readlines()

keywords = []
other_lines = []
for line in lines:
    if line.startswith('DOMAIN-KEYWORD'):
        keywords.append(line)
    else:
        other_lines.append(line)

lines = keywords + sorted(other_lines)

rows_to_delete = set()  # 修改为set，避免重复索引
for i, line in enumerate(keywords):
    content = line.split(',')[1].strip()
    for j, search_line in enumerate(lines[i+1:]):
        if search_line.startswith('DOMAIN'):
            search_part = ','.join(search_line.split(',')[1:]).strip()
            if content in search_part and search_line != line:
                rows_to_delete.add(i+j+1)  # 使用 add() 方法添加元素到 set

# 逐个删除需要删除的行
for idx in sorted(rows_to_delete, reverse=True):
    del lines[idx]

with open('xn.txt', 'w') as f:
    f.writelines(lines)
