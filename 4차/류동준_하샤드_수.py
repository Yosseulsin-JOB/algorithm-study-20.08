def solution(x):
    # answer = list(map(lambda x :int(x),str(x)))
    answer = list(map(int,str(x)))
    result = sum(answer)
  
    return True if x%result == 0 else False