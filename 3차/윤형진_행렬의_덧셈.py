def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)) :
        tmp = []
        for list_elem in range(len(arr1[i])) :
            tmp.append(arr1[i][list_elem] + arr2[i][list_elem])
            
        answer.append(tmp)

            
    return answer