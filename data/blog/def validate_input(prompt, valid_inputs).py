def validate_input(prompt, valid_inputs):
    """
	Repeatedly ask user for input until they enter an input
	within a set valid of options.

	:param prompt: The prompt to display to the user, string.
	:param valid_inputs: The range of values to accept, list
	:return: The user's input, string.
	"""
    while True:
        chosen_input = input(prompt)
        if chosen_input not in valid_inputs:
            print('Invalid input, please try again.')

        else:
            return(chosen_input)
        
if __name__ == "__main__":
    user_input = validate_input("Please select an option (a, b, c): ", ["a", "b", "c"])

def create_board():
    """
	Returns a 2D list of 6 rows and 7 columns to represent
	the game board. Default cell value is 0.

	:return: A 2D list of 6x7 dimensions.
	"""
    board = []
    for row in range(6):
        board.append([])
        for columns in range(7):
            board[row].append(0)
    return board

if __name__ == "__main__":
    print(create_board())

def print_board(board):
    """
	Prints the game board to the console.

	:param board: The game board, 2D list of 6x7 dimensions.
	:return: None
	"""
    for row in range(6):
        for columns in range(7):
            if board[row][columns] == 0:
                board[row][columns] = " "
            elif board[row][columns] == 1:
                board[row][columns] = X
            elif board[row][columns] == 2:
                board[row][columns] = O

    visual = "========== Connect4 =========\n"
    visual += "Player 1: X       Player 2: O\n"
    visual += "\n 1   2   3   4   5   6   7"
    visual += "\n --- --- --- --- --- --- ---"
    print(visual)

    for row in range(6):
        print("|",end='')
        for columns in range(7):
            print(board[row][columns],end='  |')
        print("\n --- --- --- --- --- --- ---")
    print('=============================')

if __name__ == "__main__":
    board = create_board()
    print_board(board)

def drop_piece(board,player,column):
    counter = 5
    while(counter > -1):
        if(board[counter][column-1]==0):
            board[counter][column-1] = player
            counter = -3
        else:
            counter = counter - 1
        if (counter == -1):
            counter = -5
    if(counter == -3):
        return True
    elif(counter == -5):
        return False
    
if __name__ == "__main__":
	board = create_board()
	for row in board:
		print(row)

def execute_player_turn(player, board):
    turn = 0

    if turn == 0:
        player_column = int(input("Player 1, please enter the column you would like to drop your piece into: "))
        print(drop_piece(board, player_column, 4) )
        turn += 1
    elif turn == 1:
        player_column = int(input("Player 1, please enter the column you would like to drop your piece into: "))
        print(drop_piece(board, player_column, 4 ))
        turn -= 2
    
    raise NotImplementedError

if __name__ == "__main__":
	# Enter test code below
	board = create_board()
	move = execute_player_turn(1, board)
	print(move)