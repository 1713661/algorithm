# 프로그래머스 67258 보석쇼핑에서 while end<length: 쓸 수 있었던 이유는, 보석을 적어도 하나씩 포함했어야 하기 때문!
# (절대 start가 end를 넘지 않음)
import sys
input = sys.stdin.readline

N,S = map(int,input().split()) # 10 ≤ 길이 N짜리 수열 < 100,000  0 < 합 S ≤ 100,000,000
li = list(map(int,input().split())) # 각 원소는 10,000이하의 자연수

end,sum = 0,li[0]
ans = int(1e9)
for start in range(N): # while left<=right은 이코테 정렬 코드쉐도잉. 투 포인터도 템플릿 있다는 것 기억하기!
    while sum<S and end<N:
        end += 1
        if end != N: sum += li[end] 
    if end==N: break
    ans = min(ans,end-start+1)
    sum -= li[start]

if ans == int(1e9): ans=0
print(ans)





