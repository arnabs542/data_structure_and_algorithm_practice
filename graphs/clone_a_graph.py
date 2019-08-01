class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

root = Node(1, [])
node2 = Node(2, [])
node3 = Node(3, [])
node4 = Node(4, [])
root.neighbors = [node2, node3]
node2.neighbors = [root, node4]
node3.neighbors = [root, node4]
node4.neighbors = [node2, node3]


def bfs(root):
    if root == None:
        return None

    seen = set([root])
    queue = [root]

    while len(queue) > 0:
        current_node = queue.pop()
        print(current_node.val)

        for neighbor in current_node.neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.insert(0, neighbor)

bfs(root)
