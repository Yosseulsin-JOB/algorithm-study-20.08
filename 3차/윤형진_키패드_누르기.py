def get_distance(hand, number):
    location = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                '4': (1, 0), '5': (1, 1), '6': (1, 2),
                '7': (2, 0), '8': (2, 1), '9': (2, 2),
                '*': (3, 0), '0': (3, 1), '#': (3, 2)}
    number = str(number)
    
    x_hand, y_hand = location[hand]
    x_number, y_number = location[number]
    
    return abs(x_hand - x_number) + abs(y_hand - y_number)

def solution(numbers, hand):
    answer = ''
    left, right = '*', '#'
    if hand == 'right' :
        hand = 'R' 
    else :
        hand = 'L'
    
    left_numbers = [1,4,7]
    right_numbers = [3,6,9]
    center_numbers = [2,5,8,0]
    
    for number in numbers:
        if number in left_numbers:
            answer += 'L'
            left = str(number)
            continue
        elif number in right_numbers:
            answer += 'R'
            right = str(number)
            continue
        elif number in center_numbers:
            distance1 = get_distance(left, number)
            distance2 = get_distance(right, number)
            if distance1 > distance2:
                answer += 'R'
                right = str(number)
            if distance1 < distance2:
                answer += 'L'
                left = str(number)
            if distance1 == distance2:
                answer += hand
                if hand == 'R':
                    right = str(number)
                if hand == 'L':
                    left = str(number)
    return answer