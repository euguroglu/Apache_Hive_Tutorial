import sys

col = []
while True:
    line = sys.stdin.readline()
    if not line:
        break

    line = line.strip('\n ')
    print(line)
    line = line.split('\t')
    print(line)
    for i in range(len(line)):
        col.append(line[i].upper())

    print(col)
