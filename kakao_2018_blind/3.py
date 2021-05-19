from collections import deque

def solution(n, t, m, timetable):
    # n : 셔틀 운행 횟수
    # t : 셔틀 운행 간격
    # m : 한 셔틀에 탈 수 있는 최대 크루 수
    # timetable : 크루들이 도착하는 타임테이블
    lst = []
    for time in timetable:
        hour, minute = time.split(':')
        newTime = int(hour)*60 + int(minute)
        lst.append(newTime)
    lst.sort()
    timeList = deque(lst)

    busTime = [9*60 + t*i for i in range(n)]

    for i in range(n-1):
        bus = busTime[i]
        for j in range(m):
            if timeList[j] > bus:
                break
            timeList.popleft()

    bus = busTime[-1]
    lastPeople = []
    for i in range(m):
        if i < len(timeList):
            if timeList[i] <= bus:
                lastPeople.append(timeList[i])
    if len(lastPeople) < m:
        resHour = bus//60
        resMin = bus%60
    else:
        resHour = (lastPeople[-1] - 1)//60
        resMin = (lastPeople[-1] - 1)%60
    hour = str(resHour)
    min = str(resMin)
    if 0<=resHour<=9:
        hour = "0"+str(resHour)
    if 0<=resMin<=9:
        min = "0"+str(resMin)
    return hour+":"+min


print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))