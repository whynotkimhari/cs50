"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    check_empty = 0
    checkX = 0
    checkO = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                check_empty += 1
            elif board[i][j] == X:
                checkX += 1
            else:
                checkO += 1
    
    if check_empty == 9:
        return X
    else:
        if checkX > checkO:
            return O
        else:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_ = copy.deepcopy(board)
    if board_[action[0]][action[1]] == EMPTY:
        board_[action[0]][action[1]] = player(board_)
    else:
        raise Exception
    return board_


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if ((board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][2] == X) or 
        (board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][2] == X) or 
        (board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][2] == X) or  
        (board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[2][0] == X) or 
        (board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[2][1] == X) or 
        (board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[2][2] == X) or 
        (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == X) or
        (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == X)):
        return X
    elif ((board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][2] == O) or 
        (board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][2] == O) or 
        (board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][2] == O) or  
        (board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[2][0] == O) or 
        (board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[2][1] == O) or 
        (board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[2][2] == O) or 
        (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == O) or
        (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == O)):
        return O
    else:
        return None
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    
def minimax(board):
    moves = actions(board)
    action = (0, 0)
    if player(board) == X:
        check = -10
        for move in moves:
            value = mini(result(board, move))
            if value > check:
                check = value
                action = move 
    else:
        check = 10  
        for move in moves: 
            value = maxi(result(board, move)) 
            if value < check: 
                check = value     
                action = move   
    return action

def maxi(board):
    values = []
    if terminal(board) == True:
        return utility(board)
    for move in actions(board):
        values.append(mini(result(board, move)))
    return max(values)

def mini(board):
    values = []
    if terminal(board) == True:
        return utility(board)
    for move in actions(board):
        values.append(maxi(result(board, move)))
    return min(values)

