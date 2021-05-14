"""
# 정확성 : 만점
# 효율성 : 0점
def solution(k, room_number):
    result = []
    for r in room_number:
        if r not in result:
            result.append(r)
        else:
            for r2 in range(r+1, k+1):
                if r2 not in result:
                    result.append(r2)
                    break
    return result
"""

# 구글링 풀이 -> 이해 잘 안간다.
# import sys
# sys.setrecursionlimit(10000000)
# def solution(k, room_number):
#     rooms = dict()
#     for num in room_number:
#         c = find_emptyRoom(num, rooms)
#     return list(rooms.keys())
#
# def find_emptyRoom(num, rooms):
#     if num not in rooms.keys():
#         rooms[num] = num + 1
#         return num
#     empty = find_emptyRoom(rooms[num], rooms)
#     rooms[num] = empty + 1
#     return empty
def solution(k, room_number):
    roomDict = {}
    result = []
    for r in room_number:
        n = r
        visit = [n]
        while n in roomDict.keys():
            n = roomDict[n]
            visit.append(n)
        result.append(n)
        for j in visit:
            roomDict[j] = n+1
    return result



# solution(10, [1,3,4,1,3,1])