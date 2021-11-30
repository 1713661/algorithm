# 일반리스트 sort하는것보다 heapq로 이진트리 만드는 게 나음 
# ..? 근데 sort가 시간복잡도가 그렇게 안좋은가?
# 아 sort는 O(NlogN)이고 heapify는 O(N)임(굿노트 파이썬 문법에 적어놨음)
# 25분 
import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    heapq.heappush(q,int(input()))

answer = 0 # 얘는 누적합이잖아!!!!!
while len(q)>1: 
    m = heapq.heappop(q)
    n = heapq.heappop(q)
    answer += m+n
    heapq.heappush(q,m+n) # m,n 뽑고 q가 빈 상태에서 m+n 넣으면 len(q)==1됨

print(answer)