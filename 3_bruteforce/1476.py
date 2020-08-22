import sys
E,S,M,cnt =1,1,1,1

i_E , i_S , i_M = map(int,sys.stdin.readline().split())

while(True):
    if i_E==E and i_S==S and i_M==M :
        break
    E+=1 ; S+=1 ; M+=1; cnt+=1
    if E>=16 : E-=15
    if S>=29 : S-=28
    if M>=20 : M-=19

print(cnt)

"""
E, S, M = map(int, sys.stdin.readline().split())

ans = 1
while True:
    if ans%15 == E and ans%28 == S and ans%19 == M:
        print(ans)
        break
    ans+=1
"""