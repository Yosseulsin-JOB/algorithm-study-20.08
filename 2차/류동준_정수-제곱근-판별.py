def check(n):
    value = pow(n,0.5)
    if int(value) == value:
        return pow(value+1,2)
    else:
        return -1
def solution(n):
    value = check(n)
    return value