def solution(s):
    answer = ''
    word_len = len(s)
    
    if word_len % 2 == 0 :
        answer = s[(word_len // 2 - 1) :(word_len // 2 + 1)]
    else :
        answer = s[word_len // 2]
    
    return answer