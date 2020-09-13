def solution(n):
    answer = 0
    
    if n == 2:
        answer = 1
    else :
        answer = 1
        for i in range(3, n + 1) :
            is_prime_num = True
            for j in range(2, i) :
                if i%j == 0 :
                    is_prime_num = False
                    break
                    
            if is_prime_num == True :
                answer = answer + 1
        
    return answer



