def solution1(participant, completion):
    result = dict()
    for person in participant:
        try:
            result[person] +=1
        except:
            result[person] = 1
            pass
    for person in completion:
        result[person] -=1

    for k,v in result.items():
        if result[k] != 0:
            answer = k
    return answer
 

from collections import Counter 
  
def solution(participant, completion):
    result = dict(Counter(participant))
    #for person in participant:
    #    try:
    #        result[person] +=1
    #    except:
    #        result[person] = 1
    #        pass
    
    for person in completion:
        result[person] -=1

    for k,v in result.items():
        if result[k] != 0:
            answer = k
    return answer