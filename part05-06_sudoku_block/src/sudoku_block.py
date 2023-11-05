# Write your solution here

def block_correct(sudoku: list, row_no: int, column_no: int):
    found = []

    for i in range(0,3):
        for j in range(0,3):
            current = sudoku[row_no+i][column_no+j]
            if ( current not in found) and current > 0:
                found.append(current)
            elif current > 0:
                return False
            
    return True
