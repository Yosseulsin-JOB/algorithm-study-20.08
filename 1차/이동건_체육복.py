# 21:35 ~ 21:53

def to_dict(num):
    data = {}
    for i in range(1, num + 1):
        data.update({i:0})
    return data

def solution(n, lost, reserve):
    students = to_dict(n)
    
    for reserve_student in reserve:
        students[reserve_student] = students[reserve_student] + 1
    for lost_student in lost:
        students[lost_student] = students[lost_student] - 1
    for lost_student in lost:
        if students[lost_student] == -1:
            if lost_student - 1 in students and students[lost_student - 1] == 1:
                students[lost_student - 1] = students[lost_student - 1] - 1
                students[lost_student] = students[lost_student] + 1
            elif lost_student + 1 in students and  students[lost_student + 1] == 1:
                students[lost_student + 1] = students[lost_student + 1] - 1
                students[lost_student] = students[lost_student] + 1
                
    for key in students.keys():
        if students[key] == -1:
            n = n - 1

    return n