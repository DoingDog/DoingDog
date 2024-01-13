import re

# 打开输入文件并忽略Unicode解码错误
with open('fing.txt', 'r', errors='ignore') as fin:
    # 打开输出文件
    with open('fin.txt', 'w') as fout:
        # 逐行读取输入文件
        for line in fin:
            try:
                # 使用正则表达式检测是否包含特殊字符
                if re.match(r'^[\u0020-\u007e]*$', line):
                    # 写入包含正常字符的行到输出文件
                    fout.write(line)
            except UnicodeDecodeError:
                # 忽略包含特殊字符的行
                pass
