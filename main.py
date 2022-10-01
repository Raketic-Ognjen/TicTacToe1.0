# Starting with the Tic Tac Toe project

# 1st step: Make the Tic Tac Toe Board with dictionary

theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)


# 2nd step: Print updated board after every move in the game.

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


# 3rd step: main function which has all game func

def game(turn,count):

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn " + turn + ". Move to which place?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

            # 3.1 checking if X or O player won for every move after 5 moves

            if count >= 5:
                if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across The top
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the Middle
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the bottom
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # Down the Left Side
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # Down the middle
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # Down the right
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':  # Diagonal
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # Diagonal
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break

                # 3.2 if game has no winner

                if count == 9:
                    print("\nGame Over. \n")
                    print("It's a Tie!!!")

                # 4 Change player after every move

                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'

                restart = input('Do You want to play again? Y/N')
                if restart == 'Y' or restart == 'y':
                    for key in board_keys:
                        theBoard[key] = " "

                    game(turn,count)
                    turn = 'X'
                    count = 0
game('X',0)