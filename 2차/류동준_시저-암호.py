import string
from collections import OrderedDict

def solution(s, n):
    alphabets = OrderedDict(zip(string.ascii_lowercase,range(1,27)))
    result = []
    for c in s:
        if c.isalpha():
            index = (alphabets[c.lower()] + n) % 26
            if index == 0:
                index = 26
            for key,value in alphabets.items():
                if value == index:
                    tmp = key
            if c.isupper():
                tmp = tmp.upper()
            elif c.islower():
                tmp = tmp.lower()
            result.append(tmp)
        else:
            result.append(' ')
    return "".join(result)
