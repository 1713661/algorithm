### 알고리즘 정리
# 음식 시간이 작은 애부터 heapq에서 뽑음
# sum+(현재음식 시간-전음식시간)*큐길이<=k ######빼줘야함

import heapq

def solution(food_times, k):

    if sum(food_times)<=k: return -1

    length = len(food_times)
    pre_time = 0
    sum_value = 0

    queue = [(food_times[i],i+1) for i in range(length)] # (음식시간,번호)
    heapq.heapify(queue)
    
    # idx는 생각안해도 됨(한바퀴 다 돈거니까)
    while sum_value+(queue[0][0]-pre_time)*length<=k:
        time = heapq.heappop(queue)[0]
        sum_value += (time-pre_time)*length
        length -= 1
        pre_time = time
    
    queue = sorted(queue, key=lambda x: x[1]) # 음식번호순으로 정렬
    return queue[(k-sum_value)%length][1]

print(solution([3, 1, 2],5)) # 1
print(solution([8, 6, 4],15)) # 2

print("answer 3=",solution([4,2,3,6,7,1,5,8],16)) # answer = 3
print("answer 4=",solution([4,2,3,6,7,1,5,8],27)) #answer = 5