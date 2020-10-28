import sys
def canReadWord():
    count = 0
    for i in range(N):
        isRead = True
        w = words[i]
        for j in w:
            if learn[ord(j)-ord('a')]==False:
                isRead=False
                break
        if isRead==True:
            count+=1
    return count

def dfs(idx, cnt):
    global ans
    if cnt==K:
        tempAns = canReadWord()
        ans = max(ans, tempAns)
        return
    for i in range(idx, 26):
        if learn[i]==True:
            continue
        learn[i]=True
        dfs(i, cnt+1)
        learn[i]=False

N, K = map(int, sys.stdin.readline().split())

if K<5:
    print(0)
    sys.exit()
if K==26:
    print(N)
    sys.exit()

words = []
for _ in range(N):
    words.append(sys.stdin.readline().strip())
learn = [False]*26
for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c)-ord('a')]=True
K = K - 5
ans = 0
dfs(0,0)
print(ans)