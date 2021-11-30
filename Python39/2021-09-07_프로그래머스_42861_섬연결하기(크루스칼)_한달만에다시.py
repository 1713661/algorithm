# costs의 길이는 ((n-1) * n) / 2이하입니다. (두개의 섬 사이에는 하나의 다리밖에 없음)
# 크루스칼 알고리즘
# 21분 처음에 union_parent 할필요없음..
# 23분

INF = int(10e9)
def solution(n, costs):
    parent = [k for k in range(n)] 
    
    def find_parent(x):
        if parent[x]!=x:
            parent[x] = find_parent(parent[x])
        return parent[x]

    def union_parent(a,b):
        A = find_parent(a)
        B = find_parent(b)
        if A>B:
            parent[A]=B
        else:
            parent[B]=A

    costs = sorted(costs, key=lambda x:x[2]) # 비용순으로 다리 정렬
                
    '''
    for cost in costs:
        union_parent(cost[0],cost[1])
    print(parent)
    '''
    answer = 0 
    
    # 사이클이 생기지 않으면 비용 추가(union parent도 해야함!!!!!!!)
    for cost in costs:
        if find_parent(cost[0])!=find_parent(cost[1]):
            union_parent(cost[0],cost[1])
            answer += cost[2]

    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])) # 4

# costs의 길이는 ((n-1) * n) / 2
# 다리는 무조건 최소 n-1개는 필요한건가?
# 플로이드 워셜 알고리즘?
# 간선마다의 노드 2개 정보 visited해서 visited 다 true되는 애들 중 최소값 리턴?
# A-B 최단거리랑 모든 노드 연결하는거랑 전혀 상관이 없잖아.. (예외사항 너무 많음)(에외사항 많은 코드, 분기문 많은 코드 절대 짜면 안되는 코드!!!!!)
# 17분(플로이드 워셜 알고리즘 작성 완료)
# +45분(그리디 3중 for문 헤맴) 25점............어디서 틀린걸까(알고리즘을 어떻게 잘못생각한걸까..)
######## 왜 알고리즘을 짧게 생각하지 못할까...
# from collections import deque

# 유니온 파인드 문제였음.. 이코테 10장 복습해야할듯
# 크루스칼 알고리즘 그 자체라고 한다. '크루스칼','플로이드' 둘 다 4글자여서 헷갈렸음ㅋㅋㅋㅋㅋ 플로이드 워셜로 푸는 거 아닌듯