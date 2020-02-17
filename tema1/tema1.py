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



print(problema2())
