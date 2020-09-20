# 15:05 ~ 15:18

def to_binary(num, n):
    res = "{0:b}".format(num)
    return "0" * (n - len(res)) + res

def to_map(a, b):
    return "".join(["#" if num == "1" or b[idx] == "1" else " " for idx, num in enumerate(a)])

def solution(n, arr1, arr2):
    return [to_map(to_binary(value, n), to_binary(arr2[idx], n)) for idx, value in enumerate(arr1)]