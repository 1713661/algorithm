import requests
INF = int(10e8)
MEAN = 2

### request parameter type 잘보기!!!!!!!!!!!
### 변수명 명시 모듈 뭐였지???? 파이썬 알고리즘 인터뷰 책 참고 (근데 안써봤으면 실전에서도 안쓰는 게 나을듯)

def start(token,problem):
    uri = url+"/start"
    return requests.post(uri, headers = {"X-Auth-Token" : token, 'Content-Type': "application/json"}, params = {"problem": problem}).json()
    ################ -d 옵션 data 말고 params 써야함!!!!!! 이런식으로 안맞는 거 있으면 빨리 다른 parameter 찾아서 바꿔봐야함!!!!
'''
{
  "auth_key": "1fd74321-d314-4885-b5ae-3e72126e75cc",
  "problem": 1,
  "time": 0
}
'''

def locations(key): # 현재 카카오 T 바이크 서비스 시각에 각 자전거 대여소가 보유한 자전거 수를 반환
    uri = url+"/locations"
    return requests.get(uri, headers={"Authorization" : key, 'Content-Type' : 'application/json'}).json()
'''
{
  "locations": [
    { "id": 0, "located_bikes_count": 3 },
    { "id": 1, "located_bikes_count": 3 },
    ...
  ]
}
'''

def trucks(key): # 현재 카카오 T 바이크 서비스 시각에 각 트럭의 위치와 싣고 있는 자전거 수
    uri = url+"/trucks"
    return requests.get(uri, headers={"Authorization" : key, 'Content-Type' : 'application/json'}).json()
'''
{
    "trucks": [
        { "id": 0, "location_id": 0, "loaded_bikes_count": 0 },
        { "id": 1, "location_id": 0, "loaded_bikes_count": 0 },
        ...
    ]
}
'''

def simulate(key,commands): # 현재 시각 ~ 현재 시각 + 1분 까지 각 트럭이 행할 명령을 담아 서버에 전달
    return requests.put(url+"/simulate",
                        headers = {"Authorization" : key, 'Content-Type' : 'application/json'},
                        params = {"commands": commands}).json()
'''
{
  "status": "ready",
  "time": 1,
  "failed_requests_count": 5,
  "distance": 1.2,
}
'''
def score(key):
    return requests.get(url+"/score", 
                        headers={"Authorization" : key, 'Content-Type' : 'application/json'}).json()
'''
{
  "score": 75.7
}
'''
url = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
token = "ff25fc9e3ff0f8653e7999a0bb3df761"
start_ret = start(token,1) # 다시 같은 시나리오를 Simulate 하고 싶다면 Start API를 이용해 새로운 AUTH_KEY를 발급받아야 한다.
auth_key = start_ret["auth_key"]


for time in range(1): ################
    locations_ret = locations(auth_key)["locations"] # 현재 시각에 각 자전거 대여소가 보유한 자전거 수를 반환
    #print(locations_ret,type(locations_ret)) 
    '''
        [
            { "id": 0, "located_bikes_count": 3 },
            { "id": 1, "located_bikes_count": 3 },
            ...
        ]
    '''
    '''
    for location_dict in locations_ret:
        print(location_dict,type(location_dict)) #########3딕셔너리
    '''
    #locations_ret_reverse = {v:k for k,v in locations_ret.items()} #바이크 수 중복될 수 있으니 역으로 저장하는거 안될걸?
    
    # 오버헤드 너무 큰가?
    least = INF
    least_ids = [] # 현재 시각 바이크가 가장 적은 대여소의 id(배열)
    for location in locations_ret:
        if least>location["located_bikes_count"]:
            least = location["located_bikes_count"]

    if least < MEAN:
        for location in locations_ret: 
            if location["located_bikes_count"]==least:
                least_ids.append(location["id"])
    
    trucks_ret = trucks(auth_key) # 현재 시각에 각 트럭의 위치와 싣고 있는 자전거 수
    '''
    {
        "trucks": [
            { "id": 0, "location_id": 0, "loaded_bikes_count": 0 },
            { "id": 1, "location_id": 0, "loaded_bikes_count": 0 },
            ...
        ]
    }
    '''

    for truck_id in range(5): #시나리오1=트럭5개
        print(truck_id)
    commands = [{ "truck_id": 0, "command": [2, 5, 4, 1, 6] }, #########
                    ...]
    simulate_ret = simulate(auth_key,commands) # 현재 시각 ~ 현재 시각 + 1분 까지 각 트럭이 행할 명령을 담아 서버에 전달
    # 서버의 처리 순서 : 반납건 -> 요청건 (-> 요청 취소수 증가 -> 5번)-> 트럭운행(명령수행) -> 현재시각1분증가
    # 5. 자전거 대여 요청이 성공할 경우 현재 시각 + 대여 시간(=반납예정시간?????????) 을 key, 반납할 자전거 대여소 ID 를 value로 하여 returns 에 저장한다.

score_ret = score(auth_key)
print(score_ret)

'''
# 사용자의 요청 [대여할 대여소 ID, 반납할 대여소 ID, 자전거를 탈 시간(분 단위)]
10시 00분: [[3, 0, 10]]
10시 01분: [[1, 3, 1], [1, 4, 15]]
10시 02분: [[0, 3, 2], [3, 1, 4], [0, 3, 1]]
10시 03분: [[1, 3, 5]]
'''