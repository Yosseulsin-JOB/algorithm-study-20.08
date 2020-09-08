# 22:14 ~ 22:27

def addChar(char, n):
    if char == ' ':
        return ' '
    chat_ascii = ord(char)
    next_ascii = chat_ascii + n
    if chat_ascii <= 90:
        return chr(next_ascii - (26 if next_ascii > 90 else 0))
    return chr(next_ascii - (26 if next_ascii > 122 else 0))

def solution(s, n):
    return "".join([addChar(char, n) for char in s]) 