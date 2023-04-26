# First pass
with open('Expt2.asm', 'r') as f:
    lines = f.readlines()

macro_table = {}

for i, line in enumerate(lines):
    tokens = line.split()
    if tokens and tokens[0] == 'MACRO':
        name = tokens[1]
        params = tokens[2:]
        macro_lines = []
        j = i + 1
        while j < len(lines) and lines[j].strip() != 'MEND':
            macro_lines.append(lines[j])
            j += 1
        macro_table[name] = (params, macro_lines)

# Second pass
for line in lines:
    tokens = line.split()
    if tokens and tokens[0] in macro_table:
        name = tokens[0]
        args = tokens[1:]
        params, macro_lines = macro_table[name]
        if len(args) != len(params):
            raise ValueError(f"Macro {name} takes {len(params)} arguments, {len(args)} given")
        for param, arg in zip(params, args):
            for i, macro_line in enumerate(macro_lines):
                macro_lines[i] = macro_line.replace(param, arg)
        print(''.join(macro_lines), end='')  # print instead of writing to file
    else:
        print(line, end='')  # print instead of writing to file