# 30분 와 딴사람 코드보고 풀었는데도 이정도 걸림

from itertools import combinations

def solution(relation):
    # columns를 idx_combi로 '그때그때' 참조하기
    columns = list(map(tuple,zip(*relation)))
    '''
    columns = [
        ('100', '200', '300', '400', '500', '600'), 
        ('ryan', 'apeach', 'tube', 'con', 'muzi', 'apeach'), 
        ('music', 'math', 'computer', 'computer', 'music', 'music'), 
        ('2', '2', '3', '4', '3', '2')
    ]'''
    '''
    idx_combinations = [ set(combi) for combi in combinations([num for num in range(len(columns))],i+1 for i in range(len(columns))) ]
    idx_combinations = [ set(combi) for combi in combinations([num for num in range(len(columns))],i+1) for i in range(len(columns))]
    이렇게 쓰면 틀림 why???? 파이썬 문법 공부부터
    '''
    # 이따 intersection연산 쓰기 위해서 set을 씀
    idx_combinations = [ set(combi) for i in range(len(columns)) for combi in combinations([num for num in range(len(columns))]2,i+1)]
    '''[
        {0}, {1}, {2}, {3}, 
        {0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 3}, {2, 3}, 
        {0, 1, 2}, {0, 1, 3}, {0, 2, 3}, {1, 2, 3}, {0, 1, 2, 3}]
    '''
    keys = []
    for idx_set in idx_combinations:
        tuples = list(zip(*[columns[idx] for idx in idx_set])) 
        # 원소 1개면 뒤에 쉼표 붙는데 딱히 상관없는듯 (1)보단 (1,)인 게 튜플인지 알아보기 쉬우니까 그냥 이렇게 쓰는듯?
        #print(tuples)
        ''' [
            ('100', 'music'), 
            ('200', 'math'), 
            ('300', 'computer'), 
            ('400', 'computer'), 
            ('500', 'music'), 
            ('600', 'music')
        ]'''

        if len(set(tuples))!=len(tuples):   # 유일성 테스트
            continue

        check_minimality = True
        for key in keys:                    # 최소성 테스트
            if key.intersection(idx_set)==key:
                check_minimality = False
                break

        if check_minimality:   
            keys.append(idx_set)

    return len(keys)

print(solution([ # 2(후보 키의 개수)
    ["100","ryan","music","2"],
    ["200","apeach","math","2"],
    ["300","tube","computer","3"],
    ["400","con","computer","4"],
    ["500","muzi","music","3"],
    ["600","apeach","music","2"]
]))
