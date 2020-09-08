# 22:03 ~ 22:09
def solution(s):
    middle = int(len(s)/2)
    return s[middle - 1: middle + 1] if len(s)%2 == 0 else s[middle]