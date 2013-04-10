import curses
from tetrislib import *
import time

screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.noecho();curses.cbreak();screen.keypad(1);screen.nodelay(1);
screen.clear()
screen.border(1)
curses.curs_set(0)
screen_height, screen_width = screen.getmaxyx()
window = curses.newwin(HEIGHT+5,WIDTH+5,(screen_height-HEIGHT)/2,(screen_width-WIDTH)/2)
window.clear()

score = 0
new_piece = 1
position = [1,0]
curr_piece_index = randint(0,len(PIECES))
curr_piece = generate_piece_coords(PIECES[curr_piece_index])
draw_board(window, position, curr_piece, board, score)


delay= 0
changed = 1 
while sum(board[0])!= WIDTH:
    old_position = copy.deepcopy(position)
    old_piece = copy.deepcopy(curr_piece)
    old_piece_index = curr_piece_index
    move = screen.getch()
    
    if move == 113:
        break

    if move == curses.KEY_RIGHT:
        position[1]+=1
        if not check_horizontal_collision(position,curr_piece,board):
            changed = 1
        else:
            position = old_position

    if move==curses.KEY_LEFT:
        position[1]-=1
        if not check_horizontal_collision(position,curr_piece,board):
            changed = 1
        else:
            position = old_position

    if move==curses.KEY_UP:
        curr_piece_index = ROTDICT[curr_piece_index]
        curr_piece = generate_piece_coords(PIECES[curr_piece_index])
        if not check_rotate_collision(position, curr_piece, board):
            changed = 1
        else:
            curr_piece_index = old_piece_index
            curr_piece = old_piece
    

    if (move==curses.KEY_DOWN and position[0]<=HEIGHT-2) or delay%30000==0:   
        position[0]+=1
        if check_vertical_collision(position,curr_piece,board):
            board = update_board(old_position,curr_piece,board)
            curr_piece_index = randint(0,len(PIECES))
            curr_piece = generate_piece_coords(PIECES[curr_piece_index])
            position = [1,0]
            board,score = detect_lines(board, score) 
        changed = 1

            
    if changed == 1:
        changed = 0
        draw_board(window, position, curr_piece, board, score)
    delay +=1

curses.endwin()
print "Thank you for playing"
