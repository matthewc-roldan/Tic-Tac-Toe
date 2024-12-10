# Matthew Chaparro-Roldan
# Tic tac toe
# COP 2500
# October 28, 2024

# Sets up the board with vertical and horizontal lines and print X or O's
# Depending on the input
def print_board(b):
    for row in range(3):
        for col in range(3):
            if b[row] [col] == 1:
                print("X", end="")
            elif b[row] [col] == 2:
                print("O", end="")
            else:
                print(" ", end="")
            if (col != 2):
                print("|", end="")
                
        print() # This gives us a newline at the end of each row.
        if row != 2:
            print("-+-+-")
# Checks the win by looping through and seeing whether there is 3 X's in a row
# Or if there are 3 O's in a row.
def check_win(b):
    for i in range(3):
        if b[0][i] == 1 and b[1][i] == 1 and b[2][i] == 1:
            return 1
        if b[i][0] == 1 and b[i][1] == 1 and b[i][2] == 1:
            return 1
        if b[0][i] == 2 and b[1][i] == 2 and b[2][i] == 2:
            return 2
        if b[i][0] == 2 and b[i][1] == 2 and b[i][2] == 2:
            return 2
    if b[0][0] == 1 and b[1][1] == 1 and b[2][2] == 1:
            return 1
    if b[2][0] == 1 and b[1][1] == 1 and b[0][2] == 1:
            return 1
    if b[0][0] == 2 and b[1][1] == 2 and b[2][2] == 2:
            return 2
    if b[2][0] == 2 and b[1][1] == 2 and b[0][2] == 2:
            return 2
        
    return 0
def main():
    # You can make a list of lists
    # This is known as a 2D list
    board =[ [0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0] ]

    turn = 0
    winner = 0

    # Row major order
    #print(board[1])
    #print(board[1][2])
    
    # While loop to iterate through the turns and receive the inputs
    while (turn < 9 and winner == 0):
        print_board(board)
        print("It is player #", turn % 2 +1,"'s turn")
        print("Where do you want to go?")
        row = int(input())
        col = int(input())
        row -= 1
        col -= 1

        # Checks to see if spot is taken and prints error message if taken
        if board[row][col] == 0:
            board[row] [col] = turn % 2 + 1
            turn += 1
            winner = check_win(board)

        else:
            print("That space is taken. Try again")

    #print_board(board)
    if winner ==0:
        print("Tied game")
    elif winner == 1:
        print("X wins")
    else:
        print("O wins")

main()
