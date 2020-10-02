import re

def solution(phone_number):
    tmp = list(phone_number)
    tmp[:len(tmp) -4 ] = '*' * (len(tmp) -4) 
    # or 이거 왜 안되는지 모르겠음 9번 케이스가 틀린다
    # data = re.sub('[\s]','*',phone_number,len(phone_number)-4) 일때 9번이 통과는함 근데  re.sub('[\s\d]','*',phone_number,len(phone_number)-4) 일때는 안함 ㅅㅂ
    # data = re.sub('[\d\s]','*',phone_number,len(phone_number)-4)
    # print(data)
    # return data
    return ''.join(tmp)
