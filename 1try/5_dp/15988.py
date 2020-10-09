import sys
T = int(sys.stdin.readline())
n=[]
for _ in range(T):
    n.append(int(sys.stdin.readline()))
ans=[0,1,2,4]
for i in range(4, max(n)+1):
    ans.append((ans[i-1]+ans[i-2]+ans[i-3])%1000000009)
for k in n:
    print(ans[k]%1000000009)