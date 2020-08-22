# nqueen
"""
import sys
N=int(sys.stdin.readline())
ans=0

a=[False]*N
b=[False]*(2*N-1)
c=[False]*(2*N-1)

def solve_dfs(i):
    global ans
    if i==N:
        ans+=1
        return
    for j in range(N):
        if (a[j]==False and b[i+j]==False and c[i-j+N-1]==False):
            a[j]=True
            b[i+j]=True
            c[i-j+N-1]=True
            solve_dfs(i+1)
            a[j]=False
            b[i+j]=False
            c[i-j+N-1]=False
solve_dfs(0)
print(ans)
"""
def promising(i):
    for j in range(0,i):
        # 새로운 퀸과 기존의 퀸이 같은 행에 있거나 대각선에 있을 경우
        if row[j] == row[i] or abs(row[j]-row[i]) == (i-j):
            return False
    return True

def N_queen(i):
    global result
    if i == N:
        result += 1
    else:
        for j in range(N):
            row[i] = j
            if promising(i):
                N_queen(i+1)
import sys
N = int(sys.stdin.readline())
row = [0]*15
result = 0
N_queen(0)
print(result)