n = int(input('nhap N : '))

def is_valid(board, row, col, n):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False
    return True

def solve(board, row, n, res):
    if row == n:
        res.append(["".join(row) for row in board])
        return
    for col in range(n):
        if is_valid(board, row, col, n):
            board[row][col] = 'Q'
            solve(board, row+1, n, res)
            board[row][col] = '.'

board = [['.' for _ in range(n)] for _ in range(n)]
res = []
solve(board, 0, n, res)
print(res)
