import curses
from tetrislib import *
import time

#USE NO GLOBALS. Every function takes in all needed inputs and generates an output
screen = curses.initscr()
curses.noecho();curses.cbreak();screen.keypad(1);screen.nodelay(1)

score = 0
new_piece = 1
position = [1,0]
curr_piece_index = randint(0,7)
curr_piece = generate_piece_coords(PIECES[curr_piece_index])
draw_board(screen, position, curr_piece, board, score)


delay= 0
changed = 1 
while sum(board[0])!= WIDTH:
    old_position = copy.deepcopy(position)
    move = screen.getch()
    
#Process inputs
    #ASCII for q
    if move == 113:
        break

    if move == curses.KEY_RIGHT and position[1]<WIDTH-2:
        position[1]+=1
        if not check_collision(position,curr_piece,board):
            changed = 1
        else:
            position = old_position
    if move==curses.KEY_LEFT and position[1]>0:
        position[1]-=1
        if not check_collision(position,curr_piece,board):
            changed = 1
        else:
            position = old_position

    if (move==curses.KEY_DOWN and position[0]<=HEIGHT-2) or delay%30000==0:   
        position[0]+=1
        if check_collision(position,curr_piece,board):
            board = update_board(old_position,curr_piece,board)
            curr_piece_index = randint(0,7)
            curr_piece = generate_piece_coords(PIECES[curr_piece_index])
            position = [1,0]
            board,score = detect_lines(board, score) 
        changed = 1
    #Update position and board
    # if delay %50000 == 0:
    #     changed = 1
    #     position[0]+=1

    # #See if this causes issues with current board
    #  if check_collision(position,curr_piece,board):
    #     changed = 1
    #     board = update_board(old_position,curr_piece,board)
    #     curr_piece_index = randint(0,7)
    #     curr_piece = generate_piece_coords(PIECES[curr_piece_index])
    #     position = [1,0]
    #     board = detect_lines(board) 
    if changed == 1:
        changed = 0
        draw_board(screen, position, curr_piece, board, score)
    delay +=1

#curses.nocbreak(); 
#screen.keypad(0); 
#screen.echo()
#screen.nodelay
curses.endwin()
print "Thank you for playing"
