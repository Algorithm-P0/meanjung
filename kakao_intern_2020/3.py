def solution(gems):
    size = len(set(gems))
    gemDict = {gems[0]:1}
    temp = [0, len(gems)-1]
    start, end = 0, 0

    while start<len(gems) and end<len(gems):
        if len(gemDict) == size:# 모든 element 다 들어있음
            if end - start < temp[1] - temp[0]:
                temp = [start, end] # 정답 update
            # 충족은 되지만 길이가 더 짧지 않음
            if gemDict[gems[start]] == 1:
                del gemDict[gems[start]]
            else:
                gemDict[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            if gems[end] in gemDict.keys():
                gemDict[gems[end]] += 1
            else:
                gemDict[gems[end]] = 1
    return [temp[0]+1, temp[1]+1]

print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))