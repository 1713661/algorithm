# 몇 번 음식부터 다시 섭취하면 되는지 return 하도록 
# 7분 30초 알고리즘이 아예 안떠올라서 이코테 답지 봄 -> (시간,음식번호) "튜플"로 저장해야함
# 다시 풀어봤는데 안됨(내가 알고리즘을 잘 못 생각한듯) 이코테 풀이
# 아니 이게 어떻게 난이도1에 풀이시간 30분임..그리디 문제 따로 많이 풀어봐야하나?
# 그리디는 템플릿이 없어서 생각을 잘 못하는듯..

#### 아 내가 짠 코드 안되는 이유가 while문빠져나온다음에 prev_time,time다시 설정하기 까다롭기 때문에
# 이코테 풀이가 더 좋은 풀이인듯
import heapq

def solution(food_times, k):
    
    if sum(food_times)<=k: return -1 # '만약 더 섭취해야 할 음식이 없다면'이므로 k랑 같을때도 포함해야함
                                     # while문안에서 # if len(queue)==0: return -1하는것보다는 이게 더 효율적인 코드
    prev_time = 0
    queue = [(food_times[i],i+1) for i in range(len(food_times))]
    heapq.heapify(queue)
    while k>0:
        time,idx = heapq.heappop(queue)
        k -= (time-prev_time)*(len(queue)+1) #######time-prev_time ... len(queue)+1은 맞음(숫자 팍팍 줄일려고 while문 도는거니까)
        print("time=",time,"idx=",idx)
        print("k=",k)
        prev_time = time

    ### break문 빠져나오고 할거 
    k += (time*(len(queue)+1))
    heapq.heappush(queue,(time,idx))
    print("afterWhile k=",k)
    queue = sorted(queue,key=lambda x:x[1]) #번호순으로 정렬
    print("sorted_queue=",queue)
    idx = k%len(queue)
    print("idx=",idx)
    return queue[idx][1]

#print(solution([3, 1, 2],5)) # 1
#print(solution([8, 6, 4],15)) # 2

print("answer 3=",solution([4,2,3,6,7,1,5,8],16)) # answer = 3
#print("answer 4=",solution([4,2,3,6,7,1,5,8],27)) #answer = 5