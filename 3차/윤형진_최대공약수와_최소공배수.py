from math import gcd
def solution(n, m):
    answer = []

    # Euclidean Algorithm ==> gcd module
    answer.append(gcd(n,m))
    answer.append(n*m // gcd(n,m))    
    
    return answer