# info 0:양 1:늑대
# 

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def solution(info, edges):
    answer = 0

    sheep = 0
    wolf = 0

    root = Node(0)
    for i in range(len(edges)):
        Node(edges[0]).left = Node(edges[1]) if Node(edges[0]).left == None or Node(edges[0]).left > edges[1] else Node(edges[0]).right = edges[1]

    print(Node)

    return answer

solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])