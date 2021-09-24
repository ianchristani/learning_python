import random

#--------------------------------------- necessary loads -----------------------------------------------------
board = [{1:1,2:2,3:3},{1:4,2:'X',3:6},{1:7,2:8,3:9}]

while True:
    #--------------------------------------- functions to draw the board -------------------------------------
    def bhl():
        print('+-------'*3 + '+')

    def bvl():
        print('|       '*3 + '|')

    def bvlp(y):
        print(f'|   {y}   ', end='')

    #---------------------------------------- show the curent board status -----------------------------------
    def display_board(board):
        for n in board:
            bhl()
            bvl()
            for y in n.values():        
                bvlp(y)
            print('|')
            bvl()
        bhl()

    #---------------------------------------- the player's turn ----------------------------------------------
    def enter_move(board):
        pturn = int(input('where do you want to mark: '))

        if  pturn in range (1,4):
            if board [0][pturn] == 'X' or board [0][pturn] == 'O':
                print('this position was chosen already!')
            else:
                board [0][pturn] = 'O'

        if pturn in range (4,7):
            if pturn == 4: pturn = 1
            if pturn == 5: pturn = 2
            if pturn == 6: pturn = 3
            if board [1][pturn] == 'X' or board [1][pturn] == 'O':
                print('this position was chosen already!')
            else:
                board [1][pturn] = 'O'

        if pturn in range (7,10):
            if pturn == 7: pturn = 1
            if pturn == 8: pturn = 2
            if pturn == 9: pturn = 3
            if board [2][pturn] == 'X' or board [2][pturn] == 'O':
                print('this position was chosen already!')    
            else:
                board [2][pturn] = 'O'
                

    #---------------------------------------- game analysis ---------------------------------------------------    
    def game_analisys(board):
      
        #horizontal
        for n in range (0,3):
            if board[n][1] == board [n][2] == board [n][3]:
                victory_for(board,board[n][1])
            else:
                continue

        #diagonal
        if board[0][1] == board[1][2] == board[2][3] or board[0][3] == board[1][2] == board[2][1]:
            victory_for(board,board[1][2])

        #vertical
        for n in range (1,4):
            if board[0][n] == board [1][n] == board [2][n]:
                victory_for(board,board[0][n])
            else:
                continue

    #---------------------------------------- PRIZE ---------------------------------------------------------------
    def victory_for(board, sign):
        if sign == 'O':
            print ('YOU WIN!!!! :D')
            return False
        else:
            print ('LOOOOOOOOOSERRRR!! ahahahaha')
            return False

#---------------------------------------- the computer's turn --------------------------------------------------
    def draw_move(board):
        cturn = random.randint(1,10)

        if cturn in range (1,4):
            if board [0][cturn] == 'X' or board [0][cturn] == 'O':
                draw_move(board)
            else:
                board [0][cturn] = 'X'

        if cturn in range (4,7):
            if cturn == 4: cturn = 1
            if cturn == 5: cturn = 2
            if cturn == 6: cturn = 3
            if board [1][cturn] == 'X' or board [1][cturn] == 'O':
                draw_move(board)
            else:
                board [1][cturn] = 'X'

        if cturn in range (7,10):
            if cturn == 7: cturn = 1
            if cturn == 8: cturn = 2
            if cturn == 9: cturn = 3
            if board [2][cturn] == 'X' or board [2][cturn] == 'O':
                draw_move(board)    
            else:
                board [2][cturn] = 'X'

    #-------------------------------------------- The game sequence ----------------------------------------------
    display_board(board)
    enter_move(board)
    game_analisys(board)
    draw_move(board)
    game_analisys(board)