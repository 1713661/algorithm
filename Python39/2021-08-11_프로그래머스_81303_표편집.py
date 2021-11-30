# 모든 명령어를 수행한 후 표의 상태와 처음 주어진 표의 상태를 비교하여 
# 삭제되지 않은 행은 O, 삭제된 행은 X로 표시하여 문자열 형태로 return
# 효율성 테스트 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 일단 효율성 생각안하고 짜보자
########### heapq로 구현하기!!!!!!!! 왜 heapq를 생각못했지.. (효율성 있다고 해서 행 삭제할때마다 반영하면 안된다고 생각했음..)
########### 자료구조 효과적으로 쓸 수 있어야!!!!!
# 시간복잡도 log2N이어도 엄청난거임 (N=백만이어도 20이니까)
######### 문제에서 효율성은 주어진 제한사항 외에 다른 거 없다고 했으니까 그 '커트라인 안에만' 들어오면 됨

# 15분 일단 heapq쓰기(maxheap, minheap 써야한다는 걸 깨달음)
# +7분 heapify 문법........................
# +35분 알고리즘을 생각하는 게 아니라 print문 찍어보면서 하나 고치고 또 하나 고치고.. 이런식이야 이렇게 코딩하면 안돼!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# +30분 성공!!!!!!!!!!!!

####################### 통일된 알고리즘 생각하는 것이 중요
## select는 항상 bigger[0] 도록 bigger, smaller 관리하기!!!!!
## smaller[0]은 select 바로 앞에 있는 안지워진 원소가 되도록 관리하기!!!!!!(음수)

import heapq

def solution(n, k, cmds):

    arr = ['O'] * n # 문자열을 배열형태로 저장

    bigger = [i for i in range(k,n)]  # k~n-1
    smaller = [-i for i in range(k)]   # 0~k-1
    heapq.heapify(bigger)
    heapq.heapify(smaller)

    deleted = []  # 삭제한 항 인덱스 저장할 스택(스택이니까 deque 쓸 필요없음!!!!!!!!!!!!!! 진짜 이런것도 그러면 안돼..)
    select = k    # 현재 선택된 행
    
    for cmd in cmds:

        # "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다. # 표의 범위를 벗어나는 이동은 입력으로 주어지지 않습니다.
        if cmd[0]=="U": 
            for _ in range(int(cmd[2:])):
                if len(smaller)>0:
                    heapq.heappush(bigger,-heapq.heappop(smaller))
            select = bigger[0] 

        # "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
        elif cmd[0]=="D": 
            for _ in range(int(cmd[2:])):
                if len(bigger)>0:
                    heapq.heappush(smaller,-heapq.heappop(bigger))
            select = bigger[0] 

        # "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다.
        elif cmd[0]=="C":  
            deleted.append(select) #O(1)
            heapq.heappop(bigger)

            # 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
            if len(bigger)==0:
                heapq.heappush(bigger,-heapq.heappop(smaller))
                select = bigger[0]

            else: 
                select = bigger[0]

        # "Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
        elif cmd[0]=="Z": 
            num = deleted.pop() #O(1)
            if num>bigger[0]:
                heapq.heappush(bigger,num)
            else:
                heapq.heappush(smaller,-num)


    for idx in deleted:
        arr[idx]='X'
    
    answer = ''
    for item in arr:
        answer += item
    
    return answer

print(solution( 8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])) # "OOOOXOOO"
print(solution( 8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])) #"OOXOXOOO"