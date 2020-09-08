def solution(a, b):
    answer = ''
    year_dict = {1 : 31, 2 : 29, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31 }
    day_counter = 0
    day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    
    for i in year_dict.keys() :
        
        if i is not a :
            day_counter = day_counter + year_dict[i]
            
        else :
            day_counter = day_counter + b
            break
            
    day_counter = (day_counter + 4) % 7 
    
    if day_counter >= 7 :
        day_counter = day_counter % 7
        
    answer = day[day_counter]
            
    return answer