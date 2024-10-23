# 30분 정도 소요
def solution(players, callings):
    answer = players
    d = dict(zip(players, range(len(players))))
    for p in callings:
        idx = d[p]
        answer[idx] = answer[idx-1]
        answer[idx-1] = p
        d[p] = idx-1
        d[answer[idx]] = idx
    return answer