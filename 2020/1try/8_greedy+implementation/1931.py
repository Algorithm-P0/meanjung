import sys
N = int(sys.stdin.readline())
order=[]
for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    order.append([e,s])
order.sort()
earlist = 0
selected = 0
for i in range(len(order)):
    meetingEnd, meetingBegin = order[i]
    if earlist<=meetingBegin:
        earlist = meetingEnd
        selected+=1
print(selected)