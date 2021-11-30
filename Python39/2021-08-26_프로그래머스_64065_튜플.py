# 22분.

'''
중복된 원소가 있을 수 있습니다. ex : (2, 3, 1, 2)
원소에 정해진 순서가 있으며, 원소의 순서가 다르면 서로 다른 튜플입니다. ex : (1, 2, 3) ≠ (1, 3, 2)
튜플의 원소 개수는 유한합니다.
'''
def solution(s):
    tuples = list(s.lstrip("{").rstrip("}").split("},{"))
    tuples = sorted(tuples,key=len)
    
    length = len(tuples)
    for i in range(length):
        tuples[i] = list(map(int,tuples[i].split(",")))
    # [['2'], ['2', '1'], ['2', '1', '3'], ['2', '1', '3', '4']]

    answer = []
    for i in range(length):
        for j in range(len(tuples[i])):
            if tuples[i][j] not in answer: # 시간초과날 것 같은데... 
                # No. '전체' s가 100만인거고 return 배열의 길이가 최대 500이니까 1+2+...+500 O(N^2)도 가능함
                answer.append(tuples[i][j])
    
    # s가 표현하는 튜플을 '배열'에 담아 return 
    return answer

# s는 항상 중복되는 원소가 없는 튜플을 올바르게 표현하고 있습니다.
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")) # [2, 1, 3, 4]
print(solution("{{20,111},{111}}")) # [111, 20]
print(solution("{{123}}")) # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")) # [3, 2, 4, 1]