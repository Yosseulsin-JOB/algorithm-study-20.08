def gcd(a,b):
    mod = a % b;
    while(mod > 0):
        a = b
        b = mod
        mod = a % b  
    return b


def solution(n, m):
    value = gcd(n,m)
    return [value, n *m / value]