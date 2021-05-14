import sys
def capitalize(input):
   return input.upper()

for line in sys.stdin:
   line = line.strip()
   print capitalize(line)
