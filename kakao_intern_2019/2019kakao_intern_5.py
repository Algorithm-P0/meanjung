"""
# 정확성 테스트: 2개 빼고 OK
# 효율성 테스트: 0점
def solution(stones, k):
    N = len(stones)
    result = 0
    while True:
        cnt = 0
        for i in range(N):
            if cnt>=k:
                return result
            if stones[i] != 0:
                stones[i] -= 1
                cnt = 0
            else:
                cnt += 1
        result += 1
"""


# 정확도 테스트: 100점
# 효율성 테스트: 0점
# import sys
# def solution(stones, k):
#     N = len(stones)
#     people = 0
#     while True:
#         minH = sys.maxsize
#         for s in stones:
#             if s!=0 and s<minH:
#                 minH = s
#         cnt = 0
#         for i in range(N):
#             if stones[i] == 0:
#                cnt += 1
#                if cnt == k:
#                    return people
#             else:
#                 stones[i] -= minH
#                 cnt = 0
#         people += minH

def solution(stones, k):
    left, right = 1, max(stones)
    result = 1
    while left<=right:
        mid = (left + right) // 2
        blank = 0
        flag = True
        for stone in stones:
            if stone<mid:
                blank += 1
                if blank == k:
                    flag = False
                    break
            else:
                blank = 0
        if flag:
            result = max(result, mid)
            left = mid + 1
        else:
            right = mid -1
    return result

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
