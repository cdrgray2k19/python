board = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]
]

def legal(arr):
    for i in arr:
        for j in i:
            if j != 0:
                if i.count(j) > 1:
                    return False
    for x in range(0, len(arr[0])):
        temp = []
        for y in range(0, len(arr)):
            val = arr[y][x]
            temp.append(val)
            if val != 0:
                if temp.count(val) > 1:
                    return False
    return True

def findEmpty(arr):
    coords = []
    for y in range(0, len(arr)):
        for x in range(0, len(arr[0])):
            if arr[y][x] == 0:
                coords.append([y, x])
    return coords

def solve(i, arr, empty):
    if i == len(empty):
        return True
    else:
        for num in range(1, 10):
            arr[empty[i][0]][empty[i][1]] = num
            if legal(arr):
                if solve(i+1, arr, empty):
                    return True
        arr[empty[i][0]][empty[i][1]] = 0

if legal(board):
    empty = findEmpty(board)
    if solve(0, board, empty):
        print('\nsolution:\n')
        for row in board:
            print(row)
        print('\n')
    else:
        print('there was a problem solving this sudoku board!')
else:
    print('invalid sudoku board given')