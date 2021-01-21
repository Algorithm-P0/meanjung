import sys
card = sys.stdin.readline().strip()
N = len(card)
card = '0'+card
if N==1:
    print(1)
else:
    dp = [0]*(N+1)
    # dp[i] : index i까지의 가능한 경우의 수
    dp[1]=1
    if 10<=int(card[1:3])<=34 and card[2]!='0':
        dp[2]=2
    else:
        dp[2]=1
    for i in range(3, N+1):
        if 10<=int(card[i-1]+card[i])<=34:
            dp[i]+=dp[i-2]
        if card[i]!='0':
            dp[i]+=dp[i-1]
print(dp[-1])
