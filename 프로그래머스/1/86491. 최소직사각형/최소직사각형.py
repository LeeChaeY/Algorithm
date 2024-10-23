#  20분정도 소요
def solution(sizes):
    answer = 1
    a, b = [], []
    min_num = 0
    max_num = 0
    for i, j in sizes:
        if (min(i,j) > min_num):
            min_num = min(i,j)
        if (max(i,j) > max_num):
            max_num = max(i,j)
            
    # print(max_num, min_num)
    return max_num * min_num
