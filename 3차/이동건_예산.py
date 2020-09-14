# 23:20 ~ 23:24
def solution(d, budget):
    d.sort()
    buy = 0
    cnt = 0
    for request in d:
        if buy + request > budget:
            break
        buy += request
        cnt += 1
    return cnt