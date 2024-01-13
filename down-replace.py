import re

# 读取文件
with open('2.txt', 'r') as f:
    try:
        content = f.read()
    except UnicodeDecodeError:
        pass

# 删除空行
try:
    content = '\n'.join(line for line in content.splitlines() if line.strip())
except TypeError:
    pass

# 删除以#开头的行
try:
    content = '\n'.join(line for line in content.splitlines() if not line.startswith('#'))
except TypeError:
    pass

# 删除以@开头的行
try:
    content = '\n'.join(line for line in content.splitlines() if not line.startswith('@'))
except TypeError:
    pass

# 删除包含制表符的行
try:
    content = '\n'.join(line for line in content.splitlines() if '\t' not in line)
except TypeError:
    pass

# 删除以!开头的行
try:
    content = '\n'.join(line for line in content.splitlines() if not line.startswith('!'))
except TypeError:
    pass

# 删除以[开头的行
try:
    content = '\n'.join(line for line in content.splitlines() if not line.startswith('['))
except TypeError:
    pass

# 删除不是以i或I开头的行
try:
    content = '\n'.join(line for line in content.splitlines() if line.startswith('i') or line.startswith('I') or ':' in line)
except TypeError:
    pass

# 删除不是以i或I开头的行
try:
    content = '\n'.join(line for line in content.splitlines() if line.startswith('i') or line.startswith('I') or '/' in line)
except TypeError:
    pass

# 删除行首空格
try:
    content = '\n'.join(line.lstrip() for line in content.splitlines())
except TypeError:
    pass

# 将IP地址转换为DOMAIN
try:
    content = '\n'.join('DOMAIN,' + line.split()[1] for line in content.splitlines() if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s', line))
except TypeError:
    pass

# 删除所有空格
try:
    content = content.replace(' ', '')
except TypeError:
    pass

# 删除行首的-
try:
    content = '\n'.join(line.lstrip('-') for line in content.splitlines())
except TypeError:
    pass

# 删除行尾的,no-resolve
try:
    content = '\n'.join(line.rstrip(',no-resolve') for line in content.splitlines())
except TypeError:
    pass

# 如果行中包含三个逗号，则删除最后一个逗号及其后面的内容
try:
    content = '\n'.join(line.rsplit(',', 2)[0] if line.count(',') == 3 else line for line in content.splitlines())
except TypeError:
    pass

# 如果行以||开头，则将||替换为DOMAIN-SUFFIX,并删除^后面的内容，删除包含@的行
try:
    content = '\n'.join('DOMAIN-SUFFIX,' + line.split('||', 1)[1].split('^', 1)[0] for line in content.splitlines() if line.startswith('||') and '@' not in line)
except TypeError:
    pass

# 如果行中包含.bcefjklotqv，则在行首加上DOMAIN,，如果行首为DOMAIN,.，则将其替换为DOMAIN-SUFFIX,
try:
    content = '\n'.join(('DOMAIN,' if any(c in line for c in '.bcefjklotqv') else '') + line.lstrip('DOMAIN,.').replace('DOMAIN,', 'DOMAIN-SUFFIX,', 1) for line in content.splitlines())
except TypeError:
    pass

# 将host替换为domain，将HOST替换为DOMAIN
try:
    content = content.replace('host', 'domain').replace('HOST', 'DOMAIN')
except TypeError:
    pass

# 将ip6-cidr替换为ip-cidr6，将IP6-CIDR替换为IP-CIDR6
try:
    content = content.replace('ip6-cidr', 'ip-cidr6').replace('IP6-CIDR', 'IP-CIDR6')
except TypeError:
    pass

# 将domain-keyword替换为DOMAIN-KEYWORD，将domain-suffix替换为DOMAIN-SUFFIX，将domain替换为DOMAIN
try:
    content = content.replace('domain-keyword', 'DOMAIN-KEYWORD').replace('domain-suffix', 'DOMAIN-SUFFIX').replace('domain', 'DOMAIN')
except TypeError:
    pass

# 将user-agent替换为USER-AGENT
try:
    content = content.replace('user-agent', 'USER-AGENT')
except TypeError:
    pass

# 将ip-cidr替换为IP-CIDR
try:
    content = content.replace('ip-cidr', 'IP-CIDR')
except TypeError:
    pass

# 删除以D开头，后面跟着非K字符，然后是逗号，最后是一个或多个数字和一个.的行
try:
    content = '\n'.join(line for line in content.splitlines() if not (line.startswith('D') and not line.startswith('DK') and re.match(r',.*\.\d+$', line)))
except TypeError:
    pass

# 删除以D开头，后面跟着逗号，然后是任意字符，最后是一个大写字母的行
try:
    content = '\n'.join(line for line in content.splitlines() if not (line.startswith('D') and ',' in line and re.search(r'[A-Z]$', line)))
except TypeError:
    pass

# 将DOMAIN,*替换为DOMAIN-SUFFIX,
try:
    content = '\n'.join(line.replace('DOMAIN,*.', 'DOMAIN-SUFFIX,') for line in content.splitlines())
except TypeError:
    pass

# 删除以D开头，后面跟着任意字符，最后是*的行
try:
    content = '\n'.join(line for line in content.splitlines() if not (line.startswith('D') and ',' in line and line.endswith('*')))
except TypeError:
    pass

# 删除以DOMAIN-WILDCARD开头的行
try:
    content = '\n'.join(line for line in content.splitlines() if not line.startswith('DOMAIN-WILDCARD'))
except TypeError:
    pass

# 将处理后的内容写回文件
with open('2.txt', 'w') as f:
    try:
        f.write(content)
    except TypeError:
        pass

