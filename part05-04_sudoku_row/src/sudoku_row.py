# Write your solution here

def row_correct(sudoku: list, row_no: int):
    
    found = []
    for el in sudoku[row_no]:
        
        if (el not in found) and el > 0:
            found.append(el)
        elif el > 0:
            return False
        
    return True

