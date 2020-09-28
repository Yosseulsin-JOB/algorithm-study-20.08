def solution(s):
    s = s.split(' ')
    for i,data in enumerate(s):
        word = ''
        for j in range(len(data)):
            syntax = ''
            if j % 2 == 0:
                syntax = data[j].upper()
            else:
                syntax = data[j].lower()
            word += syntax
        s[i] = word
    answer = ' '.join(s)
    return answer