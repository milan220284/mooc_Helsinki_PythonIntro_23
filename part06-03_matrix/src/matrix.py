# write your solution here


def read_matrix():
    matrix = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")    
            parts = line.split(",")
            new_row = []
            for el in parts:
                new_row.append(int(el))
            matrix.append(new_row)
    return matrix


def matrix_sum():
    row_sum = row_sums()
    sum = 0
    for el in row_sum:
        sum += el
    return sum


def matrix_max():
    matrix = read_matrix()
    max = matrix[0][0]
    for row in matrix:
        for el in row:
            if el > max:
                max = el
    return max


def row_sums():
    row_summ = []
    matrix = read_matrix()
    for row in matrix:
        sum = 0
        for el in row:
            sum += el
        row_summ.append(sum)
    return row_summ
