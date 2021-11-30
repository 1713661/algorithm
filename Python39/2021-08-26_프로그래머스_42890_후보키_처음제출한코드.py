# 내가 짠 코드는 column zip했다 튜플 zip했다 왔다리갔다리 해야하는 안좋은 코드

# key_len마다 while문 도는 게 아니라 
# 모든 column에 대한 combies 다 만들고(어차피 column 길이 최대 8이니까 완전탐색해도 됨)
# 그 combies 다 도는 걸로 짜는 게 더 좋음
# 튜플 단위로 zip한 릴레이션을 다시 쪼개고 뭐 이러는 게 아니라
# combies 완전 탐색할 때마다 r[idx] 가져와서 튜플 단위로 zip하는 게 나음
# 하... 나는 언제쯤 안 헤매고 알고리즘 짤까

from itertools import combinations

def solution(relation):
    answer = 0
    attr_list = list(zip(*relation))
    keyLen = 1

    while True: 
        
        isNotUniqAttr_list = []

        for i in range(len(attr_list)):
            if len(set(attr_list[i]))==len(attr_list[i]):
                answer += 1
            else: ### 여기서부터 심상치 않음...
                # isNotUniqAttr_list에 넣은 애들은 튜플 단위로 묶어준 애들이기 때문에 다시 column으로 zip하고 완전 비효율적인 코드...
                isNotUniqAttr_list.append(attr_list[i]) 

        ### 오우 여기는 완전 최악
        if len(isNotUniqAttr_list)<=keyLen: break

        keyLen += 1
        attr_list = []
        for attr in combinations(isNotUniqAttr_list,keyLen):
            attr_list.append(tuple(zip(*attr)))
    
    return answer

print(solution([ # 2(후보 키의 개수)
    ["100","ryan","music","2"],
    ["200","apeach","math","2"],
    ["300","tube","computer","3"],
    ["400","con","computer","4"],
    ["500","muzi","music","3"],
    ["600","apeach","music","2"]
]))
