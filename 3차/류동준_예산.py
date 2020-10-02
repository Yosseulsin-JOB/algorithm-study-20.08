def solution(d, budget):
    answer = 0
    # d가 가장 작은 값을 순서대로 가지게 끔 함 
    # 혹은 d의 value를 pop 할때 d.pop(d.index(min(d))) 도 가능하기는함.
    d.sort()
    while (budget):
        # 모든 d 를 pop 하고 budget이 여유있을때도 있음 test case를 통해 확인함.
        if d:
            min_value = d.pop(0)
            if min_value <= budget:
                budget -= min_value
                answer += 1
            else:
                break
        else:
            break
    return answer