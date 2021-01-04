import sys
board = list(map(str, sys.stdin.readline().strip()))
flag = 0
i = 0
while i<len(board):
    if board[i:i+4]==list('XXXX'):
        board[i:i+4]='AAAA'
        i+=4
    elif board[i:i+2]==list('XX'):
        board[i:i+2]='BB'
        i+=2
    elif board[i]=='.':
        i+=1
    else:
        flag = 1
        break
if flag == 1:
    print(-1)
else:
    print(''.join(board))