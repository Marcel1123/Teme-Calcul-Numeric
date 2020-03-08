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


def array_sum(first_list, second_list):
    first_list = {v: k for k, v in first_list}
    for i in second_list:
        if i[1] in first_list.keys():
            first_list[i[1]] = first_list.get(i[1]) + i[0]
        else:
            first_list[i[1]] = i[0]
    return [[v, k] for k, v in first_list.items()]


def sort_matrix(matrix):
    for i in range(0, len(matrix)):
        matrix[i] = sorted(matrix[i], key=lambda x: x[1])
    return matrix

def array_product(first_matrix, second_matrix):
    result_matrix = []
    dictionary = {}
    for a_line in first_matrix:
        dictionary.clear()
        for a_colum in a_line:
            for b_line in second_matrix[a_colum[1]]:
                if b_line[1] in dictionary.keys():
                    dictionary[b_line[1]] += b_line[0] * a_colum[0]
                else:
                    dictionary[b_line[1]] = b_line[0] * a_colum[0]
        result_matrix.append([[v, k] for k, v in dictionary.items()])
    return result_matrix

start = time.time()

new_matrix_A, size_A = build_efficient_matrixes("a.txt")
new_matrix_B, size_B = build_efficient_matrixes("b.txt")
new_matrix_AplusB, size_AplusB = build_efficient_matrixes("aplusb.txt")
new_matrix_AoriB, size_AoriB = build_efficient_matrixes("aorib.txt")
sum_matrix = list(map(array_sum, new_matrix_A, new_matrix_B))
new_matrix_AplusB = sort_matrix(new_matrix_AplusB)
sum_matrix = sort_matrix(sum_matrix)
product_matrix = array_product(new_matrix_A, new_matrix_B)
product_matrix = sort_matrix(product_matrix)
new_matrix_AoriB = sort_matrix(new_matrix_AoriB)

if new_matrix_AplusB == sum_matrix:
    print("Sumele sunt egale")
else:
    print("Sumele nu sunt egale")

if new_matrix_AoriB == product_matrix:
    print("Produsele sunt egale")
else:
    print("Produsele nu sunt egale")

end_time = time.time() - start
print(end_time)

print(new_matrix_A[0])