import re
from operator import itemgetter
def solution(files):
    fileList = []
    for file in files:
        file_lower = file.lower()
        numList = re.findall('\d+', file_lower)
        num = numList[0]
        if len(num) >= 6:
            num = num[:5]
        file_lower_split = file_lower.split(num)
        file_lower_split.insert(1, int(num))
        file_lower_split.append(files.index(file))
        fileList.append(tuple(file_lower_split))
    fileList.sort(key=itemgetter(0, 1))
    result = []
    for f in fileList:
        result.append(files[f[-1]])
    return result