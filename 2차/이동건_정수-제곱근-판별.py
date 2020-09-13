# 22:31 ~ 22:35

def solution(n):
    n_pow = n ** 0.5
    return (int(n_pow)+1)**2 if n_pow % 1 == 0 else -1