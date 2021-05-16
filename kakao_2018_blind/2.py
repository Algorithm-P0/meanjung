# correct but not sexy...
#
# def makeDict(string):
#     string = string.lower()
#     strDict = {}
#     for i in range(len(string) - 1):
#         if not 'a' <= string[i] <= 'z':
#             continue
#         elif not 'a' <= string[i + 1] <= 'z':
#             i += 2
#         else:  # 둘 다 문자임이 확인되었음
#             if string[i:i + 2] not in strDict.keys():
#                 strDict[string[i:i + 2]] = 1
#             else:
#                 strDict[string[i:i + 2]] += 1
#     return strDict
# def solution(str1, str2):
#     str1Dict = makeDict(str1)
#     str2Dict = makeDict(str2)
#     if len(str1Dict)==0 and len(str2Dict)==0:
#         J = 1*65536
#     else:
#         intersec = {}
#         union = {}
#         for k1 in str1Dict.keys():
#             if k1 in str2Dict.keys():
#                 intersec[k1] = min(str1Dict[k1], str2Dict[k1])
#                 union[k1] = max(str1Dict[k1], str2Dict[k1])
#             else:
#                 union[k1] = str1Dict[k1]
#         for k2 in str2Dict.keys():
#             if k2 not in union.keys():
#                 union[k2] = str2Dict[k2]
#         intersecSum = sum([intersec[k] for k in intersec.keys()])
#         unionSum = sum([union[k] for k in union.keys()])
#         J = (intersecSum*65536)//unionSum
#     return J

# fun cool sexy한 풀이
import re
import math
def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0:
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum / hap_sum) * 65536)

print(solution('aa1+aa2', 'AAAA12'))