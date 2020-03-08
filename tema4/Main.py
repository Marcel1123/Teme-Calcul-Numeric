import time


def precizie_masina():
    precizie = 1
    while True:
        if 1 + pow(10, - precizie) == 1:
            return precizie - 1
        else:
            precizie += 1


def build_efficient_matrixes(txt):
    with open(txt, "r") as file:
        size_a = int(file.readline().split("\n")[0])
        matrix = [[] for i in range(0, size_a)]
        for line in file:
            line_array = line.split(", ")
            line_array[-1] = line_array[-1].split("\n")[0]
            if line_array == ['']:
                break
            flag = False
            for element in matrix[int(line_array[1])]:
                if element[1] == int(line_array[2]):
                    element[0] += int(line_array[0])
                    flag = True
            if flag is False:
                matrix[int(line_array[1])].append([float(line_array[0]), int(line_array[2])])
    return matrix, size_a


def build_vector(txt):
    with open(txt, "r") as file:
        size_vector = file.readline()
        return_vector = []
        for line in file:
            line_array = line.split("\n")[0]
            if line_array is '':
                break
            return_vector.append(float(line_array))
    return return_vector, size_vector


def test_matrix(matrix, size, precision):
    count = 0
    for i in range(0, size):
        for j in matrix[i]:
            if j[1] == i:
                if abs(j[0]) > precision:
                    count += 1
    if count == size:
        return True
    return False


def build_even_more_efficient_matrixes(txt):
    valori = []
    ind_col = []
    with open(txt, "r") as file:
        size_matrix = int(file.readline())
        inceput_linii = [-1 for i in range(0, size_matrix + 1)]
        for line in file:
            line_array = line.split(", ")
            line_array[-1] = line_array[-1].split("\n")[0]
            line_array[0] = line_array[0].split(" ")[0]
            if line_array == ['']:
                break
            current_line = int(line_array[1])
            current_column = int(line_array[2])
            current_value = float(line_array[0])
            if inceput_linii[current_line] == -1:
                inceput_linii[current_line] = len(valori)
            flag = False
            for i in range(inceput_linii[current_line], len(valori)):
                if ind_col[i] == current_column:
                    valori[i] += current_value
                    flag = True
            if flag is False:
                valori.append(current_value)
                ind_col.append(current_column)
    inceput_linii[-1] = len(valori) + 1
    return valori, ind_col, inceput_linii



start_time = time.time()
##### Initializare matrici si vectori #####
matrix_A1, size_A1 = build_efficient_matrixes("a_1.txt")
matrix_A2, size_A2 = build_efficient_matrixes("a_2.txt")
matrix_A3, size_A3 = build_efficient_matrixes("a_3.txt")
matrix_A4, size_A4 = build_efficient_matrixes("a_4.txt")
matrix_A5, size_A5 = build_efficient_matrixes("a_5.txt")
# vector_B1, size_B1 = build_vector("b_1.txt")
# vector_B2, size_B2 = build_vector("b_2.txt")
# vector_B3, size_B3 = build_vector("b_3.txt")
# vector_B4, size_B4 = build_vector("b_4.txt")
# vector_B5, size_B5 = build_vector("b_5.txt")
end_time = time.time() - start_time
print(end_time)
start_time = time.time()
valori_a1, ind_col_a1, inceput_linii_a1 = build_even_more_efficient_matrixes("a_1.txt")
valori_a2, ind_col_a2, inceput_linii_a2 = build_even_more_efficient_matrixes("a_2.txt")
valori_a3, ind_col_a3, inceput_linii_a3 = build_even_more_efficient_matrixes("a_3.txt")
valori_a4, ind_col_a4, inceput_linii_a4 = build_even_more_efficient_matrixes("a_4.txt")
valori_a5, ind_col_a5, inceput_linii_a5 = build_even_more_efficient_matrixes("a_5.txt")
end_time = time.time() - start_time
print(end_time)

