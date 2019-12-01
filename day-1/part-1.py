import sys
import math

print(sum([math.floor(int(line.strip()) / 3) - 2 for line in sys.stdin.readlines()]))
