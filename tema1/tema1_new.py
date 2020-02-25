import math
from itertools import permutations
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


def from_boolean_list_to_integer(boolean_list):
	integer_number = 0
	boolean_list = list(reversed(boolean_list))
	for i in range(0, len(boolean_list)):
		if boolean_list[i]:
			integer_number = integer_number + pow(2, i)
	return integer_number


def split(text):
	return [bool(int(n)) for n in text]


def generate_all_combination(num):
	result = []
	for i in range(0, pow(2, num)):
		n = str(bin(i))[2:]
		a = len(str(bin(i))[2:])
		for j in range(a, len(str(bin(num))[2:]) + 1):
			n = '0' + n
		result.append(split(n))
	return result


def generate_matrix(number_line, number_column):
	matrix = []
	for i in range(0, number_line):
		line = []
		for j in range(0, number_column):
			line.append(random.choice([True, False]))
		matrix.append(line)
	return matrix


def calculate_matrix_line_sum(matrix):
	result = []
	lists = generate_all_combination(len(matrix))
	for i in lists:
		aux = [False for t in range(0, len(matrix[0]))]
		for j in range(0, len(i)):
			if i[j]:
				aux = numpy.logical_or(aux, matrix[j])
		result.append(list(aux))
	return result


def calculate_Ci_matrix(matrix_A, matrix_B):
	Ci = []
	all_combination = calculate_matrix_line_sum(matrix_B)
	for i in matrix_A:
		num = from_boolean_list_to_integer(i)
		Ci.append(all_combination[num])
	return Ci


print(calculate_Ci_matrix(generate_matrix(7, 4) ,generate_matrix(4, 7)))
#print(calculate_matrix_line_sum(generate_matrix(4, 7)))
#print(generate_all_combination(3))
#print(generate_all_combination(generate_matrix(4, 8)))
#print(generate_number(12))
#print(from_boolean_list_to_integer([True, False, True, True]))
