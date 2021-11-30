# end가 아니라 end-request의 최소를 찾아야 하는거니까 뒤로 조금 밀릴수록 좋은거겠지
# 뒤로 조금 밀리려면 weight 오름차순으로 정렬해야겠지 (생각을 해 생각을) (SJF 스케줄링)

'''# 이게 내가 생각해야하는 알고리즘이었음.. 공부하자
우선순위에 의한 처리(기본적으로는 요청 된 순번으로 처리 해야 함.)

요청순으로 특정 작업을 처리하는 도중 다른 요청이 들어오면
1건만 있는 경우 작업 끝나고 처리
2건 이상인 경우는 처리 시간이 짧은 항목부터 처리(그래야 뒤로 덜 밀리니까. 생각을 해 생각을.)
딱 이내용만 맞춰서 돌리면 전부 성공 뜸.

'''
# johnyejin님 코드 heapq로만 바꾸려고 했을 뿐인데 고려사항이 꽤 많음.. 그래도 문제풀었으니 넘어가자!
import heapq

def solution(jobs):

    q = []
    answer = 0
    cur = 0
    jobs = sorted(jobs, key=lambda x: x[0]) #요청시간(request)순으로 정렬
    #print("jobs=",jobs)
    length = len(jobs)

    while len(jobs)!=0 or q: 
        #print("jobs=",jobs,"len=",len(jobs))
        #print("0=",len(jobs))
        idx = len(jobs)
        for i in range(len(jobs)): # job = [request,weight]
            if jobs[i][0]>cur: #i번째job>cur
                idx = i
                break
            heapq.heappush(q,(jobs[i][1],jobs[i][0])) # cur시간안에 요청된 작업들 큐에 넣음 (weight순으로) (weight,request)
        jobs = jobs[idx:] #####인덱스 슬라이싱 jobs객체는 하나?????????
        #print("jobs=",jobs,"len=",len(jobs))
        
        #print("pushq=",q)
        if len(q)==0: #cur시간안에 요청된 작업 없다는거니까 cur 증가시킴
            cur += 1
        else: # q에 원소 있으면
            weight,request = heapq.heappop(q) #weight 짧은순으로 처리
            time = cur-request+weight
            answer += time
            cur = request+time
            #print("weight=",weight,"time=",time,"answer=",answer,"cur=",cur)
        #print("popq=",q)

    return answer//length

'''
import heapq

def solution(jobs):
    q = []
    temp = []
    answer = 0
    cur = 0
    for job in jobs:
        heapq.heappush(q,(job[0]+job[1],job[0])) 
        # (end,request) (1,4), (1,5), (3,0), (3,4), (9,1), (6,2) end = request+weight
        # print(q)
    while q:
        end, request = heapq.heappop(q) # end가 아니라 time써야할 것 같은데???
        print("now: end=",end,"request=",request)
        weight = end-request
        if request>cur:
            time = weight
        else:
            time = cur+weight-request 
            #(cur-request)+weight / request, weight은 언제나 고정값. 따라서 cur을 최소화해야함. 그러려면 weight낮은순으로 처리해야함
            continue
        answer += time
        cur = request+time
        #print("time=",time,"cur=",cur)
    return answer//len(jobs)
'''

#print("case1=",solution( [[0,3], [4,3], [1,9], [2,6], [5,1], [4,1]] ))
#print("case2=",solution([[0, 3], [1, 9], [2, 6]]))

#[request,weight]
#print("case0=",solution([[0, 3], [1, 9], [2, 6]]))
# 내가 알고리즘 자체를 잘못생각한듯. 내가 생각한대로 하면 105//4여서 26맞는데

print("case1=",solution([[0, 10], [2, 10], [9, 10], [15, 2]]))#, 14) 내코드 16
print("case2=",solution([[0, 10], [2, 12], [9, 19], [15, 17]]))#, 25) 내코드 26

print("case3=",solution([[0, 3], [1, 9], [2, 6]]))#, 9)
print("case4=",solution([[0, 1]]))#, 1)
print("case5=",solution([[1000, 1000]]))#, 1000)
print("case6=",solution([[0, 1], [0, 1], [0, 1]]))#, 2)
print("case7=",solution([[0, 1], [0, 1], [0, 1], [0, 1]]))#, 2)
print("case8=",solution([[0, 1], [1000, 1000]]))#, 500) 

print("case9=",solution([[100, 100], [1000, 1000]]))#, 500) #내코드 550
print("case10=",solution([[10, 10], [30, 10], [50, 2], [51, 2]]))#, 6)
print("case11=",solution([[0, 3], [1, 9], [2, 6], [30, 3]]))#, 7)

'''
설명(johnyejin님 풀이)
1. jobs 배열은 소요시간을 기준으로 오름차순 정렬을 한다. 소요시간이 작을수록 각 작업들이 기다리는 시간이 줄어들기 때문이다.
2. jobs 배열이 empty가 될때까지 while문을 돌린다.
3. jobs 길이만큼 for문을 돌리면서 해당 작업의 요청시간이 start(현재까지 진행된 작업 시간)보다 작으면,
  즉, 해당 작업이 진행된 시간보다 먼저 요청이 들어왔으면, 해당 작업을 진행시키고 jobs 배열에서 지워버린다.

def solution(jobs):
    answer = 0
    start = 0  # 현재까지 진행된 작업 시간
    length = len(jobs)

    jobs = sorted(jobs, key=lambda x: x[1])  # 소요시간 우선 정렬

    # weight대로 정렬해서 500번 완전탐색해야함
    # 완전탐색 안하고싶어서 heap 쓴건데 코드 어떻게 짜야할지 모르겠다..
    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= start:
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i) #len(jobs)시간바뀌어도 i는 그대로 증가하나?
                break
            # 해당시점에 아직 작업이 들어오지 않았으면 시간 ++
            if i == len(jobs) - 1:
                start += 1

    return answer // length
'''