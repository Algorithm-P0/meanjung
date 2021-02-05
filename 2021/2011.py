import sys
code = sys.stdin.readline().strip()
if code[0]=="0":
    print(0)
    sys.exit()
N = len(code)
dp = [0]*(N+1)
dp[0]=1
dp[1]=1
for i in range(2, N+1):
    if int(code[i-1])>0:
        dp[i]=dp[i-1]
    if 10<=int(code[i-2:i])<=26:
        dp[i]=(dp[i]+dp[i-2])%1000000
print(dp[N]%1000000)