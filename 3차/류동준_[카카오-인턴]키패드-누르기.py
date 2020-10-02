def caldist(l_hand,r_hand, num,position,hand):
    dist_l = abs(position[num][0] - position[l_hand][0]) + abs(position[num][1] - position[l_hand][1])
    dist_r = abs(position[num][0] - position[r_hand][0]) + abs(position[num][1] - position[r_hand][1])
    if dist_l == dist_r:
        return 'R' if hand =='right' else 'L'
    return 'R' if dist_l > dist_r else 'L'

def solution(numbers, hand):
    position = {
        1: (0,0), 2: (0,1) ,3 :(0,2),
        4: (1,0), 5: (1,1) ,6 :(1,2),
        7: (2,0), 8: (2,1) ,9 : (2,2),
        '*':(3,0), 0:(3,1),'#': (3,2)
    }
    
    left_numbers,right_numbers = set([1,4,7,'*']),set([3,6,9,'#'])
    answer = ''
    l_hand = '*'
    r_hand = '#'
    
    for num in numbers:
        if num in left_numbers:
            answer += 'L'
            l_hand = num
        elif num in right_numbers:
            answer += 'R'
            r_hand = num
        else:
            result = caldist(l_hand,r_hand,num,position,hand)
            if result == 'R':
                r_hand = num
            else:
                l_hand = num
            answer += result
    
    return answer