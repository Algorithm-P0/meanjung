import sys
N = int(sys.stdin.readline())
innings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
order = [0]*9
visited = [0]*9
order[3] = 0
visited[3] = 1
# 1번 선수는 정해져있다.
ans = 0
def dfs(cnt):
    global ans
    if cnt==9:
        start, score = 0, 0
        for inning in innings:
            out, b1, b2, b3 = 0, 0, 0, 0
            while out<=2:
                p = order[start]
                if inning[p]==0:
                    out+=1
                elif inning[p]==1:
                    score += b3
                    b1, b2, b3 = 1, b1, b2
                elif inning[p]==2:
                    score += b2 + b3
                    b1, b2, b3 = 0, 1, b1
                elif inning[p]==3:
                    score += b1 + b2 + b3
                    b1, b2, b3 = 0, 0, 1
                else:#홈런
                    score += b1 + b2 + b3 + 1
                    b1, b2, b3 = 0, 0, 0
                start += 1
                start = start % 9
        ans = max(ans, score)
        return 
    # cnt가 9가 되기 전, 순열 구하기
    for i in range(9):
        if visited[i]==0:
            visited[i] = 1
            order[i] = cnt
            dfs(cnt+1)
            visited[i] = 0
            order[i] = 0
dfs(1)
print(ans)