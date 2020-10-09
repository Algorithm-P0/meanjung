import sys
import itertools
L, C = map(int, sys.stdin.readline().split())
chars = list(map(str, sys.stdin.readline().split()))
vowel=[] # 모음
consonant=[] # 자음
for c in chars:
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        vowel.append(c)
    else:
        consonant.append(c)
# 암호 : L자리 문자열/ 최소 한 개의 모음, 최소 두 개의 자음/ 정렬
vowel_count=1
ans = []
while True:
    consonant_count = L - vowel_count
    if vowel_count>len(vowel) or consonant_count<2:
        break
    volist = list(itertools.combinations(vowel, vowel_count))
    conlist = list(itertools.combinations(consonant, consonant_count))
    for v in volist:
        for c in conlist:
            lst = v + c
            tmp = sorted(lst)
            ans.append(''.join(tmp))
    vowel_count+=1
ans.sort()
for a in ans:
    print(a)


