ans = []
def solution(user_id, banned_id):
    resultSet = []
    for ban in banned_id:
        tmpSet = []
        for user in user_id:
            flag = 0
            if len(ban)==len(user):
                for i in range(len(user)):
                    if ban[i]=='*' or ban[i]==user[i]:
                        continue
                    elif ban[i]!=user[i]:
                        flag = 1
                        break
                if flag==0:
                    tmpSet.append(user_id.index(user))
        resultSet.append(tmpSet)
    solution2(0, resultSet, [])
    return len(ans)

def solution2(i, resultSet, lst):
    # resultSet = [[0,1], [0,2], [3,4], [3,4]]
    if i >= len(resultSet):
        if set(lst) not in ans:
            ans.append(set(lst))
        return
    for j in resultSet[i]:
        if j not in lst:
            lst.append(j)
            solution2(i+1, resultSet, lst)
            lst.pop()
