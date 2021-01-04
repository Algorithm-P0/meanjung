import sys
N = int(sys.stdin.readline())
cnt = N
for _ in range(N):
    word = sys.stdin.readline().strip()
    exist = []
    i = 0
    while i < len(word):
        if word[i] not in exist:
            k = i+1
            while k<len(word) and word[i]==word[k]:
                k+=1
            exist.append(word[i])
            i = k
        else:
            cnt-=1
            break
print(cnt)