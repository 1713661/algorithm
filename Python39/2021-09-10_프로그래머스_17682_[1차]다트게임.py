# 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다.
# 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 
#  이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 
#  이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 
#  이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)

# 36분
def solution(dartResult):
    import re
    scores = re.findall('[1]*[0-9]+[SDT][*#]*',dartResult)
    ############([1-9]|[10])안되는 이유????
    ### 그냥 [0-9]+썼으면 됐었음.. 잘못된 입력 들어오지 않기 때문
    print("scores=",scores)
    answer = 0
    dic = {
        "S":1,
        "D":2,
        "T":3
    }
    
    N = len(scores)
    newscores = [0]*N
    for i in range(len(scores)):
        #print("score=",scores[i][0:2])

        if scores[i][0:2]=="10":
            score = 10
            x = scores[i][2]

        else:
            score = int(scores[i][0])
            x = scores[i][1]
        print("score=",score)
        newscores[i] = pow(score,dic[x])
        if len(scores[i])==3:
            if scores[i][2]=='#':
                newscores[i] = -newscores[i]
            elif scores[i][2]=='*':
                newscores[i] *=2
                if i>0:
                    newscores[i-1] *=2

    return sum(answer)

print(solution("1S2D*3T"))
# 37
print(solution("1D2S#10S"))
# 9
print(solution("1S*2T*3S"))
# 23