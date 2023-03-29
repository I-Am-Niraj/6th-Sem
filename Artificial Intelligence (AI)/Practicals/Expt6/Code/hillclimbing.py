import random

print("***** 4-Queen Problem using Hill Climbing Algorithm *****")
def get_board_cost(board):
    cost = 0
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if board[i] == board[j] or abs(board[i]-board[j]) == abs(i-j):
                cost += 1
    return cost
    
def hill_climb():
    board = [random.randint(0, 3) for _ in range(4)]
    print("Board: ", board)
    cost = get_board_cost(board)
    while cost > 0:
        new_board = list(board)
        for i in range(len(board)):
            for j in range(4):
                if j != board[i]:
                    new_board[i] = j
                    new_cost = get_board_cost(new_board)
                    if new_cost < cost:
                        board = list(new_board)
                        cost = new_cost
                        break
        if board == new_board:
            break
    return board

print("Solution: ", hill_climb())