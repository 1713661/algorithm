# 후위 순회는 재귀함수가 go를 호출이 끝날때의 tree부터 탐색하는것이기때문에 이후에 append를 시켜준다.
# 그렇게 되면 제일 깊숙한 애가 먼저 append 되기 때문(거꾸로 추가) (생각을 해 생각을)
import sys
sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self,data_list,original_list):
        self.data = max(data_list, key=lambda x:x[1])
        self.idx = original_list.index(self.data)+1
    
        left = list(filter(lambda x: x[0]<self.data[0],data_list))
        right = list(filter(lambda x: x[0]>self.data[0],data_list))

        if left!=[]:
            self.left = Tree(left,original_list) ##### Tree객체 만들어야함!!!!!!!!!!
        else:
            self.left = None

        if right!=[]:
            self.right = Tree(right,original_list)
        else:
            self.right = None

def go(tree,pre,post):
    pre.append(tree.idx)
    
    if tree.left:
        go(tree.left,pre,post)
    if tree.right:
        go(tree.right,pre,post)

    post.append(tree.idx) # 왼 -> 오 -> 부모 순으로
    
    
def solution(treeinfo):
    pre = []
    post = []
    tree = Tree(treeinfo,treeinfo)

    go(tree,pre,post)

    return [pre,post]

print(solution(
    [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
))
# result = [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]