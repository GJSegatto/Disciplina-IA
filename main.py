def print_board(board):
    """Function to print the Tic-Tac-Toe board."""
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def check_winner(board, player):
    """Function to check if a player has won the game."""
    
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Verify columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Verify diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_board_full(board):
    """Function to check if the board is full."""
    
    for row in board:
        if ' ' in row:
            return False
    return True

def get_score(board):
    """Function to get the score of the game."""
    
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing):
    """Function to implement the minimax algorithm."""
    
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[row][col] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ' '
                    best_score = min(score, best_score)
        return best_score

def make_move(board):
    """Function to make a move for the machine."""

    best_score = float('-inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'
                score = minimax(board, 0, False)
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    board[best_move[0]][best_move[1]] = 'X'

def play_game():
    """Main loop to play the game."""
    
    board = [[' ' for i in range(3)] for i in range(3)]
    print('Bem-vindo ao Jogo da Velha!')
    print_board(board)

    while True:
        #Player make its move
        row = int(input('Digite o número da linha (1-3): '))
        col = int(input('Digite o número da coluna (1-3): '))
        if board[row-1][col-1] != ' ':
            print('Essa posição já está ocupada. Tente novamente.')
            continue
        board[row-1][col-1] = 'O'
        print_board(board)

        #Check if player wins
        if check_winner(board, 'O'):
            print('Você ganhou! Parabéns!')
            break

        #Check if game ties
        if is_board_full(board):
            print('O jogo empatou!')
            break

        #Machine Move
        make_move(board)
        print('A máquina fez sua jogada:')
        print_board(board)

        if check_winner(board, 'X'):
            #Check if machine wins
            print('A máquina ganhou! Tente novamente.')
            break

        
        if is_board_full(board):
            #Check if game ties
            print('O jogo empatou!')
            break
        
play_game()