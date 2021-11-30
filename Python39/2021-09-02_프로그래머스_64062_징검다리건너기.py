### 이건 무지의 먹방라이브처럼 k가 있는 게 아니라 한번씩 건너는거기때문에
# heapq써서 합계산 할필요없음!!
# 18분 근데 알고리즘 생각 못하겠음... 다른사람코드보기!!
# 43분 일단 짜긴 했음
# 58분 디버깅 계속 하긴 하는데 못고치겠음 -> 알고리즘 자체를 생각해야함!!!!
# +11분 어디가 문젠지는 알겠는데 어떻게 구현해야할지 모르겠음 -> 다른사람코드보기

## answer에 대하여 이진탐색하는거임!!!!!!!
def solution(stones, k):
   
    min_ans,max_ans = min(stones),max(stones)
    answer = 0

    while min_ans<=max_ans:
        N = (min_ans+max_ans)//2  # 건널 수 있는 사람의 수(중간값)
        impossible = 1 # 건너야하는 징검다리의 수
        max_impossible = 0 # 건너야하는 징검다리의 수의 최댓값(한 while루프에서)
        for stone in stones:
            if stone<N: 
                # stone의 숫자가 N보다 작으면 그건 N번째 사람이 못건넌다는뜻
                impossible += 1
            else:
                max_impossible = max(max_impossible,impossible)
                impossible = 1
        max_impossible = max(max_impossible,impossible)
    
        if max_impossible>k: 
            max_ans = N-1 # 건널 수 있는 사람의 수(answer)는 N보다 작음
        else: 
            min_ans = N+1
            answer = max(answer,N) # answer중 가장 큰 값
    
    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3)) #3