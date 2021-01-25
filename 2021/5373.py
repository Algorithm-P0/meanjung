import sys
T = int(sys.stdin.readline())
def rotate(color, ro):
    temp = [[0]*3 for _ in range(3)]
    if ro=='-':
        for y in range(3):
            for x in range(3):
                temp[2-x][y]=color[y][x]
    else:
        for y in range(3):
            for x in range(3):
                temp[x][2-y]=color[y][x]
    return temp
def rotation(p, ro):
    global w, y, r, o, g, b
    if p == "U":
        r1, r2, r3, b1, b2, b3 = r[0][0], r[0][1], r[0][2], b[0][0], b[0][1], b[0][2]
        o1, o2, o3, g1, g2, g3 = o[0][0], o[0][1], o[0][2], g[0][0], g[0][1], g[0][2]
        if ro == "-":
            r[0][0], r[0][1], r[0][2], b[0][0], b[0][1], b[0][2] = g1, g2, g3, r1, r2, r3
            o[0][0], o[0][1], o[0][2], g[0][0], g[0][1], g[0][2] = b1, b2, b3, o1, o2, o3
        else:
            r[0][0], r[0][1], r[0][2], b[0][0], b[0][1], b[0][2] = b1, b2, b3, o1, o2, o3
            o[0][0], o[0][1], o[0][2], g[0][0], g[0][1], g[0][2] = g1, g2, g3, r1, r2, r3
        w = rotate(w, ro)
    elif p == "D":
        r1, r2, r3, b1, b2, b3 = r[2][0], r[2][1], r[2][2], b[2][0], b[2][1], b[2][2]
        o1, o2, o3, g1, g2, g3 = o[2][0], o[2][1], o[2][2], g[2][0], g[2][1], g[2][2]    
        if ro == "-":
            r[2][0], r[2][1], r[2][2], b[2][0], b[2][1], b[2][2] = b1, b2, b3, o1, o2, o3
            o[2][0], o[2][1], o[2][2], g[2][0], g[2][1], g[2][2] = g1, g2, g3, r1, r2, r3
        else:
            r[2][0], r[2][1], r[2][2], b[2][0], b[2][1], b[2][2] = g1, g2, g3, r1, r2, r3
            o[2][0], o[2][1], o[2][2], g[2][0], g[2][1], g[2][2] = b1, b2, b3, o1, o2, o3
        y = rotate(y, ro)
    elif p == "F":
        y1, y2, y3, w1, w2, w3 = y[0][0], y[0][1], y[0][2], w[2][0], w[2][1], w[2][2]
        b1, b2, b3, g1, g2, g3 = b[0][0], b[1][0], b[2][0], g[0][2], g[1][2], g[2][2]
        if ro == "-":
            y[0][0], y[0][1], y[0][2], w[2][0], w[2][1], w[2][2] = g1, g2, g3, b1, b2, b3
            b[0][0], b[1][0], b[2][0], g[0][2], g[1][2], g[2][2] = y3, y2, y1, w3, w2, w1
        else:
            y[0][0], y[0][1], y[0][2], w[2][0], w[2][1], w[2][2] = b3, b2, b1, g3, g2, g1
            b[0][0], b[1][0], b[2][0], g[0][2], g[1][2], g[2][2] = w1, w2, w3, y1, y2, y3
        r = rotate(r, ro)
    elif p == "B":
        w1, w2, w3, b1, b2, b3 = w[0][0], w[0][1], w[0][2], b[0][2], b[1][2], b[2][2]
        g1, g2, g3, y1, y2, y3 = g[0][0], g[1][0], g[2][0], y[2][0], y[2][1], y[2][2]    
        if ro == "-":
            w[0][0], w[0][1], w[0][2], b[0][2], b[1][2], b[2][2] = g3, g2, g1, w1, w2, w3
            g[0][0], g[1][0], g[2][0], y[2][0], y[2][1], y[2][2] = y1, y2, y3, b3, b2, b1
        else:
            w[0][0], w[0][1], w[0][2], b[0][2], b[1][2], b[2][2] = b1, b2, b3, y3, y2, y1
            g[0][0], g[1][0], g[2][0], y[2][0], y[2][1], y[2][2] = w3, w2, w1, g1, g2, g3
        o = rotate(o, ro)
    elif p == "L":
        w1, w2, w3, r1, r2, r3 = w[0][0], w[1][0], w[2][0], r[0][0], r[1][0], r[2][0]
        y1, y2, y3, o1, o2, o3 = y[0][0], y[1][0], y[2][0], o[0][2], o[1][2], o[2][2]    
        if ro == "-":
            w[0][0], w[1][0], w[2][0], r[0][0], r[1][0], r[2][0] = r1, r2, r3, y1, y2, y3
            y[0][0], y[1][0], y[2][0], o[0][2], o[1][2], o[2][2] = o3, o2, o1, w3, w2, w1
        else:
            w[0][0], w[1][0], w[2][0], r[0][0], r[1][0], r[2][0] = o3, o2, o1, w1, w2, w3
            y[0][0], y[1][0], y[2][0], o[0][2], o[1][2], o[2][2] = r1, r2, r3, y3, y2, y1
        g = rotate(g, ro)
    elif p == "R":
        w1, w2, w3, r1, r2, r3 = w[0][2], w[1][2], w[2][2], r[0][2], r[1][2], r[2][2]
        y1, y2, y3, o1, o2, o3 = y[0][2], y[1][2], y[2][2], o[0][0], o[1][0], o[2][0]   
        if ro == "-":
            w[0][2], w[1][2], w[2][2], r[0][2], r[1][2], r[2][2] = o3, o2, o1, w1, w2, w3
            y[0][2], y[1][2], y[2][2], o[0][0], o[1][0], o[2][0] = r1, r2, r3, y3, y2, y1
        else:
            w[0][2], w[1][2], w[2][2], r[0][2], r[1][2], r[2][2] = r1, r2, r3, y1, y2, y3
            y[0][2], y[1][2], y[2][2], o[0][0], o[1][0], o[2][0] = o3, o2, o1, w3, w2, w1
        b = rotate(b, ro)
    
for _ in range(T):
    w = [["w"] * 3 for i in range(3)]
    y = [["y"] * 3 for i in range(3)]
    r = [["r"] * 3 for i in range(3)]
    o = [["o"] * 3 for i in range(3)]
    g = [["g"] * 3 for i in range(3)]
    b = [["b"] * 3 for i in range(3)]
    n = int(sys.stdin.readline())
    action = list(sys.stdin.readline().strip().split())
    for i in action:
        p, ro = list(i)
        rotation(p, ro)
    for i in range(3):
        print(''.join(w[i]))