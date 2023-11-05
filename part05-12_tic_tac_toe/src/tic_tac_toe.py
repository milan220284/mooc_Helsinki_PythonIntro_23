# Write your solution here

def play_turn(game_board: list, x: int, y: int, piece: str):
    if (x >= len(game_board)) or (y >= len(game_board)) or  (x < 0) or (y < 0) :
        return False
    elif game_board[y][x] != "":
        return False
    else:
        game_board[y][x] = piece
        return True