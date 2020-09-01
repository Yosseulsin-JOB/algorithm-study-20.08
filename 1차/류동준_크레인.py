def get_doll(board,moves):
    hash = {mov-1 :0 for mov in moves}
    for move in moves:
        for row in range(hash[move-1],len(board)):
            if board[row][move-1] != 0:
                hash[move-1] = row +1
                yield board[row][move-1] 
                break
        

def solution(board,moves):
    answer = 0
    stack = []
    for doll in get_doll(board,moves):
        if stack and stack[-1] == doll:
            stack.pop()
            answer = answer + 2
        else:
            stack.append(doll)
    return answer

def solution1(board, moves):
    answer = 0
    stack = []
    hash = {mov-1 :0 for mov in moves}
    for move in moves:
        for row in range(hash[move-1],len(board)):
            if board[row][move-1] != 0:
                doll = board[row][move-1] 
                hash[move-1] = row + 1
                if stack and stack[-1] == doll:
                    stack.pop()
                    answer = answer + 2
                    break
                else:
                    stack.append(doll)
                    break
    return answer