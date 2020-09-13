def solution(n):
    answer = 0
    
    if n == 0 :
        pass
    elif n == 1 :
        answer = 1
    else :     
        for i in range(2, n) :
            if n % i == 0 :
                answer = answer + i

        answer = answer + 1 + n
    return answer