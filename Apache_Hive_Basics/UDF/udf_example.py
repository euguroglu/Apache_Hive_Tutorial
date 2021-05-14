import sys

try:
    for line in sys.stdin:
        line = str(line)
        line = line.strip()
        first = line[0]
        upper = first.upper()
        new_line = upper+line[1:]
        print(','.join([new_line]))

except:
    print(sys.exc_info())
