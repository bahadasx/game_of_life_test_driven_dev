import pytest

def neighborCount(board, i, j):
    neighborcnt = 0
    for cindex, col in enumerate(board):
        for rindex, cell in enumerate(col):
            rdistance = abs(rindex - j)
            cdistance = abs(cindex - i)
            if rdistance <= 1 and cdistance <= 1:
                if (rdistance + cdistance > 0):
                    if cell > 0:
                        neighborcnt += 1
                        #print('is neighbor')
            #print(cindex, rindex, '-', cdistance, rdistance, '-', cell)
    return neighborcnt

def test_three_neighbor_count():
    board = [
        [0,0,0],
        [1,1,1],
        [0,0,0]
    ]
    assert neighborCount(board, 0, 1) == 3

def test_one_neighbor_count():
    board = [
        [0,0,0],
        [1,1,1],
        [0,0,0]
    ]
    assert neighborCount(board, 1, 0) == 1

def test_two_diff_neighbor_count():
    board = [
        [0,0,0],
        [1,1,1],
        [0,0,0]
    ]
    assert neighborCount(board, 0, 0) == 2


def newCell(board, i, j):
    newCellValue = 0
    neighbors = neighborCount(board, i, j)
    currentCellValue = board[i][j]
    if currentCellValue == 0:
        if neighbors == 3:
            newCellValue = 1
    else:
        if neighbors == 2 or neighbors == 3:
            newCellValue = 1
    return newCellValue


def test_live_one_neighbor():
    board = [
        [0,0,0],
        [1,1,1],
        [0,0,0]
    ]
    assert newCell(board, 1, 0) == 0

def test_dead_two_neighbor():
    board = [
        [0,0,0],
        [1,1,1],
        [0,0,0]
    ]
    assert newCell(board, 0, 2) == 0

def test_dead_three_neighbor():
    board = [
        [0,0,0],
        [1,1,1],
        [0,0,0]
    ]
    assert newCell(board, 2, 1) == 1

def changeBoard(board):
    newBoard = [];
    for cindex, col in enumerate(board):
        newBoard.append([])
        for rindex, cell in enumerate(col):
            newVal = newCell(board, cindex, rindex)
            newBoard[cindex].append(newVal)
            print('newVal: ()()()',cindex, rindex, newVal)
    return newBoard

def test_board():
    board = [
        [0,1,0,0],
        [0,1,0,1],
        [0,1,0,0]
    ]
    newBoard = [
        [0,0,0],
        [1,1,1],
        [0,0,0]
    ]
    assert changeBoard(board) == newBoard
