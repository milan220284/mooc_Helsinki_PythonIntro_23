# Write your solution here

def column_correct(sudoku: list, column_no: int):
    found = []
    for row in sudoku:
        
        if (row[column_no] not in found) and row[column_no] > 0:
            found.append(row[column_no])
        elif row[column_no] > 0:
            return False
        
    return True

