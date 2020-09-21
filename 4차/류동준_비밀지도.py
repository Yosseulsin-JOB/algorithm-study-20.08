def convert(x,n):
    tmp = ''
    for c in x[2:]:
        if c == '1':
            tmp +='#'
        else:
            tmp += ' '
    if len(tmp) < n:
        blank = [' '] * (n-len(tmp))
        tmp = ''.join(blank) + tmp
    return tmp
def solution(n, arr1, arr2):
    tmp = list(map(lambda x,y: bin(x|y),arr1,arr2))
    answer = list(map(lambda x :convert(x,n),tmp))
    return answer