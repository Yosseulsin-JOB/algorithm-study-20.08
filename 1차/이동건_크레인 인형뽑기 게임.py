# 23:33 ~ 23:46 (13분)

def get_non_zero_row(board, col):
    for row in range(0, len(board)):
        if board[row][col] != 0:
            return row
    return None

def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        row = get_non_zero_row(board, move - 1)
        if row is None:
            continue
        doll = board[row][move - 1]
        if stack and stack[-1] == doll:
            del stack[-1]
            answer=answer + 2
        else:
            stack.append(doll)
        board[row][move - 1] = 0
    return answer