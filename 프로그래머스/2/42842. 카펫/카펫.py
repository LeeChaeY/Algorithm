# 약 25분 소요
def solution(brown, yellow):
    sum = (brown-4)//2
    for i in range(1, sum):
        if i * (sum-i) == yellow:
            break
    return [i+2, sum-i+2] if sum-i < i else [sum-i+2, i+2]