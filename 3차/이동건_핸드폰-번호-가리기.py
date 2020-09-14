# 23:33 ~ 23:36

def create_star(num):
    s = ""
    for i in range(num):
        s += "*"
    return s

def solution(phone_number):
    num = len(phone_number) - 4
    return create_star(num) + phone_number[num:]