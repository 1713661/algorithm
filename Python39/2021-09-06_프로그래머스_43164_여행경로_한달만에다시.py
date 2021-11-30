# 항상 "ICN" 공항에서 출발합니다.
# 주어진 항공권은 모두 사용해야 합니다.
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
# 백트래킹?
# 40분 아 짱나 dict만드는 거 너무 비효율적인 것 같음
# len(graph)==3이기때문에 이 조건 안됨.. dict()은 그래서 처리하기 힘듦..
# if not check: ######이렇게 뒤에서 처리하는것도 No.....
####### 백트래킹은 기본적으로 기존 데이터 '복사'해야함!!!!!!!! '참조하면안됨'

# 코드만
def solution(tickets):
    
    answer = []

    graph = dict()
    for ticket in tickets:
        if ticket[0] not in graph:
            graph[ticket[0]] = [ticket[1]]
        else:
            new = graph.get(ticket[0])[:]
            new.append(ticket[1])
            graph[ticket[0]] = new

    def dfs(start,route):
        
        if len(route) == len(tickets)+1:
            answer.append(route[:])
            return
        
        if graph.get(start)==None:
            return

        for nxt in graph.get(start)[:]:
            
            route.append(nxt)
            new = graph.get(start)[:] ##### 그리고 graph copy해야돼서 더 복잡... 그냥 tickets에서 바로쓰자
            new.remove(nxt)
            graph[start] = new

            dfs(nxt,route)

            route.pop()
            new = graph.get(start)[:]
            new.append(nxt)
            graph[start] = new

    dfs("ICN",["ICN"])
     
    answer.sort()
    for ans in answer:
        if len(ans)!=len(tickets)+1:
            continue
        return ans
   


''' # 주석포함
def solution(tickets):

    answer = []

    graph = dict()
    for ticket in tickets:
        if ticket[0] not in graph:
            graph[ticket[0]] = [ticket[1]]
        else:
            new = graph.get(ticket[0])
            new.append(ticket[1])
            graph[ticket[0]] = new
    # dic= {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}
    print("graph=",graph)

    tickets = [tuple(item) for item in tickets]
    #print("tickets=",tickets)

    def dfs(start,route):
        
        if len(graph)==0: #len(graph)==3이기때문에 이 조건 안됨.. dict()은 그래서 처리하기 힘듦..
            answer.append(route)
            return
        
        print("route=",route)
        check=False
        for nxt in graph.get(start): 
            #tickets.remove((start,nxt))
            check=True
            route.append(nxt)
            new = graph.get(start) ##### 그리고 graph copy해야돼서 더 복잡... 그냥 tickets에서 바로쓰자
            new.remove(nxt)
            graph[ticket[0]] = new
            print("remove=",graph,"route=",route,"length=",len(graph))
            dfs(nxt,route)
            #tickets.append((start,nxt))
            route.pop()
            new = graph.get(start)
            new.append(nxt)
            graph[ticket[0]] = new
            print("append=",graph,"route=",route)

        if not check: ######이렇게 뒤에서 처리하는것도 No.....
            print("hiiiiiiiiii=",route) # hiiiiiiiiii= ['ICN', 'SFO', 'ATL']
            answer.append(route)
            print("helllllllll0=",answer) # helllllllll0= [['ICN', 'SFO', 'ATL'], ['ICN', 'SFO', 'ATL']]
            return

    dfs("ICN",["ICN"])
    
    answer.sort()
    print("terminal=",answer)
'''  
#print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
#print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

#print(solution([["ICN", "BBB"],["ICN", "CCC"],["BBB", "CCC"],["CCC", "BBB"],["CCC", "ICN"]])) 
# 답: ["ICN", "BBB", "CCC", "ICN", "CCC", "BBB"]

print(solution([["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]))
# ["ICN", "B", "ICN", "A", "D", "A"]

print(solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]))
# ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"]

print(solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]))
# ["ICN", "COO", "ICN", "BOO", "DOO"]

print(solution([["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]]))
# ["ICN", "SFO", "ICN", "SFO", "QRE"]

print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]))
# ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]