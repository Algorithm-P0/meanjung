import sys
N = sys.stdin.readline().strip()
dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '7':0, '8':0}
sixnine = 0
for n in N:
    if n=='6' or n=='9':
        sixnine+=1
        continue
    dict[n]+=1
if sixnine%2==0:# 짝수라면
    sixnine=sixnine//2
else:
    sixnine=sixnine//2+1
print(max(max(dict.values()), sixnine))