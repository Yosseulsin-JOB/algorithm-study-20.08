# 23:00 ~ 23:22
def get_measure(n, m, stack=[]):
    min_num = min([n, m])
    for i in range(2, min_num + 1):
        if n % i == 0 and m % i == 0:
            stack.append(i)
            n = (n - (n % i))/i
            m = (m - (m % i))/i
            return get_measure(int(n),int(m), stack)
    return stack , [int(n),int(m)]

def mul(data):
    result = 1
    for num in data:
        result *= num
    return result

def solution(n, m):
    min_num, max_num = get_measure(n,m,[])
    return [mul(min_num), mul(max_num + min_num)]