# start(AAA..에서 name이랑 똑같아짐),name말고 check배열도 추가로 선언해야함!!!
######## 내가 지금 뭘 짜고 있는지 항상 생각하고 있어야함

# 시간초과
# 1시간 19분 나 구현력 많이 부족한듯 PS보다는 구현력이 중요하다고 했음 끝까지 풀자!!

# idx,cnt = nextIdx(idx,start,check) # check = [False]*len(name) #[item for item in name] #알파벳바꿨는지확인

def nextIdx(idx,check): # 좀 더 효율적인 코드 없을까...

    tmpL,tmpR = idx,idx
    cntL,cntR = 0,0

    def moveLeft(temp):
        return temp-1 if temp>0 else len(check)-1

    def moveRight(temp):
        return temp+1 if temp<len(check)-1 else 0

    for _ in range(len(check)): ## while True:하면 안돼 생각을 해 생각을
        cntL += 1
        tmpL = moveLeft(tmpL)
        if not check[tmpL]:
            break
    
    for _ in range(len(check)): 
        cntR += 1
        tmpR = moveRight(tmpR)
        if not check[tmpR]:
            break

    if cntL==len(check) or cntR==len(check):
        return -1,-1

    elif cntL>=cntR:
        idx = tmpR
        return idx,cntR

    else:
        idx = tmpL
        return idx,cntL
    
    

def solution(name):

    answer = 0
    cnt = 0 
    idx = 0

    start = 'A'*len(name)
    check = [ False if item!='A' else True for item in name] #알파벳바꿨는지확인 'A'이면 바꿀필요없음
    print("check=",check)

    while start!=name:
    
        difference = abs(ord(name[idx])-ord('A'))   # 괄호조심
        move = min( difference,26-difference )
        print("move=",move,"cnt=",cnt)
        answer += (move+cnt)                        # name 첫글자가 'A'이면 move,cnt 둘 다 0이니까 상관없음

        start = start[:idx]+name[idx]+start[idx+1:] # 한글자씩 바꿔서 최종적으로는 name문자열이랑 같아지도록
        check[idx] = True
        print("start=",start)

        idx,cnt = nextIdx(idx,check)
        print("nextIdx=",idx)

    return answer

print(solution("JEROEN")) #56
print(solution("JAN")) #23
print(solution("JAZ")) #11
print(solution("AABACAAAAAAAA")) #7
print(solution("AABACAAAAAAAD")) #12
print(solution("ZAAAZZZZZZZ")) #15
print(solution("BBAAABAAAAAAAAAAAABA")) #15 아님 -2+3+4+4(B글자수)=13
print(solution("ABABAAAAAAABA")) #10 나는 11나오는데 통과되네 그냥 그때그때 가장 가까운 글자로 가게만 짜도 통과되는듯





