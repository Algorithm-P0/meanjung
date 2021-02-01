import sys
N = int(sys.stdin.readline())
S = int(sys.stdin.readline())
student = list(map(int, sys.stdin.readline().split()))
stu_list = []
stu_dict = {}
def delete(s):
    # dict에서 가장 작은 value를 갖는 key를 찾아서
    # list에서 삭제
    # 만약 2개 이상이라면 가장 앞에 있는 원소 삭제
    # dict에서도 해당 key 삭제
    # dict에 s에 해당하는 값 =1 넣기
    min_value = sys.maxsize
    min_key = []
    for k in stu_dict.keys():
        if min_value>stu_dict[k]:
            min_value = stu_dict[k]
            min_key = [k]
        elif min_value==stu_dict[k]:
            min_key.append(k)
    for l in stu_list:
        if l in min_key:
            stu_list.remove(l)
            del stu_dict[l]
            break
    stu_list.append(student[s])
    stu_dict[student[s]]=1

for s in range(S):
    if student[s] in stu_list:# stu_list에 있다면
        stu_dict[student[s]]+=1# +1만 해주면 된다.
    else:
        if len(stu_list)<N:# stu_list에 여유가 있다면
            stu_list.append(student[s])
            stu_dict[student[s]]=1
        else:# stu_list에 여유가 없다면 삭제하고 넣기
            delete(s)
stu_list.sort()
print(' '.join(map(str, stu_list)))