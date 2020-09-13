# 22:36 ~ 22:41
def solution(n):
    stack = []
    for num in range(1, n + 1):
        if n%num == 0:
            stack.append(num)
    return sum(stack)