# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 
#        / 스테이지에 도달한 플레이어 수
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
# count함수는 stages에 원소없는 경우 쓸수없음

from bisect import bisect_left,bisect_right

def solution(N, stages):
    l = len(stages)
    stages.sort()

    li = []
    for i in range(1,N+1): 
        btm = l-bisect_left(stages,i)
        if btm==0: 
            rate=0
        else: 
            rate = (bisect_right(stages,i)-bisect_left(stages,i))/ btm
        li.append((rate,i))
    li = sorted(li,key=lambda x: (-x[0],x[1]))

    answer = [item[1] for item in li]
    return answer

print(solution( 5, [2, 1, 2, 6, 2, 4, 3, 3] ))  # [1, 2, 2, 2, 3, 3, 4, 6] # [3,4,2,1,5]
print(solution( 4, [4,4,4,4,4] ))              # [4,1,2,3]