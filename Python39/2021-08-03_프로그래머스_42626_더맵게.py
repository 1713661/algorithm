import heapq

def solution(scoville, K):
    answer = 0
    q = []
    for i in range(len(scoville)):
        heapq.heappush(q,scoville[i])

    while True:
        value = heapq.heappop(q)
        if value>=K:
            return answer
        elif q:
            new = value + heapq.heappop(q)*2
            heapq.heappush(q,new)
            answer += 1 
        else:
            if value<K:
                return -1

print("case1=",solution( [1,2,3,9,10,12], 7 ))
print("case2=",solution( [12,11,9,10,6,7,8,1,2,3,4,5], 1000 ))
print("case1=",solution( [1,2], 0 ))

