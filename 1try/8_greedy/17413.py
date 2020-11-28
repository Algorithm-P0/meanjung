import sys
ans = ''
word = ''
flag = 0 
for c in sys.stdin.readline().strip():
    if c=='<':
        flag^=1
        ans+=word
        word='<'
    elif c=='>':
        flag^=1
        ans+=(word+'>')
        word=''
    elif c==' ':
        ans+=(word+' ')
        word=''
    else:
        if flag==0: #false 괄호 밖
            word = c + word
        else:# 괄호 안
            word += c
if word:
    ans += word
print(ans)

