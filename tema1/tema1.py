import math
import random
import numpy

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


def generate_boolean_matrix(dimension):
	return numpy.array([[random.choice([True, False]) for i in range(0, dimension)] for j in range(0, dimension)], dtype=bool)


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


def matrix_A_decomposition(initial_matrix, m, p):
	result = []
	start = 0
	end = m
	for i in range(0, p):
		aux = [i[start:end] for i in initial_matrix]
		start = start + m
		end = end + m
		result.append(aux)
	return numpy.array(result)


def matrix_B_decomposition(initial_matrix, m, p):
	result = []
	start = 0
	end = m
	for i in range(0, p):
		aux = initial_matrix[start:end]
		start = start + m
		end = end + m
		result.append(aux)
	return numpy.array(result)


def problema3(start):
	number = generate_number(start)

	matrix_A = generate_boolean_matrix(number)
	matrix_B = generate_boolean_matrix(number)

	m = math.floor(math.log2(number))
	p = math.ceil(number / m)

	list_of_matric_from_A = matrix_A_decomposition(matrix_A, m, p)
	list_of_matric_from_B = matrix_B_decomposition(matrix_B, m, p)

	print(list_of_matric_from_A)
	print(list_of_matric_from_B)


print(problema3(4))
