import random
board = [' ' for x in range(10)]

def insertMark(mark,pos):
    board[pos] = mark

def isSpaceFree(pos):
    return board[pos] == " "

def printBoard(board):
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("-----------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("-----------")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")

def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True

def isWinner(b,m):
    return (b[1] == m and b[2] == m and b[3] == m) or (b[4] == m and b[5] == m and b[6] == m) or \
           (b[7] == m and b[8] == m and b[9] == m) or (b[1] == m and b[4] == m and b[7] == m) or \
           (b[2] == m and b[5] == m and b[8] == m) or (b[3] == m and b[6] == m and b[9] == m) or \
           (b[1] == m and b[5] == m and b[9] == m) or (b[3] == m and b[5] == m and b[7] == m)

def playerMove():
    game_run = True
    while game_run:
        player_move = input("Select position to place 'O' (1-9):\n")
        try:
            player_move = int(player_move)
            if 0 < player_move < 10:
                if isSpaceFree(player_move):
                    game_run = False
                    insertMark("O", player_move)
                else:
                    print("You cannot place 'O' in this place")
            else:
                print("Please type a number from 1 to 9!")
        except:
            print("Please type a number!")

def computerMove():
    possibleMoves = [x for x, mark in enumerate(board) if mark == " " and x != 0]
    computer_move = 0

    for sign in ["O", "X"]:
        for i in possibleMoves:
            board_copy = board[:]
            board_copy[i] = sign
            if isWinner(board_copy, sign):
                computer_move = i
                return computer_move

    corner_free = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            corner_free.append(i)

    if len(corner_free) > 0:
        computer_move = selectRandomMove(corner_free)
        return computer_move

    if 5 in possibleMoves:
        computer_move = 5
        return computer_move

    edge_free = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edge_free.append(i)

    if len(edge_free) > 0:
        computer_move = selectRandomMove(edge_free)
        return computer_move

def selectRandomMove(moves):
    len_moves = len(moves)
    r = random.randrange(0, len_moves)
    return moves[r]

def main():
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, "X")):
            playerMove()
            printBoard(board)
        else:
            print("You lose!")
            break

        if not(isWinner(board, "O")):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertMark("X", move)
                print("Computer placed 'X' on position ", move, ":")
                printBoard(board)
        else:
            print("You win!")
            break

    if isBoardFull(board):
        print("Tie game!")
print("This is Tic Tac Toe by Max\n")

print(" 1 | 2 | 3 ")
print("-----------")
print(" 4 | 5 | 6 ")
print("-----------")
print(" 7 | 8 | 9 ")
print("-----------------")

while True:

    start = input("Do you want to play a game? Y/N\n")

    if start.lower() == "y":
        board = [" " for x in range(10)]
        main()
    else:
        break


