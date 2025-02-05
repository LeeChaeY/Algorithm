# 7-8분 소요
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(len(score)//m):
        answer += score[m*i:m*i+m][-1] * m
    return answer