import random

def user_input():

    # Function to get user input for Tic Tac Toe game
    print("Welcome to Tic Tac Toe!\n")
    print("Player 1, please choose your marker.\n")
    print("You can choose 'X' or 'O'.\n")
    print("Player 2 will automatically get the other marker.\n")
    player1 = input("Please pick a marker 'X' or 'O': ").upper()
    while player1 not in ['X', 'O']:
        print("Invalid marker. Please choose 'X' or 'O'.")
        
    print(f"Player 1 has chosen {player1}.")
    player2 = 'O' if player1 == 'X' else 'X'
    print(f"Player 2 will be {player2}.\n")
    return player1,player2

def display_board(board):

    print("Current board:")
    for i in range(3):
        print(f"{board[i*3]} | {board[i*3+1]} | {board[i*3+2]}")
        if i < 2:
            print("---------")


def place_marker(board,position,marker):
    # Function to place a marker on the board
    
    if board[position]== ' ':
        board[position] = marker
        return True
    else:
        print("Position already taken. Try again.")
        return False
   
def choose_first():
    # Function to randomly choose which player goes first
    first_player = random.choice(['Player 1', 'Player 2'])
    print(f"{first_player} will go first.")
    return first_player


def replay():
    # Function to ask players if they want to play again
    play_again = input("Do you want to play again? Enter y for Yes, n for No: ").strip().lower()
    return play_again == 'y'

player1_marker,player2_marker=user_input()
player_choice = choose_first()
board = [' ' for _ in range(9)]
display_board(board)

position = int(input("Enter a position (0-8) to place your marker: "))


if player1_marker == player_choice:
    place_marker(board, position, player1_marker)
else:
    place_marker(board, position, player2_marker)

display_board(board)

#call this at end when game finishes to ask if players want to play again
if replay():
    print("Starting a new game...")
    board = [' ' for _ in range(9)]
    display_board(board)
else:
    print("Thanks for playing! Goodbye!")
