# Write your solution here

def print_sudoku(sudoku: list):
    i = 0
    for row in sudoku:
        if i == 3 or i == 6:
                print("")
        j = 0
        for el in row:
            if j == 3 or j == 6:
                print(" ", end="")
            if el != 0:
                print(f"{el} ", end="")
            else:
                print("_ ", end="")
            j += 1
        print("")
        i += 1
    



def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    copy_sudoku = []
    for i in range(9):
        new_row = []
        for j in range(9):
            new_row.append(sudoku[i][j])
        copy_sudoku.append(new_row)

    copy_sudoku[row_no][column_no] = number

    return copy_sudoku
