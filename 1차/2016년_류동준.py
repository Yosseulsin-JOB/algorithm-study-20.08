import datetime

def solution(a, b):
    answer = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    dt = datetime.datetime(2016,a,b).weekday()
    return answer[dt]