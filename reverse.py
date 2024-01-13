with open('fin-do.txt', 'r', errors='ignore') as file_a:
    with open('fin-rev-noat.txt', 'w') as file_b:
        for line in file_a:
            try:
                reversed_line = line.rstrip()[::-1] + '\n'
                file_b.write(reversed_line)
            except UnicodeDecodeError:
                continue
with open('fin-rev-noat.txt', 'r') as fin:
    with open('fin-rev.txt', 'w') as fout:
        for line in fin:
            parts = line.strip().split(',', 1)
            if len(parts) > 1:
                fout.write(parts[0].replace('-', '@') + ',' + parts[1] + '\n')
            else:
                fout.write(parts[0].replace('-', '@') + '\n')
