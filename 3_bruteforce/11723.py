import sys
M=int(sys.stdin.readline())
S=[]

def add(x):
    global S
    if x not in S:
        S.append(x)

def remove(x):
    global S
    if x in S:
        S.remove(x)

def check(x):
    global S
    if x in S:
        print(1)
    else:
        print(0)

def toggle(x):
    global S
    if x in S:
        S.remove(x)
    else:
        S.append(x)

def all():
    global S
    S=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def empty():
    global S
    S=[]

for _ in range(M):
    func = str(sys.stdin.readline().strip())
    if func == 'all':
        all()
        continue
    elif func == 'empty':
        empty()
        continue
    func = func.split()
    if func[0] == "add":
        add(int(func[1]))
    elif func[0]=="check":
        check(int(func[1]))
    elif func[0]=="remove":
        remove(int(func[1]))
    elif func[0]=="toggle":
        toggle(int(func[1]))
    else:
        break