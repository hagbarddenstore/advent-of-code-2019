from day1 import fuel_for_mass, fuel_for_fuel


def test_day1_part1():
	assert fuel_for_mass(12) == 2
	assert fuel_for_mass(14) == 2
	assert fuel_for_mass(1969) == 654
	assert fuel_for_mass(100756) == 33583

def test_day1_part2():
	assert fuel_for_fuel(12) == 2
	assert fuel_for_fuel(1969) == 966
	assert fuel_for_fuel(100756) == 50346
