import tkinter as tk
import random
import argparse



sudoku = [
    [0,0,0,0,0,0,6,8,0],
    [0,0,0,0,7,3,0,0,9],
    [3,0,9,0,0,0,0,4,5],
    [4,9,0,0,0,0,0,0,0],
    [8,0,3,0,5,0,9,0,2],
    [0,0,0,0,0,0,0,3,6],
    [9,6,0,0,0,0,3,0,8],
    [7,0,0,6,8,0,0,0,0],
    [0,2,8,0,0,0,0,0,0],
]
def algo(sud):
    #print_sudoku(sud)
    #print("iteration")
    find = find_empty(sud)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if validation_check(sud, i, (row,col)):
            sud[row][col] = i

            if algo(sud):
                return True

            sud[row][col] = 0

    return False



def print_sudoku(sud):

    for i in range(len(sud)):
        for j in range(len(sud[0])):
            print(sud[i][j],end=" ")

        print("")

def find_empty(sud):
    for i in range(len(sud)):
        for j in range(len(sud[0])):
            if sud[i][j]==0:
                return (i, j)

    return None

def validation_check(sud, no, pos):

    for i in range(len(sud[0])):
        if sud[pos[0]][i] == no and pos[1] != i:
            return False

    for i in range(len(sud)):
        if sud[i][pos[1]] == no and pos[0] != i:
            return False

    x = pos[1]//3
    y= pos[0]//3

    for i in range(y*3,y*3+3):
        for j in range(x*3, x*3+3):
            if sud[i][j]== no and (i,j)!=pos:
                return False
        
    
    return True    
    

    






print_sudoku(sudoku)
algo(sudoku)
print("after solving")
print_sudoku(sudoku)

