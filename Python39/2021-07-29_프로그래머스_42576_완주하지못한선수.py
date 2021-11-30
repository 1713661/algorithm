def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append("-")
    length = len(participant)
    for i in range(length):
        if participant[i]!=completion[i]:
            return participant[i]

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))