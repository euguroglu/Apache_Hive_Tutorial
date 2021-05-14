import sys

for line in sys.stdin:
    line = line.strip()
    first = line[0]
    upper = first.upper()
    new_line = upper+line[1:]
    print(new_line)
