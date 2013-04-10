import sys
from random import randint
import copy

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
    
def update_board(position, coords, board):
    new_board = copy.deepcopy(board)
    for x,y in coords:        
        new_board[y+position[0]][x+position[1]] = 1
    return new_board

def draw_board(screen, position, coords, board,score):
    n_board = update_board(position, coords, board)
    screen.clear()
    screen.border(0)
    screen_height, screen_width = screen.getmaxyx()
    for i in range(HEIGHT):
        row = "|"
        for j in range(WIDTH):
            if n_board[i][j]==1:
                row+="0"
            else:
                row+=" "
        screen.addstr(i+(screen_height-HEIGHT)/2,(screen_width-WIDTH)/2, row+"|\n")
    screen.addstr(screen_height-1,2,"Score: "+str(score))
    screen.refresh()

def detect_lines(board, score):
    r_board = []
    i = 0
    while i <HEIGHT:
        while sum(board[i]) == WIDTH:
            i = i+1
            score +=1
        r_board.append(board[i])
        i = i+1
    for i in range(len(board)-len(r_board)):
        r_board.insert(0,[0 for j in range(WIDTH)])
    return r_board,score


