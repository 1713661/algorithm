# 14분 문제이해 문제풀기시작
# 23분 재생시간전처리
# 31분 melody 전처리
# 43분 전처리 완료
# 49분 infos 딕셔너리 형태로 만듦
# 57분 1차제출 테스트케이스4,11번실패
# +14분 못고침..

# 네오가 기억하고 있는 멜로디는 음악 끝부분과 처음 부분이 이어서 재생된 멜로디일 수도 있다
# 한 음악을 중간에 끊을 경우 원본 음악에는 네오가 기억한 멜로디가 들어있다 해도 그 곡이 네오가 들은 곡이 아닐 수도 있다. ??? 이게 무슨말이지 설명보니까이해됐음
# 기억한 멜로디를 재생 시간과 제공된 악보를 직접 보면서 비교

 

# 음악이 00:00를 넘겨서까지 재생되는 일은 없다. ???????


# 네오가 기억한 멜로디를 담은 문자열 m
def solution(m, musicinfos):
    infos = dict()
    change = {
        'C#':'c',
        'D#':'d',
        'F#':'f',
        'G#':'g',
        'A#':'a',
        'E#':'e'
    }
    for (key,value) in change.items(): # 반음을 소문자로 표현
        m = m.replace(key,value)
    # 전처리
    for info in musicinfos:
        start,end,name,melody = info.split(',')
        # start="12:00", end="12:14", name="HELLO", melody="CDEFGAB"
        # 시간범위 00:00~23:59 맞나?
        '''
        제 경우에도 4번, 11번에 틀렸었는데 종료 시간이 00:00일 때 24:00로 변경하는 코드를 빼니까 통과가 되네요?
        틀리는 경우가 시간 계산 관련 경우였든지, 그냥 우연히 맞은건지는 테케가 없으니 불확실 하지만 도움 되었으면 합니다~
        '''
        #if start=="24:00": start="00:00" ################### 얘네 다 빼야함
        #if end=="00:00": end="24:00" ##################
        
        # 그러니까 end도 00:00 일 때 바꿀 필요없는거임!

        startTime,startSecond = start.split(':')
        endTime,endSecond = end.split(':')
        # startTime="12",startSecond="00"
        # endTime="12",endSecond="14"
        time = 60*(int(endTime)-int(startTime))+int(endSecond)-int(startSecond) # 시간을 분으로 환산해야함
        ####### 아 13:50 14:20 인경우 60*1+(-30)이어서 결론적으로는 맞음!
        #print(time) #74,55분

        for (key,value) in change.items(): # 반음을 소문자로 표현
            melody = melody.replace(key,value)
        #print(melody)

        cycle = time//len(melody)
        remain = time%len(melody)
        #print(len(melody),cycle,remain)
        running = ""

        for i in range(cycle):
            running += melody
        
        running += melody[:remain]
        
        # 100개 이하 곡이니까 { running:name } 딕셔너리 형태로 만들어도 될듯
        # running이 같다면???????
        if running in infos: continue # 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
        infos[running] = name
    
    # 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 
    runnings = infos.keys()
    runnings = sorted(runnings, key=len, reverse=True) ################################## 순서 보장해주나?
    print(infos)
    print(runnings) 
    length = len(runnings)
    for i in range(length):
        if m in runnings[i]:
            return infos.get(runnings[i])
    
    return "(None)"


# 시간을 분으로 환산해야함
# #이붙어있는경우주의
# 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다.

'''
print(solution( "ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", 
                            "13:00,13:05,WORLD,ABCDEF"])) #"HELLO"

print(solution( "CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", 
                                     "04:00,04:08,BAR,CC#BCC#BCC#B"])) #"FOO"

print(solution( "ABC", ["12:00,12:14,HELLO,C#DEFGAB", 
                        "13:00,13:05,WORLD,ABCDEF"])) #"WORLD"



print(solution( "ABC", ["00:00,01:14,HELLO,C#DEFGAB", 
                        "23:05,00:00,WORLD,ABCDEF"])) #"WORLD"


print(solution( "ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", 
                            "13:00,13:14,WORLD,ABCDEFG"])) #"HELLO"
'''
# 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다.
# 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
print(solution( "ABC", ["23:10,00:00,HELLO,ABCDE", #time=-1390으로 잘못나옴
                        ])) #"HELLO"