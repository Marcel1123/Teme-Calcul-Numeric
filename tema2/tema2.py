import numpy
import math
import random


"""
def precizie_masina():
	precizie = 1
	while True:
		if 1 + pow(10, - precizie) == 1:
			return precizie - 1
		else:
			precizie += 1


def tema2(dimensiune):
	epsilon = pow(10, - precizie_masina())
	matrix_A = numpy.array([[random.randint(1, 10) for i in range(0, dimensiune)] for j in range(0, dimensiune)])
	vector_terminali = numpy.array([random.randint(1,10) for i in range(0, dimensiune)])
	matrix_A = list(numpy.linalg.lu(matrix_A))
	print("Matrix: ", matrix_A)
	print(numpy.linalg.det(matrix_A))
"""
#print(tema2(10))
def generate_single_one_matrix(dimension, index):
	if index == 0:
		result = [1]
		for i in range(0, dimension - 1):
			result.append(0)
		return result
	else:
		result = []
		for i in range(0, index):
			result.append(0)
		result.append(1)
		for i in range(0, dimension - len(result)):
			result.append(0)
		return result
		

def inv_function(L_matrix, U_matrix, A_matrix):
	result = [[] for i in range(0, len(A_matrix))]
	
	for i in range(0, len(A_matrix)):
		y_star = numpy.linalg.solve(L_matrix, generate_single_one_matrix(len(A_matrix), i))
		x_star = numpy.linalg.solve(U_matrix, y_star)
		for j in range(0, len(A_matrix)):
			result[j].append(x_star[j])
	return result


# print(generate_single_one_matrix(10, 2))
print(inv_function([[1,0,0], [2,1,0], [2,1,1]], 
					[[2.5, 2, 2], [0, 2, 1], [0,0,1.5]],
					[[2.5, 2,2], [5,6,5], [5,6,6.5]]))
