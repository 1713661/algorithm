def solution(dartResult):
    import re
    scores = re.findall('(\d+)([SDT])([*#]?)',dartResult)
    ##### 그룹핑!!!!
    print(scores)
    # [('1', 'S', ''), ('2', 'D', '*'), ('3', 'T', '')]

print(solution("1S2D*3T"))
# 37
print(solution("1D2S#10S"))
# 9
print(solution("1S*2T*3S"))
# 23
