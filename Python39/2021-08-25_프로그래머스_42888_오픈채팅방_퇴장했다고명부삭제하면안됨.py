# 30분 + 10분 고치기
def solution(record):
    users = dict() # 현재 채팅방에 있는 사용자의 (아이디,닉네임)을 저장할 딕셔너리 
    cmds = [] # record

    # 최종 명부 만들기(퇴장했다고 명부에서 삭제하면 안됨. 이따 기록의 닉네임 바꿀때 필요하기 때문)
    for cmd in record:
        cmd = cmd.split()
        cmds.append(cmd)
        if cmd[0]=="Leave": continue 
        users[cmd[1]] = cmd[2]

    answer = []
    for cmd in cmds:
        if cmd[0]=="Enter":
            answer.append(users[cmd[1]]+"님이 들어왔습니다.")
        elif cmd[0]=="Leave":
            answer.append(users[cmd[1]]+"님이 나갔습니다.")
    
    return answer

print(solution([
    "Enter uid1234 Muzi", 
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"
    ] ))