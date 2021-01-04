import sys
N = int(sys.stdin.readline())
word1 = [0]*26
for w in sys.stdin.readline().strip():
    word1[ord(w)-ord('A')]+=1
res=0
for _ in range(N-1):
    plus, minus = 0, 0
    word2 = [0]*26
    for w in sys.stdin.readline().strip():
        word2[ord(w)-ord('A')]+=1
    for i in range(26):
        if word2[i]>word1[i]:
            plus+=(word2[i]-word1[i])
        else:
            minus+=(word1[i]-word2[i])
    if plus<2 and minus<2:
        res+=1
print(res)