# Write your solution here


letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

layers = int(input("Layers: "))
n = 2*layers - 1
matrix = []
for i in range(layers):
    char = ''
    new_row = []
    for j in range(layers):
        if j <= i:
            char = letters[layers-1-j]
        new_row.append(char)
    matrix.append(new_row)


for i in range(layers):
    new_row = matrix[i].copy()
    new_row.reverse()
    for j in range(1,layers):
        matrix[i].append(new_row[j])


for i in range(layers-1):
    new_row = matrix[layers -2 - i].copy()
    matrix.append(new_row)


for row in matrix:
    for el in row:
        print(el,end='')
    print("")