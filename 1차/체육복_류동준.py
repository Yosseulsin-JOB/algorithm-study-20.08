def add_front_or_behind(los,students):
    if los -1 in students and students[los-1] == 2:
        students[los] +=1
        students[los-1] -=1
    elif los +1 in students and students[los+1] == 2:
        students[los] += 1
        students[los+1] -= 1
    return students

def solution(n, lost, reserve):
    students = {i+1:1 for i in range(n)}
    
    for num in reserve:
        students[num] += 1
    
    for los in lost:
        students[los] -=1
        
    for los in lost:
        if students[los] ==  0:
            students = add_front_or_behind(los,students)
            
    for num in students.keys():
        if students[num] == 0:
            n -=1
            
    return n