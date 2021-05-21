def solution(dartResult):
    dartList = list(dartResult)
    answer = []
    d = []
    for i in range(len(dartList)):
        if dartList[i] == '1' and dartList[i+1]=='0':
            d.append('10')
        elif dartList[i] == '0' and dartList[i-1] == '1':
            continue
        else:
            d.append(dartList[i])
    squareDict = {'S':1, 'D':2, 'T':3}
    for i in range(1, len(d)):
        if d[i] in squareDict.keys():
            answer.append(int(d[i-1])**squareDict[d[i]])

        if d[i]=='*':
            if len(answer)>=2:
                answer[-1] = answer[-1]*2
                answer[-2] = answer[-2]*2
            else:
                answer[-1] = answer[-1]*2
        elif d[i] == '#':
            answer[-1] = answer[-1]*(-1)
    return sum(answer)

# 정규 표현식으로도 할 수 있다.
# 다음에 이런 문자열관련 나오면 정규식으로 해보기