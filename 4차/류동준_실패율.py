# def solution(N, stages):
#     person = len(stages)
#     answer = []
#     for n in range(1,N+1):
#         count = 0
#         for stage in stages:
#             if n == stage:
#                 count +=1
#         if person == 0:
#             answer.append(0)
#         else:
#             answer.append(count/person)
#         person -= count
    
#     tmp = {i+1:value for i,value in enumerate(answer)}
#     tmp = sorted(tmp.items(),key = lambda x: x[1],reverse=True)
#     return list(map(lambda x :x[0],tmp))


def solution(N,stages):
    tmp = {}
    persons = len(stages)
    for n in range(1,N+1):
        count = len(list(filter(lambda x: x==n, stages)))
        if persons == 0:
            tmp[n] = 0
            # answer.append(0)
        else:
            tmp[n] = count/persons
            # answer.append(count/persons)
        persons = persons - count if count is not None  else persons
    # tmp = {i+1:value for i,value in enumerate(answer)}
    tmp = sorted(tmp.items(),key = lambda x: x[1],reverse=True)
    return list(map(lambda x :x[0],tmp))