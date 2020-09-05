# 22:01 ~ 22:06

def find_num(ori):
    def find(command):
        start, end, idx = command
        temp = ori[start - 1: end]
        temp.sort()
        return temp[idx - 1]
    return find

def solution(array, commands):
    return list(map(find_num(array), commands))