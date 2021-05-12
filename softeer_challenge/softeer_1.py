import sys
N, K = map(int, sys.stdin.readline().split())
string = sys.stdin.readline().strip()
# p로봇 h부품
# HHPHPPHHPPHPPPHPHPHP
cnt = 0
visited = [False]*len(string)
for i in range(N):
    if string[i] == 'H':#부품이라면
        visited[i] = True
        for j in range(i-K, i+K+1):
            if 0 <= j < N:
                if string[j] == 'P' and visited[j] == False:
                    visited[j] = True
                    cnt += 1
                    break
print(cnt)



