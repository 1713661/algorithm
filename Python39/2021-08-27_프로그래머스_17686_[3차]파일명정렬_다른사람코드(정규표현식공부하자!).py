import re
# 먼저 NUMBER을 정렬한 다음에 HEAD를 정렬해야함(생각을 해 생각을)(sorted함수 따로 쓰니까)
# key에 여러 기준 한번에 주는 경우는 원래대로 HEAD 먼저 NUMBER 나중 정렬(HEAD가 같은경우 NUMBER순으로 보정해주기 때문에)
def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0])) 
    # 각 file에서 처음 나오는(findall()함수는 리스트 리턴하기 때문에 뒤에 [0] 붙인거임) 5자리까지의 숫자순으로 정렬
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    # 숫자를 기준으로 split한 애들 중 첫번째 원소(HEAD)를 대소문자 구분없이(.lower()함수 씀) 정렬
    return b