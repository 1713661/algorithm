# 취약 지점의 위치는 정북 방향 지점으로부터 시계 방향으로 떨어진 거리로 나타냅니다.
# 시계,반시계 둘다가능
# 취약 지점을 점검하기 위해 보내야 하는 친구 수의 '최소값'을 return 하도록
# 25분 (혹시나했는데 역시나) bisect쓰는건 아니야.. 예외사항 많아짐
# 27분 이코테 답지 봄 -> 저번이랑 똑같은데에서 막혔음
# for friend in friends쓰는 게 아니라 (friends 배열은 끝까지 탐색하지 않을 수 있기 때문에 for문 쓰는게 별로 적합하지 않음)
############ 대신 for idx in range(startidx,startidx+l) 써야함
########### 근데 나중에 나보고 짜라고 하면 못짤 것 같음. 다시 공부하기!!!!
# 분할정복 풀이: https://velog.io/@ckstn0778/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-60062%EB%B2%88-%EC%99%B8%EB%B2%BD-%EC%A0%90%EA%B2%80-X-1-Python

from itertools import permutations

def solution(n, weak, dist):

    l = len(weak) #원래weak배열의길이
    weak += [(w+n) for w in weak]
    answer = len(dist)+1

    for startidx in range(l):
        for friends in permutations(dist,len(dist)): # friends=[4,3,2,1] 완전탐색 8!=720*56 약 4만개?

            cnt = 1 # 투입할 친구의 수
            last = weak[startidx]+friends[cnt-1]    # cnt번째 친구가 갈 수 있는 끝

            for idx in range(startidx,startidx+l): # startidx부터 길이 l만큼의 weak만 확인하면 됨
                # 점검할 수 있는 위치를 벗어나는 경우 weak[idx]가 현재 friend가 갈 수 있는 경우 for문에서 아무것도 안함
                if weak[idx]>last:
                    cnt += 1
                    if cnt > len(dist): break
                    # 여기서 갱신한 last는 26번째줄에서 weak과 비교할 때 씀
                    last = weak[idx]+friends[cnt-1] 
                    
            answer = min(answer,cnt)

    if answer>len(dist): # 까먹지말기
        return -1

    return answer

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4])) # 2
# weak = [1, 5, 6, 10, 13, 17, 18, 22]

print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7])) # 1
# weak = [1, 3, 4, 9, 10, 13, 15, 16, 21, 22]