import math

def solution(n):
    answer = 0
    k = math.sqrt(n)
    k = str(k)

    if len(k[k.find("."):]) == 2 and int(k[k.find(".") + 1]) == 0 :
        answer = (int(float(k)) + 1) * (int(float(k)) + 1)
    else :
        answer = -1
    return answer