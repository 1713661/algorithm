# 진짜 이것도 한번에 못짜는 내가 싫다..
# 이 문제에서는 split 안쓰는 게 맞는 것 같다.
# replace 써야한다!!!
# 7분

def solution(string):

    change = {
        'zero':'0',
        'one':'1', 
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }

    for key,value in change.items():
        string = string.replace(key,value)

    return int(string)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))
