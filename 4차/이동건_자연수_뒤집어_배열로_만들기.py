# 11:33 ~ 11:35

def solution(n):
    return [int(str(n)[num]) for num in range(len(str(n)) - 1, -1, -1)]