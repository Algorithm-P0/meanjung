import sys
L, C = map(int, sys.stdin.readline().split())
chars = list(sys.stdin.readline().strip().split())
chars.sort()
# vowel : 모음
# consonant : 자음
def solve(lst, vowel, consonant, idx):
    if len(lst)==L and vowel>=1 and consonant>=2:
        print(''.join(lst))
        return
    for i in range(idx+1, C):
        if chars[i]=='a' or chars[i]=='e' or chars[i]=='i' or chars[i]=='o' or chars[i]=='u':
            lst.append(chars[i])
            solve(lst, vowel+1, consonant, i)
            lst.pop()
        else:
            lst.append(chars[i])
            solve(lst, vowel, consonant+1, i)
            lst.pop()

for i in range(C):
    if chars[i]=='a' or chars[i]=='e' or chars[i]=='i' or chars[i]=='o' or chars[i]=='u':
        solve([chars[i]], 1, 0, i)
    else:
        solve([chars[i]], 0, 1, i)