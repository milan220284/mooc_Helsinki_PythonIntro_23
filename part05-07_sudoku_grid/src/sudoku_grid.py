# Write your solution here

def row_correct(sudoku: list, row_no: int):
    
    found = []
    for el in sudoku[row_no]:
        
        if (el not in found) and el > 0:
            found.append(el)
        elif el > 0:
            return False
        
    return True


def column_correct(sudoku: list, column_no: int):
    found = []
    for row in sudoku:
        
        if (row[column_no] not in found) and row[column_no] > 0:
            found.append(row[column_no])
        elif row[column_no] > 0:
            return False
        
    return True

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


def sudoku_grid_correct(sudoku: list):
    for i in range(0,9):
        if not (column_correct(sudoku, i) and row_correct(sudoku, i)):
            return False
    
    for i in range(0,3):
        for j in range(0,3):
            if not block_correct(sudoku, 3*i, 3*j):
                return False
        
    return True
