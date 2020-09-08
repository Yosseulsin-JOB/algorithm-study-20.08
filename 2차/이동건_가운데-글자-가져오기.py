# 22:03 ~ 22:09
def solution(s):
    middle = int(len(s)/2)
    if len(s)%2 == 1:
        return s[middle]
    return s[middle - 1: middle + 1]