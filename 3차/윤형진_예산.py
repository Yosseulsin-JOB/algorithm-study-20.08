def solution(d, budget):
    answer = 0
    d.sort()
    sorted_d = d 

    for i in sorted_d :
        if budget >= i :
            budget -= i
            answer +=1
        elif budget < i :
            break
        
    return answer