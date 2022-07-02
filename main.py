# Xs and zeros game

import random


def display_board(board):
    print("\n" * 100)
    print(" " + " " + " " + "|" + " " + " " + " " + "|" + " ")
    print(" " + " " + board[7] + "|" + " " + board[8] + " " + "|" + board[9])
    print(" " + " " + " " + "|" + " " + " " + " " + "|" + " ")
    print("---|---|---")
    print(" " + " " + " " + "|" + " " + " " + " " + "|" + " ")
    print(" " + " " + board[4] + "|" + " " + board[5] + " " + "|" + board[6])
    print(" " + " " + " " + "|" + " " + " " + " " + "|" + " ")
    print("---|---|---")
    print(" " + " " + " " + "|" + " " + " " + " " + "|" + " ")
    print(" " + " " + board[1] + "|" + " " + board[2] + " " + "|" + board[3])
    print(" " + " " + " " + "|" + " " + " " + " " + "|" + " ")


def player_input():
    """
    OUTPUT = (Player 1 marker, Player 2 marker)
    """
    marker = ""
    while marker != "X" and marker != "O":
        marker = input("Please, chose a symbol X or O: ").upper()

    if marker == "X":
        return "X", "O"
    else:
        return "O", "X"


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (
            board[7] == board[8] == board[9] == mark):
        return True
    elif (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (
            board[3] == board[6] == board[9] == mark):
        return True
    elif (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark):
        return True
    else:
        return False


def chose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Please input a position number: (1-9)"))
    return position


def replay():
    choice = input("Do you want to play again? Press Yes or No: ")
    return choice == "Yes"


print("Greetings in the game!")

# Cycle while
while True:
    # Game
    # Settings
    the_board = [" "] * 10
    player1_marker, player2_marker = player_input()  # Tuple unpacking

    turn = chose_first()
    print(turn + " come first")

    play_game = input("Are you ready to play? Yes or No: ")

    if play_game == "Yes":
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == "Player 1":
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 1 win!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("No one win!")
                    game_on = False
                else:
                    turn = "Player 2"
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Player 2 win!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("No one win!")
                    game_on = False
                else:
                    turn = "Player 1"

    if not replay():
        break
    # Break
