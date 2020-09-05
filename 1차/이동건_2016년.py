# 22:12 ~ 22:17

def solution(a, b):
    month = [0, 31,29,31,30,31,30,31,31,30,31,30,31]
    days = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    return days[(sum(month[0:a]) + b)%7]