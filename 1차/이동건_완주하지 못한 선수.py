# 20:12 ~ 20:40 (28분)

def toCntDict(arr):
    result = {}
    for data in arr:
        if data not in result:
            result.update({data:0})
        result[data]=result[data] + 1
    return result

def solution(participant, completion):
    dict_participant = toCntDict(participant)
    for key in completion:
        dict_participant[key] = dict_participant[key] - 1
    for key in dict_participant.keys():
        if dict_participant[key] == 0:
            continue
        return key
    return None # 정상적인 데이터라면 이 부분은 무시됩니다.
    