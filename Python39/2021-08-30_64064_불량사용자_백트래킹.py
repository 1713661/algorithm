def solution(user_id_list, banned_id_list):
    cand_list = [[] for _ in range(len(banned_id_list))]
    for user_id in user_id_list:
        isBanned = True
        for i in range(len(banned_id_list)):
            if len(user_id)!= len(banned_id_list[i]): continue
            for j in range(len(user_id)):
                if banned_id_list[i][j]=="*": continue
                elif user_id[j]!=banned_id_list[i][j]:
                    isBanned = False
            if isBanned:
                cand_list[i].append(user_id)
            isBanned = True #초기화
        
    tmp_list = []

    def dfs(li,idx):

        if idx==(len(cand_list)-1):
            tmp_list.append(li[:]) ##### 복사본 넣어야함(li는 레퍼런스니까)
            # tmp_list.append(li) 하면 밑에 for문에서 li.remove(nxt)한것땜에 처음원소만 남음
            # idx끝까지 와서 li 넣어줬어도 결국엔 [cand_list[0][i]]만 남는거임(li는 레퍼런스니까!!!!)(생각을해생각을)
            # 참고) 33번째줄 for문 때문에 처음 li는 li = [cand_list[0][i]] 로 각각 따로 들어감
            return
            
        for nxt in cand_list[idx+1]:
            if nxt not in li:
                li.append(nxt)
                dfs(li,idx+1) 
                ### 트리구조로 생각하면 li.remove(nxt) 왜 해야 하는지 더 쉽게 이해할 수 있음
                li.remove(nxt) ### 백트래킹


    for i in range(len(cand_list[0])):
        dfs([cand_list[0][i]],0)
        
    print(tmp_list)
    tmp_list = list(set(item) for item in tmp_list)
    print(tmp_list)
    answer_list = []
    answer_list.append(tmp_list[0])
    for item in tmp_list[1:]:
        if item not in answer_list:
            answer_list.append(item)

    return len(answer_list)
    
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"])) # 2
print("terminal=",solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])) # 3