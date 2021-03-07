import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    importance = list(map(int, sys.stdin.readline().split()))
    have_to_find = [0]*n
    have_to_find[m]=1
    cnt = 0
    while True:
        if importance[0]==max(importance):
            cnt+=1
            if have_to_find[0]==1:
                print(cnt)
                break
            else:
                del importance[0]
                del have_to_find[0]
        else:
            importance.append(importance[0])
            del importance[0]
            have_to_find.append(have_to_find[0])
            del have_to_find[0]
