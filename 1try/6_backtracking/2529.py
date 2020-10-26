import sys
k = int(sys.stdin.readline())
operation = sys.stdin.readline().split()
check = [False]*10
mx, mn = "", ""

def possible(i,j,op):
    if op=='<':
        return i<j
    if op=='>':
        return i>j

def solve(cnt, string):
    # 어차피 오름차순으로 탐색하므로
    # 처음 결정된 수가 mn,
    # 마지막으로 나온 수가 mx
    global mx, mn
    if cnt == k+1:
        if len(mn)==0:
            mn = string
        else:
            mx = string
        return

    for i in range(10):
        if check[i]==False:
            if cnt==0 or possible(string[-1], str(i), operation[cnt-1]):
                check[i]=True
                solve(cnt+1, string+str(i))
                check[i]=False
solve(0, "")
print(mx)
print(mn)