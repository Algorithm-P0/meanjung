# def solution(s):
#     s = s[1:-1]
#     numbers = []
#     string = ''
#     for i in s:
#         if i=='{': # 집합 내부 진입
#             bracketFlag = 0
#             continue
#         elif i=='}': # 집합 내부 빠져나옴
#             numbers.append(list(map(int, string.split(','))))
#             string = ''
#             bracketFlag = 1
#             continue
#         elif i==',':
#             if bracketFlag==1:
#                 continue
#             else:
#                 string += i
#         else:
#             string += i
#     # numbers = [[2], [2, 1], [2, 1, 3], [2, 1, 3, 4]]
#     numbersDict = {}
#     for num in numbers:
#         numbersDict[len(num)] = num
#     result = []
#     i = 1
#     while True:
#         if i not in numbersDict.keys():
#             break
#         for v in numbersDict[i]:
#             if v not in result:
#                 result.append(v)
#                 break
#         i+=1
#     return result

# 프로그래머스 찢어놓은 풀이
import re
from collections import Counter
def solution(s):
    # print(re.findall('\d+', s)) -> ['4', '2', '3', '3', '2', '3', '4', '1', '2', '3']
    s = Counter(re.findall('\d+', s)) # -> Counter({'3': 4, '2': 3, '4': 2, '1': 1})
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x:x[1], reverse=True)]))



s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
solution(s)