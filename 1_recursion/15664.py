# 중복 조합
import sys
N, M =map(int, sys.stdin.readline().split())
nList=list(map(int, sys.stdin.readline().split()))
nList.sort()
ans=[]
def func(depth, idx, lst):
    if depth==M:
        res=' '.join(map(str, lst))
        if res not in ans:
            ans.append(res)
        return
    if idx<N:
        lst.append(nList[idx])
        func(depth+1, idx+1, lst)
        lst.pop()
        func(depth, idx+1, lst)
func(0,0,[])
for a in ans:
    print(a)