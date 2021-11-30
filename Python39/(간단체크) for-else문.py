l1 = []
l2 = [1,2,3,4]

print("case 1")
for l in l1:
    if l==0:
        print(l, end=' ')
        break
else:
    print("for-else sentence is available for empty list")

print("case 2")
for l in l2:
    if l==0:
        print(l, end=' ')
        break
else:
    print("for-else sentence is available for non-empty list")

