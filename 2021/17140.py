import sys
r, c, k = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

if len(A)>r-1 and len(A[0])>c-1:
    if A[r-1][c-1]==k:
        print(0)
        sys.exit()
time = 1
while time<=100:
    next_A, max_len, is_transpose = [], 0, 0
    # R, C 중 어느 것을 해야하는지
    if len(A)<len(A[0]):
        A = list(zip(*A))
        is_transpose = 1
    
    for row in A:
        # row에 해당하는 값들의 빈도수 저장: cnt
        maxn = max(row)
        cnt = [0]*(maxn+1)
        for v in row:
            if v>0:
                cnt[v] += 1
        
        # row를 temp_row로 바꿀 것
        temp_row = []
        for index, key in enumerate(cnt):
            if key!=0:
                temp_row.append([key, index])
        temp_row.sort() # 정렬하기
        temp_row2 = []
        for l in temp_row:
            temp_row2.extend([l[1], l[0]]) # 값, 빈도수대로 저장
        next_A.append(temp_row2) # 변화할 A
        max_len = max(max_len, len(temp_row2))
    # 0으로 dummy 채우기
    for row in next_A:
        if len(row) < max_len:
            z = [0]*(max_len-len(row))
            row.extend(z)
    A = next_A
    if is_transpose:
        A = list(zip(*A))
    
    # 답인지 check
    if len(A)>r-1 and len(A[0])>c-1:
        if A[r-1][c-1]==k:
            print(time)
            sys.exit()
    time += 1
print(-1)