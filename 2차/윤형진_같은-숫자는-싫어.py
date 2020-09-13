def solution(arr):
    answer = []
    isBreaked = False
    comp_idx = 1
    idx = 0
    
    while True : 
        if idx + 1 >= len(arr):
            break
        
        if arr[idx] == arr[idx + 1] :
            del arr[idx + 1]
            
        else :
            idx = idx + 1


    return arr

    