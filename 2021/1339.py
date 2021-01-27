import sys
N = int(sys.stdin.readline())
alph = [0]*26
for _ in range(N):
    word = list(sys.stdin.readline().strip())
    word_len = len(word)
    for i in range(word_len):
        alph[ord(word[i])-ord('A')]+=10**(word_len-1-i)
alph.sort(reverse=True)
ans = 0
i = 9
for j in alph:
    ans += j*i
    i-=1
print(ans)