# 12:06 ~ 12:45
def solution(dartResult):
    nums = ['1','2','3','4','5','6','7','8',"9",'0']
    squared = {'S': 1, 'D': 2, 'T':3}
    stack = []
    for dart in dartResult:
        if dart in nums:
            num = int(dart)
            if(stack and num == 0 and stack[-1]==1):
                stack.pop()
                num = 10
            stack.append(num)
        elif dart in squared.keys():
            stack.append(stack.pop() ** squared[dart])
        elif dart == '#':
            stack.append(stack.pop() * -1)
        elif dart == '*':
            stack[-1] *= 2
            if len(stack) > 1:
                stack[-2] *= 2
    return sum(stack)