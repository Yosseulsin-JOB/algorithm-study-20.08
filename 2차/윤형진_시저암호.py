def solution(s, n):
    answer = ''
    for i in s :
        if i != " " :
            if (ord(i) + n > 90 and ord(i) + n < 97) or (ord(i) + n > 122) : #대문자에서 Z를 초과한 경우
                answer = answer + (chr(ord(i) + n - 26))
            else :
                answer = answer + (chr(ord(i) + n))
        else :
            answer = answer + " "
    return answer



