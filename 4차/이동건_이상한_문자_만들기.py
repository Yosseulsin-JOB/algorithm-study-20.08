# 11:38 ~ 11:51

def solution(s):
    return " ".join(map(lambda w:"".join([value.upper() if idx % 2 == 0 else value.lower() for idx, value in enumerate(w)]), s.split(" ")))