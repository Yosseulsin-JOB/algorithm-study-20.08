# 20:55 ~ 21:03

def createWay(arr):
    def generator():
        i = 0
        while 1:
            yield arr[i%len(arr)]
            i = i + 1
    return generator()

def solution(answers):
    students=[
        createWay([1, 2, 3, 4, 5]),
        createWay([2, 1, 2, 3, 2, 4, 2, 5]),
        createWay([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]),
    ]
    result = [0, 0, 0]
    for answer in answers:
        for num in range(0, 3):
            student = students[num]
            if next(student) == answer:
                result[num] = result[num] + 1
    max_score = max(result)
    answer = []
    for num in range(0, 3):
        student_score = result[num]
        if max_score == student_score:
            answer.append(num + 1)
    
    return answer