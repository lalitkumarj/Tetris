import sys
from random import randint
import copy
import curses 
HEIGHT = 20
WIDTH  =16
MOVES = ["r","l","u","d","q",""]
               
PIECES = [
    #Vertical Line
    [[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]],
    [[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0]],
    [[0,0,0,0],[0,0,0,0],[1,1,1,1],[0,0,0,0]],
    [[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]], 
    #L1
    [[1,0,0],[1,1,1],[0,0,0]], 
    [[0,1,1],[0,1,0],[0,1,0]],
    [[0,0,0],[1,1,1],[0,0,1]],
    [[0,1,0],[0,1,0],[1,1,0]],
    #L2
    [[0,0,1],[1,1,1],[0,0,0]], 
    [[0,1,0],[0,1,0],[0,1,1]],
    [[0,0,0],[1,1,1],[1,0,0]],
    [[1,1,0],[0,1,0],[0,1,0]],
    #BLOCK
    [[1,1,0],[1,1,0],[1,1,0]], 
    # RSquiggle
    [[0,1,1],[1,1,0],[0,0,0]], 
    [[0,1,0],[0,1,1],[0,0,1]],
    [[0,0,0],[0,1,1],[1,1,0]],
    [[1,0,0],[1,1,0],[0,1,0]],
    #T
    [[0,1,0],[1,1,1],[0,0,0]], 
    [[0,1,0],[0,1,1],[0,1,0]],
    [[0,0,0],[1,1,1],[0,1,0]],
    [[0,1,0],[1,1,0],[0,1,0]],
    # LSquiggle
    [[1,1,0],[0,1,1],[0,0,0]], 
    [[0,0,1],[0,1,1],[0,1,0]],
    [[0,0,0],[1,1,0],[0,1,1]],
    [[0,1,0],[1,1,0],[1,0,0]],
    ]

board = [[0 for w in range(WIDTH)] for h in range(HEIGHT)]
ROTDICT={0:1, 1:2, 2:3, 3:1, 4:5, 5:6, 6:7, 7:4, 8:9, 9:10, 10:11, 11:8, 12:12, 13:14, 14:15, 15:16, 16:13, 17:18, 18:19, 19:20, 20:17, 21:22, 22:23, 23:24, 24:21}
    
def generate_piece_coords(piece):
    piece_coords = []
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] ==1:
                piece_coords.append((i,j))
    return piece_coords

def check_vertical_collision(position, piece, board):
    for x,y in piece:
        y = y+position[0]
        x = x+position[1]
        if y == HEIGHT:
            return True
        if board[y][x] == 1:
            return True
    return False


def check_horizontal_collision(position, piece, board):
    for x,y in piece:
        y = y+position[0]
        x = x+position[1]
        if x >= WIDTH or x<0:
            return True
        if board[y][x] == 1:
            return True
    return False

def check_rotate_collision(position, piece, board):
    for x,y in piece:
        y = y+position[0]
        x = x+position[1]
        if x >= WIDTH or x<0 or y==HEIGHT:
            return True
        if board[y][x] == 1:
            return True
    return False

    
def update_board(position, coords, board):
    new_board = copy.deepcopy(board)
    for x,y in coords:        
        new_board[y+position[0]][x+position[1]] = 1
    return new_board

def draw_board(window, position, coords, board,score):
    n_board = update_board(position, coords, board)
    for i in range(HEIGHT):
        row = "|"
        for j in range(WIDTH):
            if n_board[i][j]==1:
                row+="0"
            else:
                row+=" "
        window.addstr(i,0, row+"|\n")
    window.addstr(HEIGHT+2,2,"Score: "+str(score), curses.color_pair(1))
    window.clrtobot()

    window.refresh()

def detect_lines(board, score):
    r_board = []
    i = 0
    while i <HEIGHT:
        while sum(board[i]) == WIDTH:
            i = i+1
            score +=1
            if i == HEIGHT:
                break
        if i<HEIGHT:
            r_board.append(board[i])
        i = i+1
    for i in range(len(board)-len(r_board)):
        r_board.insert(0,[0 for j in range(WIDTH)])
    return r_board,score


