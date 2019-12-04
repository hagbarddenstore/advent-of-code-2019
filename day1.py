import math


def fuel_for_mass(mass):
	return math.floor(mass / 3) - 2

def fuel_for_fuel(mass):
	result = fuel_for_mass(mass)

	if result > 0:
		return result + fuel_for_fuel(result)

	return 0

if __name__ == '__main__':
	with open('input/day1.txt') as stream:
		lines = [int(line.strip()) for line in stream.readlines()]

	part1 = sum([fuel_for_mass(line) for line in lines])
	print(f'Part1: {part1}')

	part2 = sum([fuel_for_fuel(line) for line in lines])
	print(f'Part2: {part2}')
