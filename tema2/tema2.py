import numpy
import math
import random
import scipy.linalg as la


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
	matrix_L, matrix_U = la.lu(matrix_A)
	print(matrix_A)
	print(matrix_L)
	print(matrix_U)

print(tema2(10))
