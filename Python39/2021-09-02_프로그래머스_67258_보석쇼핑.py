# 31분 start 인덱스 앞으로 한칸 옮긴다고 집합에서 바로 빼버리면 안됨
# 42분 첫 제출 -> 효율성 시간초과 -> 그때그때 set하지말고 딕셔너리 써야!

# 다른사람코드보기(딕셔너리 써야함)
# 13분

def solution(gems): #1<= <=100000
    start,end = 0,0
    length = len(gems)
    kind = len(set(gems)) #보석종류의 수
    answer = []
    
    check = { gems[start]:1 }
    
    while end<length: 
        
        if len(check)==kind:
            answer.append([start+1,end+1])
     
            if check[gems[start]]==1:
                del check[gems[start]]
            else:
                check[gems[start]] = check.get(gems[start])-1
            start += 1
        else:
            if end==length-1: break
            end += 1
            if gems[end] in check:
                check[gems[end]] = check.get(gems[end])+1
            else:
                check[gems[end]]=1
    
    answer = sorted(answer,key=lambda x:(x[1]-x[0],x[0]))
    return answer[0]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# [3, 7]    gems_set= {'EMERALD', 'SAPPHIRE', 'DIA', 'RUBY'}

print(solution(["AA", "AB", "AC", "AA", "AC"]))
# [1, 3]    gems_set= {'AC', 'AA', 'AB'}

print(solution(["XYZ", "XYZ", "XYZ"]))
# [1, 1]    gems_set= {'XYZ'}

print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
# [1, 5]    gems_set= {'YYY', 'ZZZ', 'NNNN', 'BBB'}