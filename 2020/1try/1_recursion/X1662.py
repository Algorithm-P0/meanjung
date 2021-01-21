def bracketCheck(strr, start): # 닫은 괄호의 인덱스 반환
    count1=0
    count2=0
    for i in range(start, len(strr)):
        if strr[i] == '(':
            count1+=1
        elif strr[i]==')':
            count2+=1
            if count1<count2:
                break
        else: continue
    return i

def solve(strr):
    if '(' not in strr:
        return len(strr)
    K=strr.index('(')-1
    K2 = bracketCheck(strr, K+2)
    cut = K # 개수
    strrr = strr[K+2:K2]
    cut += int(strr[K])*solve(strrr)
    if K2+1<len(strr):
        cut += len(strr)-(K2+1)
    return cut

import sys

strr = str(sys.stdin.readline().strip())
print(solve(strr))

"""
왜 틀렸는지 당최 모르겠는 사정...
"""