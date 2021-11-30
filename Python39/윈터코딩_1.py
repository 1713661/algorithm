def solution(character, monsters): #플레이어:[체력, 공격력, 방어력] | 몬스터:[이름, 경험치, 체력, 공격력, 방어력]
    
    cand = [] #얻은 경험치
    c0,c1,c2 = map(int,character.split())
    init = c0#플레이어의 처음 체력
    
    for idx,monster in enumerate(monsters):
        time = 0
        monster = monster.split()
        m0 = monster.pop(0)
        m1,m2,m3,m4 = map(int,monster)
        while time<=100:
            time += 1
            #1.플레이어가 몬스터를 공격(플레이어의 공격력 - 몬스터의 방어력)이 0 초과인 경우만)
            if c1-m4>0:  
                m2 -= (c1-m4)

            #2.몬스터의 체력이 0 이하가 되면 몬스터가 죽고, 전투가 종료
            if m2<=0:
                print("monster is dead") 
                cand.append( (m1/time,m1,idx,m0) )
                break

            #3.
            if m3-c2>0:  
                c0 -= (m3-c2)

            #4.
            if c0<=0:
                print("character is dead") 
                break
            #5.
            else:
                c0 = init

    cand = sorted(cand,key=lambda x:(-x[0],-x[1],x[2]) )
    answer = cand[0][3]
    
    return answer

    
    

print(solution("10 5 2",["Knight 3 10 10 3","Wizard 5 10 15 1","Beginner 1 1 15 1"]))