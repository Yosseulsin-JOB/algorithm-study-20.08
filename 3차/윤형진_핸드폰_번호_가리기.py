def solution(phone_number):
    answer = ''
    
    a = len(phone_number)
    for i in range(a - 4) :
        answer += "*"
    for i in range(4, 0, -1) :
        answer += phone_number[a - i]

    return answer