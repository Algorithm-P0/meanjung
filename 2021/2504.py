import sys
from collections import deque
# deque, q를 쓸 필요는 없다.
bracket = list(sys.stdin.readline().strip())
q = deque()
for b in bracket:
    if b=='(' or b=='[':
        q.append(b)
    elif b==')':
        sum = 0
        while q:
            top = q.pop()
            if top=='(':
                if sum == 0:
                    q.append(2)
                else:
                    q.append(2*sum)
                break
            elif top=='[':
                print('0')
                sys.exit()
            else:
                sum+=top
    elif b==']':
        sum = 0
        while q:
            top = q.pop()
            if top=='[':
                if sum==0:
                    q.append(3)
                    break
                else:
                    q.append(3*sum)
                    break
            elif top=='(':
                print('0')
                sys.exit()
            else:
                sum += top
res = 0
for d in q:
    if d=='(' or d=='[':
        print(0)
        sys.exit()
    else:
        res+=d
print(res)