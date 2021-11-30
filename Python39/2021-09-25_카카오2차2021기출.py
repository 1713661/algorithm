import requests#,json
from pprint import pprint

### request parameter type 잘보기!!!!!!!!!!!
### 변수명 명시 모듈 뭐였지???? 파이썬 알고리즘 인터뷰 책 참고 (근데 안써봤으면 실전에서도 안쓰는 게 나을듯)

def start(url,token,problem):
    uri = url+"/start"
    return requests.post(uri, headers = {"X-Auth-Token" : token, 'Content-Type': "application/json"}, params = {"problem": problem}) #################.json()
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
                        data = {"commands": commands}).json()
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
start_ret = start(url,token,1) # 다시 같은 시나리오를 Simulate 하고 싶다면 Start API를 이용해 새로운 AUTH_KEY를 발급받아야 한다.
print(start_ret.json(),start_ret.status_code)
