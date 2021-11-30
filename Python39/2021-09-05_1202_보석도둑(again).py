#### 가방이 넣을 수 있는 보석들 담은 최대힙(capable) 만드는 게 포인트!

# 보석도 최소힙에 저장(append&heapify말고 heappush쓰기 시간복잡도도 생각못하다니..)
# 가방은 무게가 가벼운 순으로 정렬해야함
# 가방 무거운 순이면 '무거움' 낭비하는거임

# 보석의 무게가 가방보다 작으면 다른 capable힙에 넣음(최대힙)(while문 돌리기)
# 보석의 무게가 가방보다 크면(while문 빠져나오면) capable.pop 값 answer에 추가
# (그래서 가방 무거운 순으로 정렬하면 안됨)

# ** 반드시 N>K가 아니므로 for문 끝까지 못 돌 수 있음

# 10분
import sys
import heapq
input = sys.stdin.readline

N,K = map(int,input().split())

jewels = []
for _ in range(N):
    heapq.heappush( jewels, tuple(map(int,input().split())) ) #(무게,가격)

bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort() #가방 무게 가벼운 순으로 정렬

answer = 0
capable = [] # bag가 넣을 수 있는 보석들(최대힙)
for bag in bags:
    while jewels and bag>=jewels[0][0]: ######## heappop(jewels)대신 jewels[0][0]쓰면 값 참고만 할 수 있음 
        heapq.heappush(capable,-heapq.heappop(jewels)[1]) #가격만 담기
    if capable:
        answer -= heapq.heappop(capable)
    elif not jewels: #capable도 없고 jewels도 빈 경우
        break
print(answer)

######## 내가 처음 문제 풀었을때
# 20분 이진탐색말고 우선순위큐로 풀어야함
# 26분 첫제출 시간초과
# 47분 bisect 어떻게 효과적으로 써야할지 모르겠음..
# (왜냐면 bisect를 쓰는 건 삽질이었기 때문이지)
# +17분 꼬였어.. 그냥답지보자

# 가격 비싼 순으로, 가격같으면 무게 무거운 순으로
# (한 가방이 감당할수있는 최대무게를 가져가야 다음 가벼운 가방이 가벼운 무게가져갈수있기때문)
# 아냐 가벼운 순으로 탐색해야함.. 진짜 항상 거꾸로 가는구나
# 가방 무거운 순이면 '무거움' 낭비하는거임
