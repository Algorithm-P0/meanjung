import sys
T=int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    Nmap=[list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    Nmap[0][1]+=Nmap[1][0]
    Nmap[1][1]+=Nmap[0][0]
    for i in range(2, n):
        Nmap[0][i]+=max(Nmap[1][i-1], Nmap[1][i-2])
        Nmap[1][i]+=max(Nmap[0][i-1], Nmap[0][i-2])
    print(max(Nmap[0][n-1], Nmap[1][n-1]))