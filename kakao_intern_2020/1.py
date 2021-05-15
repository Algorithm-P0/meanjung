def solution(numbers, hand):
    #           0     1     2     3     4     5     6     7     8     9
    keyPad = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    ly, lx = 3, 0
    ry, rx = 3, 2
    result = ""
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            ly, lx = keyPad[n]
            result += "L"
        elif n == 3 or n == 6 or n == 9:
            ry, rx = keyPad[n]
            result += "R"
        else:
            dy = keyPad[n][0]
            dx = keyPad[n][1]
            if abs(ry - dy) + abs(rx - dx) < abs(ly - dy) + abs(lx - dx):
                ry = dy
                rx = dx
                result += "R"
            elif abs(ry - dy) + abs(rx - dx) > abs(ly - dy) + abs(lx - dx):
                ly = dy
                lx = dx
                result += "L"
            else:
                if hand == "right":
                    ry = dy
                    rx = dx
                    result += "R"
                else:
                    ly = dy
                    lx = dx
                    result += "L"
    return result

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))