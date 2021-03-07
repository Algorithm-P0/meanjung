import sys
def main():
    N = int(sys.stdin.readline())
    board = [[] for _ in range(N*N+1)]
    max_time = 0
    for i in range(1, N*N+1):
        lst = list(map(int, sys.stdin.readline().split()))
        board[i].append(lst[0])
        board[i].extend(lst[2:])
        max_time = max(max_time, max(lst[2:]))
    # board index0 -> 점수
    # 그 다음은 일어나는 시기
    time = 1
    ans = 0
    while True:
        if time>max_time:
            break
        temp = []
        for i in range(1, N*N+1):
            if time in board[i][1:]:
                temp.append(board[i][0])
        ans += max(temp)
        time+=1
    print(ans)
if __name__=="__main__":
    main()