
def build_efficient_matrixes(txt, matrix):
    with open(txt, "r") as file:
        size_a = int(file.readline().split("\n")[0])
        current_line = 0
        for line in file:
            line_array = line.split(", ")
            line_array[-1] = line_array[-1].split("\n")[0]
            # print(line_array[1])
            if line_array == ['']:
                break
            if current_line != int(line_array[1]):
                matrix.append([])
                current_line = int(line_array[1])
                matrix[-1].append([float(line_array[0]), int(line_array[2])])
            else:
                flag = False
                for element in matrix[-1]:
                    if element[1] == int(line_array[2]):
                        element[0] = element[0] + float(line_array[0])
                        flag = True
                        break
                if not flag:
                    matrix[-1].append([float(line_array[0]), int(line_array[2])])
    return matrix, size_a


def array_sum(first_list, second_list):
    second_list = {v: k for k, v in second_list}
    for i in first_list:
        if i[1] in second_list.keys():
            second_list[i[1]] = second_list.get(i[1]) + i[0]
        else:
            second_list[i[1]] = i[0]
    return sorted([[v, k] for k, v in second_list.items()], key=lambda x: x[1])


def array_product(first_list, second_list):
    return 0
new_matrix_A, size_A = build_efficient_matrixes("a.txt", [[]])
# new_matrix_B, size_B = build_efficient_matrixes("b.txt", [[]])
# new_matrix_AplusB, size_AplusB = build_efficient_matrixes("aplusb.txt", [[]])
# new_matrix_AoriB, size_AoriB = build_efficient_matrixes("aorib.txt", [[]])
# sum_matrix = list(map(array_sum, new_matrix_A, new_matrix_B))
