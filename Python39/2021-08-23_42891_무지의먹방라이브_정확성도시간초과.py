# 5분 문제읽고 이해&효율성 알고리즘 생각
# 8분 일단 정확성통과목표(+3분)
# 14분 while numOfFood:은 나중에 idx리턴하기 어려움(제발 급하게풀지말기)
# 30분 알고리즘 완전 잘못 생각한듯 
# +20분? 정확성테스트에서도 런타임에러 장난아니게 뜸 그냥 새롭게 다시짜기!!
# idx+=1 대신 다 idx = (idx+1)%numOfFood로 바꾸고 while food_times[idx]==0로 바꿨더니 시간초과만 발생 
# 다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식을 말한다. 근데 이거 거꾸로가는거아님!

def solution(food_times, k):
    numOfFood = len(food_times)
    #length = k//numOfFood   #1
    #remain = k%numOfFood #2

    cnt = k+1
    
    idx = 0
    time = 0

    while cnt:#for i in range(length):

        while food_times[idx]==0: #if문이아니야!!!!! 진짜 이런것도 실수하면 안돼!!!!
            idx = (idx+1)%numOfFood

        if time == k: 
            return idx+1

        food_times[idx] -= 1
        cnt -= 1
        idx = (idx+1)%numOfFood
        time += 1
        #print(time,"nextidx=",idx,food_times)

    return -1


print(solution([3, 1, 2],5))