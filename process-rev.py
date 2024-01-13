with open('fin-rev-s.txt', 'r') as f:
    lines = f.readlines()

output_lines = []
last_line_ended_with_xiffus = False
prefix = ""

for i in range(len(lines)):
    line = lines[i].strip()

    if i == 0 or not last_line_ended_with_xiffus:
        output_lines.append(line)
        if line.endswith(",XIFFUS-NIAMOD"):
            prefix = line.split(',')[0] + '.'
        else:
            prefix = ""
    else:
        if line.startswith(prefix):
            continue
        else:
            output_lines.append(line)
            if line.endswith(",XIFFUS-NIAMOD"):
                prefix = line.split(',')[0] + '.'
            else:
                prefix = ""

    last_line_ended_with_xiffus = line.endswith(",XIFFUS-NIAMOD")

with open('fin-rev-processed.txt', 'w') as f:
    f.write('\n'.join(output_lines))
