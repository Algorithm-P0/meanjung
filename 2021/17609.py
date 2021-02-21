import sys
# 해당 인덱스가 회문의 조건을 충족하면 다음 인덱스로 넘어가고
# 해당 인덱스가 회문의 조건을 충족하지 않으면
# 1 - 현재 인덱스에 있는 문자를 제거한 문자열이 회문을 충족하는지
# 2 - 혹은 짝을 이루는 인덱스에 위치한 문자를 제거한 문자열이 회문을 충족하는지
T = int(sys.stdin.readline())
def pseudo(string, left, right):
    while left<right:
        if string[left]==string[right]:
            left+=1
            right-=1
        else:
            return False
    return True
def palindrom(string, left, right):
    while left<right:
        if string[left]==string[right]:#회문 조건 충족
            left+=1
            right-=1
        else:# 회문 조건 불충족 - 유사회문 검사해야 함
            res1 = pseudo(string, left+1, right)
            res2 = pseudo(string, left, right-1)
            if res1==True or res2==True:
                return 1 # 유사회문
            else:
                return 2 # 일반 문자열
    return 0
        
for _ in range(T):
    string = sys.stdin.readline().strip()
    res = palindrom(string, 0, len(string)-1)
    print(res)
