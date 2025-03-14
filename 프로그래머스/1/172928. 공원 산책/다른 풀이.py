dx = {'N':-1, 'S':1, 'E':0, 'W': 0}
dy = {'N': 0, 'S':0, 'E':1, 'W':-1}

def solution(park, routes):
    answer = []
    x, y = -1, -1
    N, M = len(park), len(park[0])
    for i in range(N):
        for j in range(M):
            if park[i][j] == 'S':
                x, y = i, j

    for route in routes:
        dir_, dist = route.split(' ')

        isFalse = False
        for i in range(1, int(dist) + 1):
            nx, ny = x + dx[dir_] * i, y + dy[dir_] * i
            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                isFalse = True
                break
            if park[nx][ny] == 'X':
                isFalse = True
                break

        if isFalse:
            continue
        nx, ny = x + dx[dir_] * int(dist), y + dy[dir_] * int(dist)
        x, y = nx, ny

    answer = [x, y]

    return answer



def solution(park, routes):
    W = len(park[0])
    park = [['X']*(W+2)] + [[*'X'+i+'X'] for i in park] + [['X']*(W+2)]

    x,y = 1,0
    while park[x][y]!='S':
        y += 1
        if y>W:
            x,y = x+1,0

    delta = {k:v for k,v in zip('NEWS',[(-1,0),(0,1),(0,-1),(1,0)])}
    for i in routes:
        v,d = i.split()
        for k in range(1,int(d)+1):
            X,Y = x+k*delta[v][0], y+k*delta[v][1]
            if park[X][Y]=='X':
                break
        else:
            x,y = X,Y
    return [x-1,y-1]

