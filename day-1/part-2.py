import sys
import math

def fuel(mass):
	result = math.floor(mass / 3) - 2

	if (result > 0):
		return result + fuel(result)

	return 0

print(sum([fuel(int(line.strip())) for line in sys.stdin.readlines()]))
