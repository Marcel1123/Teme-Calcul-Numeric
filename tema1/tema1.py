def problema1():
	precizie = 1
	while True:
		if 1 + pow(10, - precizie) == 1:
			return precizie - 1
		else:
			precizie += 1


def problema2():
	precizie = problema1()
	if (1.0 + pow(10, -precizie)) + pow(10, -precizie) != 1.0 +  ( pow(10, -precizie) + pow(10, -precizie) ):
		return True
	else:
		return False


def most_appropriate_power_of_two(number):
	num_len = len(str(bin(number))) - 2
	if pow(2, num_len) - number < number - pow(2, num_len - 1):
		return pow(2, num_len)
	else:
		return pow(2, num_len - 1)


def generate_number(number):
	start = 0
	if number <= 4:
		start = 4
	else:
		if number & (number - 1) == 0:
			start = number
		else:
			start = most_appropriate_power_of_two(number)
	while True:
		if start % math.log(start, 2) == 0:
			return start
		else:
			start = start * 2


print(generate_number(12))
