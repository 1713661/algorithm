# 추석 트래픽은 일정시간동안의 트래픽 '개수'만 세는 거니까 
# startTime,endTime만 구했었지만,
# 얘는 누적재생시간 계산해야하니까 초당 사용자수 배열에 저장하는 게 좋을듯 
# 10분 문제읽고 알고리즘구상
# 27분  users_per_second 만들기(배열 길어서 다 출력은안되는듯)
# 37분 endTime에 -1하기!!!!!!!!
# 58분 누적합은 우선 sum(d[:adv_s]) 구한다음에 거기서 앞쪽 빼주고 뒤쪽 더해주는방식으로 구하기
######### 특정 초에 시청중인 사용자의 수 계산 +1은 비효율적(logs배열 최대 30만개니까)
######### users_per_second[sec] += users_per_second[sec-1] 이용 (사용자 수 증감하는 타이밍을 반영할 수 있음)
def timeToSecond(timestring):
    timelist = timestring.split(":")
    second = int(timelist[0])*3600+int(timelist[1])*60+int(timelist[2])
    return second

def solution(play_time, adv_time, logs):
    # 100시간 초단위 -> 최대 360000개(가능한 숫자)
    play_second = timeToSecond(play_time)
    users_per_second = [0 for _ in range(play_second+1)] #+1할말??

    # logs_sec = [] # 30만개 #[[4815, 6314], [2431, 3600], [1550, 2909], [5459, 6809], [5864, 7350]]
    for log in logs:
        log = log.split("-")
        users_per_second[timeToSecond(log[0])] += 1
        users_per_second[timeToSecond(log[1])] -= 1

    # 특정 초에 시청중인 사용자의 수 계산(누적합아님!!!!!) +1은 비효율적(logs배열 최대 30만개니까)
    for sec in range(1,play_second):
        users_per_second[sec] += users_per_second[sec-1]

    adv_second = timeToSecond(adv_time) # 광고시간(초단위)
    MAX = sum(users_per_second[:adv_second]) # 간격 adv_second인 배열의 원소들의 합
    cur_MAX = MAX
    answer = 0
    for start in range(1,play_second+1-adv_second):
        cur_MAX = cur_MAX - users_per_second[start-1] + users_per_second[start-1+adv_second] # 간격 adv_second니까 start-1에 걔만더하면됨
        if cur_MAX>MAX: # 누적시간 같을때는 값 바뀌지 않음(제일 앞 start를 답으로 출력할 수 있음)
            MAX = cur_MAX
            answer = start
    # return "{0:0>2}".format(str(answer//3600))+":"+"{0:0>2}".format(str((answer%3600)//60))+":"+"{0:0>2}".format(str((answer%3600)%60))
    # format함수대신 f 문자열 포맷팅사용
    return f"{answer//3600:02d}:{answer%3600//60:02d}:{answer%60:02d}"

print(solution("02:03:55", "00:14:15", [ # 동영상재생시간, 공익광고재생시간
    "01:20:15-01:45:14", 
    "00:40:31-01:00:00", 
    "00:25:50-00:48:29", 
    "01:30:59-01:53:29", 
    "01:37:44-02:02:30"
    ])) #"01:30:59"