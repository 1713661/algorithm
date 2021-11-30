# 21분 트라이써야하나? -> 이진탐색쓰면된다고 함
# 30분 sorted key여러개쓰는경우 괄호 꼭 써야함!!!
# 47분 숲을 안보고 급하게 나무만 보니까 오히려 시간 오래걸리는듯. 밤이어서 집중력 떨어지기도 하고..
# + 12분 글자수 다른 애들 어떻게 거르지 -> 길이별로 배열 다르게 저장해야함(2차원배열!!)(이런거생각하는능력키워야할텐데)

# + 52분 이코테 알고리즘 풀이 참고해서 다시 품

from bisect import bisect_left,bisect_right

# 삽입하면 다음 쿼리에도 영향을 미치기 때문에 안됨. 그리고 굳이 삽입할필요없음(생각을해생각을) 
def count_by_range(list,l_value,r_value): 
    l_idx = bisect_left(list,l_value)
    r_idx = bisect_right(list,r_value)
    return r_idx-l_idx

# 그때그때 필요한 리스트만 정렬하는 것보다 한번에 정렬하는 게 좋음(생각을 해 생각을)
def solution(words, queries):

    # 전처리

    # 1<=각 가사 단어의 길이<=10,000
    pre_sorted = [ [] for _ in range(10001)]    # 길이별로나눠저장(접두사 기준으로)
    post_sorted = [ [] for _ in range(10001)]   # 접미사 기준으로 

    #2<=단어개수<=100,000
    for word in words: 
        pre_sorted[len(word)].append(word)
        post_sorted[len(word)].append(word[::-1]) ######### 각 단어 뒤집어서 저장(bisect때문에)
        
    for i in range(1,10001):
        pre_sorted[i].sort()
        post_sorted[i].sort()
    
    # 쿼리
    answer = []
    for query in queries:
        
        #???XX(역순)
        if query[0]=='?': 
            query = query[::-1]
            res = count_by_range(post_sorted[len(query)],query.replace('?','a'),query.replace('?','z'))
        
        #XX???
        else:              
            res = count_by_range(pre_sorted[len(query)],query.replace('?','a'),query.replace('?','z'))
        answer.append(res)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], #words 중복없음
["fro??", "????o", "fr???", "fro???", "pro?"])) #중복가능 #queries의 길이(검색 키워드 개수)는 2 이상 100,000
# [3, 2, 4, 1, 0]