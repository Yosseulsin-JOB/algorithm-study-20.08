def solution(n, lost, reserve):
    answer = 0
    student_list = [0 for i in range(n)]
    
    # 여분 보유 학생에 대해 1로 설정, 없는 학생은 -1, 일반 학생은 0
    # 여분의 체육복을 빌려주면 1을 0으로 바꿈
    for i in reserve : 
        student_list[i - 1] = 1 
        
    for i in lost :
        student_list[i - 1] = student_list[i - 1] - 1 #여분을 가져온 학생도 도난당할 수 있다는 점

    for i in range(n) : 
        if student_list[i] == -1 :
            if i > 0 and student_list[i - 1] == 1 :
                student_list[i - 1] = 0
                student_list[i] = 0
            elif  i < n - 1 and student_list[i + 1] == 1 : 
                student_list[i + 1] = 0
                student_list[i] = 0
    

    for i in student_list :
        if i >= 0 :
            answer = answer + 1
    
    return answer
