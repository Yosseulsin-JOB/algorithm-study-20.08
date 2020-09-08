def a1():
    count = 0
    while True:
        count +=1
        yield count
        if count == 5:
            count = 0

def a2():
    count = 0
    tmp = 0
    a = [1,3,4,5]
    while True:
        if count %2 == 0:
            yield 2 
        else:
            try:
                yield a[tmp]
                tmp +=1
            except:
                tmp = 0
                yield a[tmp]
                tmp +=1
        count += 1

def a3():
    tmp = [3,3,1,1,2,2,4,4,5,5]
    count = 0
    while True:
        if count == 10:
            count = 0
            yield tmp[count]
        else: 
            yield tmp[count]
        count +=1
        

def solution(answers):
    a = a1()
    b = a2()
    c = a3()
    tmp = {'1': 0 ,'2': 0 ,'3':0}
    for data in answers:
        if next(a) == data:
            tmp['1'] +=1
        if next(b) == data:
            tmp['2'] +=1
        if next(c) == data:
            tmp['3'] +=1
    answer = []
    maxvalue = max(tmp.values())
    for k,v in tmp.items():
        if v == maxvalue:
            answer.append(int(k))
    # answers = sorted(tmp.items(),key =(lambda x:x[1]),reverse=True)
    # maxvalue = max([v for _,v in answers])
    # answer = [int(k) for k,v in answers if v == maxvalue]
              
    return answer