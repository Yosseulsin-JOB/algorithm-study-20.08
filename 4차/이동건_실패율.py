
# 14:23 ~ 15:03
from functools import reduce
from collections import Counter 

def solution(N, stages):
    result = {0:[]}
    left = len(stages)
    data = dict(Counter(stages))
    
    for i in range(1, N + 1):
        if i not in data.keys():
            result[0].append(i)
            continue
        
        fail = data[i] / left
        left -= data[i]
        
        if fail not in result.keys():    
            result[fail]=[]
        result[fail].append(i)
        
    keys = list(result.keys())
    keys.sort(reverse=True)

    return reduce(lambda answer, key:answer+result[key], keys, [])