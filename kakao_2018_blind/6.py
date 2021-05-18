# Correct but not sexy..

# def solution(n, arr1, arr2):
#     board = []
#     for i in range(n):
#         binary = bin(arr1[i] | arr2[i])[2:]
#         if len(binary) < n:
#             zero = '0'*(n-len(binary))
#             binary = zero + binary
#         board.append(binary)
#     result = []
#     for b in board:
#         resultStr = ''
#         for i in b:
#             if i=='1':
#                 resultStr += '#'
#             else:
#                 resultStr += ' '
#         result.append(resultStr)
#     return result

# 깔끔하고 짧은 풀이
def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = bin(i|j)[2:]
        a12 = a12.rjust(n, '0')# a12라는 문자열이 길이 n을 채울때까지 앞에 0채워넣기
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer

solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])
