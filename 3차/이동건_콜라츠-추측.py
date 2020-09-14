# 23:37 ~ 23:42

def collatz(n):
    if n % 2 == 0:
        return n / 2
    return n * 3 + 1

def solution(num):
    if num == 1:
        return 0
    
    n = num
    for i in range(1, 502):
        n = collatz(n)
        if n == 1:
            break
    if i == 501:
        return -1
    return i