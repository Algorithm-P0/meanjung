# 실수값이라서 풀이가 애매하다면 정수로 값을 변환하라!!

def checktr(time, li):
     c = 0
     start = time
     end = time+1000
     for i in li:
         if i[1]>=start and i[0]<end:
             c += 1
     return c

def solution(lines):
    li = []
    r = 1
    for line in lines:
        d, t, s = line.split()
        t = t.split(':')
        s = float(s.replace('s', ''))*1000
        end = (int(t[0])*3600 + int(t[1])*60 + float(t[2]))*1000
        start = end - s + 1
        li.append([start, end])
    for i in li:
        r = max(r, checktr(i[0], li), checktr(i[1], li))
    return r


solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
])