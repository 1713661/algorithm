# 최소성 테스트에서 내가 생각하지 못한 뭔가가 있는듯...

from itertools import combinations

def solution(relation):
    r = [tuple(each) for each in zip(*relation)]
    combies = [set(combi) for i in range(len(r)) for combi in combinations(range(len(r)), i+1)]
    '''
    combies = [{0}, {1}, {2}, {3}, {0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 3}, {2, 3}, {0, 1, 2}, {0, 1, 3}, {0, 2, 3}, {1, 2, 3}, {0, 1, 2, 3}]
    '''
    # column에 대하여 combinations 만들면 cost 큼
    
    candidate_keys = []

    for combi in combies:
        elements = [r[index] for index in combi]
        zip_elements = list(zip(*elements))
        if len(zip_elements) != len(set(zip_elements)): # 유일성 테스트(나랑 다르게 접근했음. 이분은 스테이지 통과하는 것처럼 짬)
            continue
        for candidate_key in candidate_keys: #최소성 테스트
            if candidate_key.intersection(combi) == candidate_key: ####### 내가 생각 못한 코드
                break
        else: ######### 이부분 잘 이해안됨 indent 틀린건지..
            candidate_keys.append(combi)
            
    return len(candidate_keys)



print(solution([ # 2(후보 키의 개수)
    ["100","ryan","music","2"],
    ["200","apeach","math","2"],
    ["300","tube","computer","3"],
    ["400","con","computer","4"],
    ["500","muzi","music","3"],
    ["600","apeach","music","2"]
]))
