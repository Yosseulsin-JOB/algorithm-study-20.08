# 22:42 ~ 22:45
def solution(n):
    primes_map = [False,False] + [True]*(n-1)
    primes = 0

    for num in range(2,n+1):
        if primes_map[num]:
            primes += 1
            for disabled_idx in range(2*num, n+1, num):
                primes_map[disabled_idx] = False
    return primes