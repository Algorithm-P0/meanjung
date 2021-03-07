import sys
ans = ''
word = ''
flag = 0
for c in sys.stdin.readline().strip():
    if c=='<':
        flag = 1 #1->0/ 0->1
        ans+=word
        word = '<'
    elif c=='>':
        flag=0
        ans+=(word+'>')
        word = ''
    elif c==' ':
        ans += (word+' ')
        word =''
    else:
        if flag==0:
            word = c + word
        else:
            word += c
if word:
    ans += word
print(ans)