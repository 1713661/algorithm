# 아무리 생각해도 런타임에러 왜 나는지 모르겠음.. 인덱스 범위 벗어나는 일 없을 것 같은데ㅔㅔㅔㅔㅔ
# 1시간15분(런타임에러) from itertools import combinations 빼먹었기 때문!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! (실전에서만 안그러면 됨)
# 정확성 테스트 : 10초니까 완전탐색해도 되지않을까??
from itertools import combinations

def solution(places):

    # for place in places:
    # for string in places[i]:
    # for s in string: enumerate쓰는것도 꼭 구현해보기!!!!

    for place in range(5):                      # row 구해야 하니까 리스트로 변환해야함
        for column in range(5):      
            places[place][column] = list(places[place][column])
    
    '''
    for k in range(5):
        for i in range(5):
            print(places[k][i])
        print("\n")
    '''
    
    people_list = [[] for _ in range(len(places))] # 사람 좌표(x,y) 저장할 배열
    for place in range(5):
        for column in range(5):    
            for row in range(5):  
                if places[place][column][row]=='P':
                    people_list[place].append((column,row))
    #print(people_list)

    answer = [1,1,1,1,1]
    for place in range(5):
        #print(place, list(combinations(people_list[place],2)))

        if len(people_list[place])<2: continue # 굳이 없어도 되는 코드일듯

        for (x1,y1),(x2,y2) in combinations(people_list[place],2): # combinations 리스트로 묶을 필요없음
            if abs(x1-x2)+abs(y1-y2)==1: #맨하튼거리가 1인 경우 무조건 방역수칙위반
                print("place=",place,"x1=",x1,"y1=",y1,"x2=",x2,"y2=",y2)
                answer[place]=0
                break
            elif abs(x1-x2)+abs(y1-y2)==2: #y_smaller 구할 필요없음(이런거시간낭비하지말자)(combinations로 구했으니까)
                if x1==x2 and places[place][x1][y1+1]=='O': # 같은 행이고 그 사이가 빈칸인 경우 ##여기서 배열참조에러난건가? 근데 인덱스범위벗어나는코드인가?
                    print("X=",places[place][x1][y1+1])
                    print("place=",place,"x1=",x1,"y1=",y1,"x2=",x2,"y2=",y2)
                    answer[place]=0
                    break
                elif y1==y2 and places[place][x1+1][y1]=='O': # 같은 열이고 그 사이가 빈칸인 경우
                    print("place=",place,"x1=",x1,"y1=",y1,"x2=",x2,"y2=",y2)
                    answer[place]=0
                    break
                elif places[place][x2][y1]=='O' or places[place][x1][y2]=='O':
                    print("Hi")  
                    print("place=",place,"x1=",x1,"y1=",y1,"x2=",x2,"y2=",y2)
                    answer[place]=0      
                    break                                                              

    return answer


        

    

print(solution([
    ["POOOP", 
     "OXXOX",
     "OPXPX",
     "OOXOX", 
     "POXXP"], 

    ["POOPX", 
     "OXPXP", 
     "PXXXO", 
     "OXXXO", 
     "OOOPP"], 

    ["PXOPX",
     "OXOXP", 
     "OXPOX", 
     "OXXOP", 
     "PXPOX"], 

    ["OOOXX", 
     "XOOOX", 
     "OOOXX", 
     "OXOOX", 
     "OOOOO"], 

     ["PXOOO", "OOOOO", "PXOOO", "OOOOO", "OOOPO"]]))