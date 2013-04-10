import sys
from random import randint
import copy
import curses


#USE NO GLOBALS. Every function takes in all needed inputs and generates an output

HEIGHT = 15
WIDTH  =10
MOVES = ["r","l","u","d","q",""]
PIECES = [[[1,1,1,0],[0,1,0,0]],
          [[0,0,0,0],[1,1,1,1]],
          [[1,0,0,0],[1,1,1,0]],
          [[0,0,0,1],[0,1,1,1]],
          [[1,1,0,0],[1,1,0,0]],
          [[0,1,1,0],[1,1,0,0]],
          [[0,1,0,0],[1,1,1,0]],
          [[1,1,0,0],[0,1,1,0]]          
          ]

board = [[0 for w in range(WIDTH)] for h in range(HEIGHT)]
    
def generate_piece_coords(piece):
    piece_coords = []
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] ==1:
                piece_coords.append((i,j))
    return piece_coords

def check_collision(position, piece, board):
    for x,y in piece:
        y = y+position[0]
        x = x+position[1]
        if y == HEIGHT:
            return True
        if board[y][x] == 1:
            return True
    return False
    
def update_board(position, coords, board):
    new_board = copy.deepcopy(board)
    for x,y in coords:        
        new_board[y+position[0]][x+position[1]] = 1
    return new_board

def draw_board(position, coords, board):
    n_board = update_board(position, coords, board)
    for i in range(HEIGHT):
        row = "|"
        for j in range(WIDTH):
            if n_board[i][j]==1:
                row+="0"
            else:
                row+=" "
        print row+"|"
    print position, curr_piece_index, curr_piece
    stdscr.refresh()

def detect_lines(board):
    r_board = []
    i = 0
    while i <HEIGHT:
        while sum(board[i]) == WIDTH:
            i = i+1
        r_board.append(board[i])
        i = i+1
    for i in range(len(board)-len(r_board)):
        r_board.insert(0,[0 for j in range(WIDTH)])
    return r_board


stdscr = curses.initscr();curses.noecho();curses.cbreak();stdscr.keypad(1)
# begin_x = 20 ; begin_y = 7
# height = 5 ; width = 40
# win = curses.newwin(height, width, begin_y, begin_x)

new_piece = 1
position = [1,0]
curr_piece_index = randint(0,7)
curr_piece = generate_piece_coords(PIECES[curr_piece_index])
draw_board(position, curr_piece, board)



while sum(board[0])!= WIDTH:
    old_position = copy.deepcopy(position)
    move = 0
    while move not in MOVES:
        move  = raw_input("Next Move: ")
        print "Please input a valid move"
 
   #Process inputs
    if move == "q":
        break
    if move == "r" and position[1]<WIDTH-2:
        position[1]+=1
    if move=="l" and position[1]>=1:
        position[1]-=1
        
    #Update position and board
    position[0]+=1

    #See if this causes issues with current board
    if check_collision(position,curr_piece,board):
        print "Found an invalid position", position
        board = update_board(old_position,curr_piece,board)
        curr_piece_index = randint(0,7)
        curr_piece = generate_piece_coords(PIECES[curr_piece_index])
        position = [1,0]
    
    board = detect_lines(board) 

    draw_board(position, curr_piece, board)       
     


curses.nocbreak(); stdscr.keypad(0); curses.echo()
curses.endwin()
print "Thank you for playin"
