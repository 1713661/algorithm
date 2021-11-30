# 57분+15분 (더 간단한 코드 분명 있을텐데...)
# words 인덱스로 graph 만들 필요없음. 
# (효율적으로짜자. 파이썬 문자열라이브러리를 적극 활용하자)
# 악 이렇게 사소한 데에서 틀리는 게 제일 짜증나...(문제조건잘보자)
# 파이썬 내장함수&라이브러리 잘 쓸 줄 알아야함!!!!!!!!!

from collections import deque

def solution(begin, target, words):
    #print("len(words)=",len(words))
    #그래프에 넣어주기
    length = len(begin)
    newwords = words[:]
    newwords.insert(0,begin)


    if not target in newwords: ############### 문제조건 잘보기
        return 0

    # 단어의 인덱스로 그래프 연결관계 나타내기 위해
    graph = [set() for i in range(len(newwords))]
    #print(newwords)

    for word in newwords:
        for nxtword in newwords:
            diff = 0
            idx = length
            for s in range(len(begin)): ####### 더 효율적으로 짜는법
                if word[s] == nxtword[s]: continue
                elif word[s]!=nxtword[s] and diff==0:
                    diff += 1
                else: 
                    idx = s
                    break
            if diff==1 and idx==length:
                idx1 = newwords.index(word)
                idx2 = newwords.index(nxtword)
                #print("word=",word,"nxtword=",nxtword)
                graph[idx1].add(idx2)
                graph[idx2].add(idx1)

    for i in range(len(graph)):
        graph[i]=list(graph[i]) # bfs에서 탐색 편하게 하기 위해서 list 자료형으로 바꿈
    '''
    for i in range(len(graph)):
        print(graph[i])
    '''
    
    
    visited = [False]*len(newwords)
    queue = deque()
    visited[0]=True
    queue.append((0,0))
    while queue:
        x,cnt = queue.popleft()
        #print("now=",x,"cnt=",cnt)
        if x==newwords.index(target):
            return cnt
        for nxt in graph[x]:
            if not visited[nxt]:
                visited[nxt]=True
                queue.append((nxt,cnt+1))
        #print("queue=",queue)
    return 0


# 다른사람코드 wjdtmdgml님

# BFS 큐에서 꺼내는 단어마다 다음에 갈 수 있는 단어 리스트로 반환하는 함수
def compare(compare_word,words): 
    a=list()
    for word in words:
        if sum((1 if a!=b else 0) for a,b in zip(word,compare_word))==1:
            a.append(word)
    return a

def solution2(begin, target, words):

    ch=set([begin])
    dq=deque([(begin,0)])

    if target not in words: return 0 ######### 문제조건 잘 봤어야함

    while dq:
        start,cnt=dq.popleft()
        if start==target:   return cnt
        for word in compare(start,words): # compare BFS 큐에서 꺼내는 단어(start)마다 다음에 갈 수 있는 단어 리스트로 반환
            if word not in ch:
                ch.add(word)
                dq.append([word,cnt+1])
    
    return 0


print("Case1=",solution( "hit", "cog",  ["hot", "dot", "dog", "lot", "log", "cog"]))
print("Case2=",solution( "hit", "cog",  ["hot", "dot", "dog", "lot", "log"]))
print("Case3=",solution( "aaaaaaaaaa", "bbbbbbbbbb",  ["aaaaaaaaab", "aaaaaaaabb", "aaaaaaabbb", "aaaaaabbbb", "aaaaabbbbb", "aaaabbbbbb", "aaabbbbbbb", "aabbbbbbbb", "abbbbbbbbb",
"aaaabaaaaa", "aaaabaaaba", "aaabbaaaab", "babaaabaab", "abbaaaabbb", "bbaabbbbaa", "babaabbbbb", "abbbbbbabb", "babbbbbbbb", "bbabbbbbbb", "bbbabbbbbb"]))
