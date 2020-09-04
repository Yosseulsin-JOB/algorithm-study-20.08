def solution(board, moves):
    stack = []
    point = 0
    for i in moves : # 크레인의 동선, 단 좌표로 쓰니까 1 빼야함, x좌표라 생각
        for j in range(len(board)) : # 맨 위부터 아래로 내려옴, y좌표라 생각
                if board[j][i - 1] != 0 :
                    stack.append(board[j][i - 1])
                    board[j][i - 1] = 0
                    if len(stack) >= 2 :
                        if stack[len(stack) - 1] == stack[len(stack) - 2] :
                            del stack[len(stack) - 1]
                            del stack[len(stack) - 1]
                            point = point + 2
                    break
    return point