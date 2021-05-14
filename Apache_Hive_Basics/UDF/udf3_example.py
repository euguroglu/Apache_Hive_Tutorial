import sys
import string

while True:
    line = sys.stdin.readline()
    if not line:
        break

    line = string.strip(line, '\n ')
    line = line.upper()

    print line
