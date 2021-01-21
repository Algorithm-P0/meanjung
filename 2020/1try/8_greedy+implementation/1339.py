import sys
N = int(sys.stdin.readline())
words = [0]*26
for _ in range(N):
    w = sys.stdin.readline().strip()
    for i in range(len(w)):
        words[ord(w[i])-ord('A')]+=10**(len(w)-1-i)
words.sort(reverse=True)
sum=0
for i in range(10):
    if words[i]==0:
        break
    sum+=words[i]*(9-i)
print(sum)