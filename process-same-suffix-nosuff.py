# 打开原始文件
with open('fin-rev-processed.txt', 'r') as f:
    lines = f.readlines()

new_lines = []  # 存储处理后的行
    
for i in range(len(lines)):
    if i == 0:  # 处理第一行
        new_lines.append(lines[i])
        continue
        
    # 取出前一行和当前行逗号前的内容，判断是否完全相同
    pre_line = lines[i-1].split(',')[0]
    cur_line = lines[i].split(',')[0]
    
    if pre_line != cur_line:  # 如果不同，则将当前行添加到新的文件中
        new_lines.append(lines[i])
    else:
        new_lines[-1] = lines[i]
        
# 将处理后的行写入新的文件中
with open('fin-rev-processed-unique.txt', 'w') as f:
    f.writelines(new_lines)
