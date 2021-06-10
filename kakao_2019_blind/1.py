def solution(record):
    result = []
    idDict = dict()
    for r in record:
        splited = r.split(" ")
        com = splited[0]
        id = splited[1]
        temp = [id]
        if com == "Enter":
            nickname = splited[2]
            idDict[id] = nickname
            temp.append("님이 들어왔습니다.")
        elif com == "Leave":
            temp.append("님이 나갔습니다.")
        elif com == "Change":
            nickname = splited[2]
            idDict[id] = nickname
            continue
        result.append(temp)
    ans = []
    for r in result:
        ans.append(idDict[r[0]]+r[1])
    return ans


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
"""
"Enter uid1234 Muzi"
"Enter uid4567 Prodo"
"Leave uid1234"
"Enter uid1234 Prodo"
"Change uid4567 Ryan"
"""