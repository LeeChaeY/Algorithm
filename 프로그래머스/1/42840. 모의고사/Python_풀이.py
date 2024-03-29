def solution(answers):
    answer = []
    ans=[0,0,0]
    one = [1,2,3,4,5]*(len(answers)//5) + [1,2,3,4,5][0:len(answers)%5]
    two = [2,1,2,3,2,4,2,5]*(len(answers)//8) + [2,1,2,3,2,4,2,5][0:len(answers)%8]
    three = [3,3,1,1,2,2,4,4,5,5]*(len(answers)//10) + [3,3,1,1,2,2,4,4,5,5][0:len(answers)%10]
    for i in range(len(answers)):
        if answers[i]==one[i]:
            ans[0]+=1
        if answers[i]==two[i]:
            ans[1]+=1
        if answers[i]==three[i]:
            ans[2]+=1
    answer += [i+1 for i in range(len(ans)) if ans[i]==max(ans)]
    return answer
