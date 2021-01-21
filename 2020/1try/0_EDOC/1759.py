# 조합탐색
import sys
L, C=map(int,sys.stdin.readline().split())
alphabets=list(map(str, sys.stdin.readline().strip().split()))
ja=[]
mo=[]
for a in alphabets:
    if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
        mo.append(a)
    else:
        ja.append(a)


"""
최소 두 개의 자음 & 최소 한 개의 모음
알파벳이 증가하는 순서
"""