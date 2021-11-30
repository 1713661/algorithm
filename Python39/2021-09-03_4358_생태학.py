import sys
input = sys.stdin.readline

species = dict()
while True:
    tree = input().rstrip()
    if not tree: break
    if tree in species:
        species[tree] += 1
    else:
        species[tree] = 1

l = sum(species.values()) # 총 나무의 개수
li = sorted(species.items(), key = lambda x: x[0]) # 각 종의 이름을 사전순으로 정렬(리스트)

for tree,n in li:
    print(tree,"%.4f"%(n/l*100))

'''
li = sorted(species, key = lambda x: x[0]) # 각 종의 이름을 사전순으로 정렬(리스트)

['Ash', 'Aspen', 'Basswood', 'Beech', 'Black Walnut', 'Cherry', 'Cottonwoodt', 'Cherry', 'Cottonwood', 'Cypress', 'Gum', 'Hac Maple', 'Pecan', 'Poplankberry', 'Hickory', 'Hard Maple', 'Pecan', 'Poplan, 'Sassafras', 'Sycamore'', 'Red Alder', 'Red Elm', 'Red Oak', 'Soft Maple', 'Sassafras', 'Sycamore', 'White Oak', 'Willow', h', 1), ('Black Walnut', 
'Yellow Birch'] 

li2 = sorted(species.items(), key = lambda x: x[0])

[('Ash', 4), ('Aspen', 1), ('Basswood', 1), ('Beecn', 1), ('Poplan', 1), ('h', 1), ('Black Walnut', 1), ('Cherry', 1), ('CottSassafras', 1), ('Soft Maonwood', 1), ('Cypress', 1), ('Gum', 1), ('Hackberlow', 1), ('Yellow Birch'ry', 1), ('Hard Maple', 1), ('Hickory', 1), ('Pecan', 1), ('Poplan', 1), ('Red Alder', 1), ('Red Elmthon39>', 1), ('Red Oak', 2), ('Sassafras', 1), ('Soft Maple', 1), ('Sycamore', 1), ('White Oak', 3), ('Willow', 1), ('Yellow Birch', 1)]
'''



