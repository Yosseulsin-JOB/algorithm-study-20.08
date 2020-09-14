# 23:48 ~ 00:30

def to_len(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x2-x1) + abs(y2-y1) # 상하좌우만 가능하기 때문

def create_dict():
    return {
        1 : [0, 0],
        2 : [1, 0],
        3 : [2, 0],
        4 : [0, 1],
        5 : [1, 1],
        6 : [2, 1],
        7 : [0, 2],
        8 : [1, 2],
        9 : [2, 2],
        '*' : [0, 3],
        0 : [1, 3],
        '#' : [2, 3],
    }

def solution(numbers, hand):
    phone = create_dict()
    l = [1,4,7]
    r = [3,6,9]
    L = phone['*']
    R = phone['#']
    
    stack = ""
    for number in numbers:
        if number in l:
            L = phone[number]
            stack+='L'
            continue
        
        if number in r:
            R = phone[number]
            stack+='R'
            continue
        
        len_l = to_len(L, phone[number])
        len_r = to_len(R, phone[number])
        
        if len_l < len_r:
            L = phone[number]
            stack+='L'
            continue
        
        if len_r < len_l:
            R = phone[number]
            stack+='R'
            continue
        
        if hand[0] == 'r':
            R = phone[number]
            stack+='R'
            continue
            
        L = phone[number]
        stack+='L'
    
    return stack