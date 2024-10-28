# 약 35분 소요
def solution(park, routes):
    x = []
    h = len(park)
    w = len(park[0])
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                s = [i, j]
            if park[i][j] == 'X':
                x.append([i, j])
    for op in routes:
        op = op.split()
        op[1] = int(op[1])
        if op[0] == 'N' and s[0]-op[1] >= 0:
            p = 1
            for i in range(op[1]):
                if [s[0]-(i+1), s[1]] in x:
                    p = 0
                    break
            if p == 1:
                s = [s[0]-op[1], s[1]]
        elif op[0] == 'S' and s[0]+op[1] < h:
            p = 1
            for i in range(op[1]):
                if [s[0]+(i+1), s[1]] in x:
                    p = 0
                    break
            if p ==1 :
                s = [s[0]+op[1], s[1]]
        elif op[0] == 'W' and s[1]-op[1] >= 0:
            p = 1
            for i in range(op[1]):
                if [s[0], s[1]-(i+1)] in x:
                    p = 0
                    break
            if p == 1:
                s = [s[0], s[1]-op[1]]
        elif op[0] == 'E' and s[1]+op[1] < w:
            p = 1
            for i in range(op[1]):
                if [s[0], s[1]+(i+1)] in x:
                    p = 0
                    break
            if p == 1:
                s = [s[0], s[1]+op[1]]
    return s