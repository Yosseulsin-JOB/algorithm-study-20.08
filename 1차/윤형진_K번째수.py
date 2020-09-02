import copy

def solution(array, commands):
    answer = []
    
    for command in commands:
        copied_array = copy.copy(array)
        copied_array = copied_array[command[0] - 1:command[1]]
        copied_array.sort()
        answer.append(copied_array[command[2] - 1])
            
    return answer
    