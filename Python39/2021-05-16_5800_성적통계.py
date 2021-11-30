import sys
input = sys.stdin.readline

for i in range(int(input())):
    scores = list(map(int, input().split()))
    num = scores.pop(0)
    scores.sort()
    gap = []
    for j in range(num-1):
        gap.append(scores[j+1]-scores[j])
    print("Class %d" %(i+1))
    print("Max {0}, Min {1}, Largest gap {2}".format(scores[-1], scores[0], max(gap)))
