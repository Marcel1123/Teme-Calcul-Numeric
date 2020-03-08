import time


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


start_time = time.time()
##### Initializare matrici si vectori #####
matrix_A1, size_A1 = build_efficient_matrixes("a_1.txt")
matrix_A2, size_A2 = build_efficient_matrixes("a_2.txt")
matrix_A3, size_A3 = build_efficient_matrixes("a_3.txt")
matrix_A4, size_A4 = build_efficient_matrixes("a_4.txt")
matrix_A5, size_A5 = build_efficient_matrixes("a_5.txt")
vector_B1, size_B1 = build_vector("b_1.txt")
vector_B2, size_B2 = build_vector("b_2.txt")
vector_B3, size_B3 = build_vector("b_3.txt")
vector_B4, size_B4 = build_vector("b_4.txt")
vector_B5, size_B5 = build_vector("b_5.txt")
end_time = time.time() - start_time
print(end_time)

print(matrix_A1[0])
