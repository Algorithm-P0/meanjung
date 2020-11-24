import sys
N = int(sys.stdin.readline())
negative=[]
positive=[]
ans=0
for _ in range(N):
    n = int(sys.stdin.readline())
    if n<=0:
        negative.append(n)
    elif n == 1:
        ans+=1
    elif n>1:
        positive.append(n)
negative.sort()
positive.sort(reverse=True)
for i in range(0, len(negative), 2):
    if i+1<len(negative):
        ans+=negative[i]*negative[i+1]
    else:
        ans+=negative[i]
for i in range(0, len(positive), 2):
    if i+1<len(positive):
        ans+=positive[i]*positive[i+1]
    else:
        ans+=positive[i]
print(ans)