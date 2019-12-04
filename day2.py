def calculate(values):
	i = 0

	while True:
		op = values[i + 0]
		
		if op == 99:
			break

		in1 = values[values[i + 1]]
		in2 = values[values[i + 2]]

		if op == 1:
			values[values[i + 3]] = in1 + in2
		elif op == 2:
			values[values[i + 3]] = in1 * in2
		else:
			print(f'invalid opcode {op}')

			return []

		i += 4

	return values

def calculate2(values, limit):
	for noun in range(0, 100):
		for verb in range(0, 100):
			part2 = values.copy()

			part2[1] = noun
			part2[2] = verb

			if calculate(part2)[0] == limit:
				return 100 * noun + verb

	return 0

if __name__ == '__main__':
	with open('input/day2.txt') as stream:
		values = [int(p) for p in stream.read().split(',')]

	part1 = values.copy()

	part1[1] = 12
	part1[2] = 2

	print(f'Part1: {calculate(part1)[0]}')

	print(f'Part2: {calculate2(values, 19690720)}')
