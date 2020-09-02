import collections

def solution(participant, completion):

    answer = '' 
    a = collections.Counter(participant)
    b = collections.Counter(completion)
 
    answer = a-b

    return list(answer)[0]