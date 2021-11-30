# zip함수는 여기서 쓸 수 없을듯?
# 22분 구현력이 이렇게 떨어지다니... 현타
# 글구 내가 짠 코드는 예외사항이 너무 많은듯
# 2048이랑 비슷한느낌?

# n개씩 자르는거기 때문에(압축할 문자열 길이 다 일정) 난이도가 그렇게 높지 않았음

def solution(s):
    
    l = len(s)
    MIN = len(s)
    for step in range(1,l):
    
        s_list = [ s[start:start+step] for start in range(0,l,step) ]
        new_s_list = [] #반복되는원소들저장할배열
        new_s_list.append(s_list[0])
    
        cnt = 1

        for i in range(1,len(s_list)):
            if s_list[i]==new_s_list[-1]: #마지막원소와같으면
                cnt += 1
            else:
                if cnt>1: new_s_list.insert(-1,str(cnt)) ############# 0부터시작
                new_s_list.append(s_list[i])
                cnt = 1 #초기화
        if cnt>1: new_s_list.insert(-1,str(cnt))
    
        new_s = ''.join(new_s_list) #join(문자열,리스트,튜플) 다 가능!!
        MIN = min(MIN,len(new_s))

    return MIN
    
print(solution("aabbaccc")) # 7
print(solution("ababcdcdababcdcd")) # 9
print(solution("abcabcdede")) # 8
print(solution("abcabcabcabcdededededede")) # 14
print(solution("xababcdcdababcdcd")) # 17



    