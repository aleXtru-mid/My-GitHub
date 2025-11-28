# Tic Tac Toe game

board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] # empty dashboard

def print_dashboard(board:list):
    """
 Print dashboard in console
    """
    print(f'  0 1 2') # print horizontal fields of dashboard
    for i in range(3):
        print(i, end=' ') # print vertical fields of dashboard
        print(*board[i], sep=' ')

def end_game(board:list):
    """
    check conditions of the end of the game
    :param board:
    :return: bool
    """
    row1 = [board[0][0],board[0][1],board[0][2]]
    row2 = [board[1][0],board[1][1],board[1][2]]
    row3 = [board[2][0],board[2][1],board[2][2]]
    row4 = [board[0][0],board[1][0],board[2][0]]
    row5 = [board[0][1],board[1][1],board[2][1]]
    row6 = [board[0][2],board[1][2],board[2][2]]
    row7 = [board[0][0],board[1][1],board[2][2]]
    row8 = [board[0][2],board[1][1],board[2][0]]
    p1_row = ['x','x','x']
    p2_row = ['o','o','o']
    if p1_row == row1 or p1_row == row2 or p1_row == row3 or p1_row == row4 or p1_row == row5 or p1_row == row6 or p1_row == row7 or p1_row == row8:
        return "x WIN !!!"
    if p2_row == row1 or p2_row == row2 or p2_row == row3 or p2_row == row4 or p2_row == row5 or p2_row == row6 or p2_row == row7 or p2_row == row8:
        return 'o WIN !!!'
    else: return False

def take_input(token:str):
    """
    check that input is correct, add token to the dashboard
    :param token: str
    :return:
    """
    valid = False
    while not valid:
        col = input(f"input column 0, 1, 2 for {token} __")
        row = input(f"input row 0, 1, 2 for {token} __")
        try:
            col = int(col)
            row = int(row)
        except ValueError:
            print("incorrect input. are you sure you've input number 0 - 2 ?")
            continue
        if 0 <= col <= 2 and 0 <= row <= 2:
            if str(board[row][col]) == ' ':
                board[row][col] = token
                valid = True
            else:
                print("this place is busy ...")
                print_dashboard(board)
        else:
            print("wrong number, please input 0 - 2 ...")
            print_dashboard(board)

def tic_tac_toe(board):
    """ function that provide the game """
    counter = 0
    victory = False
    while not victory:
        print_dashboard(board)
        if counter % 2 == 0:
            take_input("x")
        else:
            take_input("o")
        counter += 1

        chk_turn = end_game(board)
        if chk_turn:
            print(chk_turn)
            victory = True
            break
        if counter == 9:
            print("it's a draw !!!")
            victory = True
            break
    print_dashboard(board)

tic_tac_toe(board)
