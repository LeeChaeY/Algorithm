# 약 1시간정도 소요
def solution(friends, gifts):
    d = {key:i for i, key in enumerate(friends)}
    size = len(friends)
    answer = [0 for _ in range(size)]
    gift_arr = [[0 for _ in range(size)] for _ in range(size)]
    gift_num = [0 for _ in range(size)]
    
    for s in gifts:
        p1, p2 = s.split()
        gift_arr[d[p1]][d[p2]] += 1
        gift_num[d[p1]] += 1
        gift_num[d[p2]] -= 1
    
    for i in range(size-1):
        for j in range(i+1, size):
            if ((gift_arr[i][j] == 0 and gift_arr[j][i] == 0) or (gift_arr[i][j] == gift_arr[j][i])):
                if gift_num[i] > gift_num[j]:
                    answer[i] += 1
                elif gift_num[i] < gift_num[j]:
                    answer[j] += 1
            else:
                if gift_arr[i][j] > gift_arr[j][i]:
                    answer[i] += 1
                elif gift_arr[i][j] < gift_arr[j][i]:
                    answer[j] += 1
    return max(answer)
