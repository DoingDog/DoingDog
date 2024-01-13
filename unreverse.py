with open('fin-rev-processed-unique.txt', 'r') as fin:
    with open('fin-rev-processed-uniqueat.txt', 'w') as fout:
        for line in fin:
            parts = line.strip().split(',', 1)
            if len(parts) > 1:
                fout.write(parts[0].replace('@', '-') + ',' + parts[1] + '\n')
            else:
                fout.write(parts[0].replace('@', '-') + '\n')
with open('fin-rev-processed-uniqueat.txt', 'r') as file_a:
    with open('fin-rev-processed-unique-unrev.txt', 'w') as file_b:
        for line in file_a:
            reversed_line = line.rstrip()[::-1] + '\n'
            file_b.write(reversed_line)
