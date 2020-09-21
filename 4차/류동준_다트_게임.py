import re

def solution(dartResult):
    dartResult = dartResult.replace('10','a')
    p = re.compile('[\d\w\*\#]')
    result = p.findall(dartResult)
     
    values = []
    for data in result:
        try:
            value = int(data)
            values.append(value)
        except:
            if data == 'a':
                values.append(10)
            if data == 'S':
                values[-1] = pow(values[-1],1)
            elif data == 'D':
                values[-1] = pow(values[-1],2)
            elif data == 'T':
                values[-1] = pow(values[-1],3)
            elif data == '*':
                values[-1] = values[-1] * 2
                if len(values) > 1:
                    values[-2] = values[-2] * 2
            elif data == '#':
                values[-1] = values[-1] * -1   

    return sum(values)