def solution(s):
    if len(s) % 2 == 0:
        n = int(len(s) / 2)
        return s[n-1:n+1]
    else:
        n = int(len(s) / 2)
        return s[n]