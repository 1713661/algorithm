import sys
sys.setrecursionlimit(10**6)

# https://bladejun.tistory.com/155

# 왼쪽 자식들은 left(리스트)에, 오른쪽 자식들은 right(리스트)에 저장
class Tree:
    def __init__(self, data_list, org_data_list):
        # 두번째 좌표의 가장 큰 값을 찾는다.(두번째값을 기준으로 노드가 계속해서 분리되기 때문이다)
        # self.data = [x,y]
        self.data = max(data_list, key=lambda x :x[1])
        
        # 나중에 node번호를 넣어주기 위한 index
        self.idx = org_data_list.index(self.data) + 1
        
        # 첫번째 좌표값을 기준으로 작으면 왼쪽 크면 오른쪽 
        left = list(filter(lambda x :x[0] < self.data[0], data_list))
        right = list(filter(lambda x :x[0] > self.data[0], data_list))
    	
        # left의 값이 있다면 계속해서 노드가 구성되게 만들어준다
        if left != []:
            self.left = Tree(left, org_data_list)
        else:
            self.left = None
        
        # right의 값이 있다면 계속해서 노드가 구성되게 만들어준다
        if right != []:
            self.right = Tree(right, org_data_list)
        else:
            self.right = None

def go(tree, pre, post):
    # 전위 순회는 위에서부터 내려오는것이기 때문에 재귀함수 go를 호출할때마다 append를 시켜준다.
    pre.append(tree.idx) 
    
    if tree.left != None:
        go(tree.left, pre, post)
        
    if tree.right != None:
        go(tree.right, pre, post)
    
    # 후위 순회는 재귀함수가 go를 호출이 끝날때의 node부터 탐색하는것이기때문에 이후에 append를 시켜준다.
    ##### 좀 더 이해해야 할듯
    post.append(tree.idx)
    
def solution(nodeinfo):
    tree = Tree(nodeinfo, nodeinfo) # '각각의 노드에 대하여' 왼쪽자식들, 오른쪽자식들을 리스트에 담아 tree.left 등으로 접근가능 
    
    pre = []
    post = []
    
    go(tree, pre, post)
    
    return [pre, post]

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
# [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]6