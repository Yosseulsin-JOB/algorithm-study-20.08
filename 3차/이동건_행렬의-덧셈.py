# 23:24 ~ 23:31
def sum_row(row1, row2):
    row = []
    for idx, value in enumerate(row1):
        row.append(value + row2[idx])
    return row

def solution(arr1, arr2):
    arr = []
    for idx, row in enumerate(arr1):
        arr.append(sum_row(row, arr2[idx]))
    return arr