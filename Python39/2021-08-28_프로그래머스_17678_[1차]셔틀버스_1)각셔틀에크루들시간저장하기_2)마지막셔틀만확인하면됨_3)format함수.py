################# 단, 콘은 게으르기 때문에 같은 시각에 도착한 크루 중 대기열에서 제일 뒤에 선다.

# 24분 거의다 짰는데 문제이해가 잘 안됨
# 셔틀은 오전 9시부터 운영한댔는데 answer에 어떻게 "08:59","00:00"가 올 수 있는거지? 아 제일 늦게 정류장에 올 수 있는시간
# 35분 첫 제출 기대 -> 컴파일에러
####### capacity(비어있는 자리 개수) 대신 crewsInShuttle(현재탄크루들이 정류장에 온 시간들의 리스트)로 만들어야함
###### 마지막 셔틀만 확인하면 됨
###### format함수는 기본함수니까 쓸 줄 알아야!!!


# 셔틀 운행 횟수 n, 셔틀 운행 간격 t분, 한 셔틀에 탈 수 있는 최대 크루 수 m, 크루가 대기열에 도착하는 시각을 모은 배열 timetable
def solution(n, t, m, timetable):
    shuttleStartSecond = 540
    shuttleSeconds = [shuttleStartSecond+t*i for i in range(n)] # 셔틀시간을 초단위로 저장

    timetableSeconds = [] #timetable의 시간을 초단위로 바꿔 저장할 배열

    timetable.sort() ##### 정렬해야함
    for crew in timetable:
        crew = crew.split(":") #["23":"59"]
        crewSecond = 60*int(crew[0])+int(crew[1])
        timetableSeconds.append(crewSecond)

    crewsInShuttle = [[] for _ in range(n)] # 각 셔틀에탄 크루들의 시간들을 리스트로 저장

    idx = 0
    # 몇번 셔틀에 타는지 저장
    for time in timetableSeconds: 
        for i in range(idx,n): 
            ### 여기 있는 두 if문은  crewsInShuttle[i].append(time) 전에 걸러낸다는 생각으로...
            if time>shuttleSeconds[i]: 
                continue
            if len(crewsInShuttle[i])==m:
                idx += 1
                continue
            crewsInShuttle[i].append(time)
            break       

    answerSecond = 0
    ###### 마지막 셔틀만 확인하면 됨
    if len(crewsInShuttle[n-1])<m:
        answerSecond = shuttleSeconds[n-1]
    
    # 마지막 셔틀이 꽉차있는 경우도 마지막애보다 1분만 앞서면 되니까
    elif len(crewsInShuttle[n-1])==m:
        answerSecond = crewsInShuttle[n-1][-1]-1

    print("answer=",answerSecond)
    return "{0:0>2}".format(str(answerSecond//60))+":"+"{0:0>2}".format(str(answerSecond%60))
    
print(solution(10, 60, 10, ["17:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
# 셔틀 운행 횟수 n, 셔틀 운행 간격 t분, 한 셔틀에 탈 수 있는 최대 크루 수 m, 크루가 대기열에 도착하는 시각을 모은 배열 timetable
print(solution( 1, 1, 5, ["08:00", "08:01", "08:02", "08:03"])) # "09:00"
print(solution( 2, 10, 2, ["09:10", "09:09", "08:00"])) #"09:09"
print(solution( 2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])) #"08:59"

'''
print(solution( 10, 60,	45,	
    ["23:59","23:59", "23:59", "23:59", "23:59", 
     "23:59", "23:59", "23:59", "23:59", "23:59", 
     "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]	)) #"18:00"
''' 