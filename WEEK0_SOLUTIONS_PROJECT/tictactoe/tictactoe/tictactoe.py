"""
Tic Tac Toe Player
"""
import copy
import math

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
    if board == initial_state():
        return X

    x_move = 0
    o_move = 0
    for row in board:
        x_move += row.count(X)
        o_move += row.count(O)

    if x_move == o_move:
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                result.append([row, col])
    return result


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    try:
        if board_copy[action[0]][action[1]] != EMPTY:
            raise IndexError
        else:
            board_copy[action[0]][action[1]] = player(board_copy)
            return board_copy
    except IndexError:
        print("Spot already occupied")





def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check Row
    for row in board:
        x_move = row.count(X)
        o_move = row.count(O)
        if x_move == 3:
            return X
        if o_move == 3:
            return O

    # checks columns
    for columns in range(len(board)):
        if board[columns][0] == board[columns][1] == board[columns][2] == X:
            return X
        elif board[columns][0] == board[columns][1] == board[columns][2] == O:
            return O

    # checks diagonally
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_counter = 0
    for row in board:
        empty_counter += row.count(EMPTY)
    if empty_counter == 0:
        return True
    elif winner(board) is not None:
        return True
    else:
        return False


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
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)
    best_move = []
    if current_player == X:
        v = -math.inf
        for action in actions(board):
            k = min_value(result(board, action))
            if k > v:
                v = k
                best_move = action
    else:
        v = math.inf
        for action in actions(board):
            k = max_value(result(board, action))
            if k < v:
                v = k
                best_move = action
    return best_move



def max_value(board):
    """
    Returns the min value for the current player
    """
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = min(v , min_value(result(board,action)))
    return v

def min_value(board):
    """
    Returns the min value for the current player
    """
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, min_value(result(board,action)))
    return v