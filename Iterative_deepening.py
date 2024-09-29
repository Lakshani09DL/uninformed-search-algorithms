class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def iterative_deepening_search(rootnode, goal):
    depth_limit = 0
    while True:
        result = depth_limited_search(rootnode, goal, depth_limit)
        if result is not None:
            return result
        depth_limit += 1


def depth_limited_search(node, goal, depth):
    if depth == 0 and node.value == goal:
        return node
    if depth > 0:
        for child in node.children:
            result = depth_limited_search(child, goal, depth - 1)
            if result is not None:
                return result
    return None


if __name__ == '__main__':
    root = Node(1)
    child1 = Node(2)
    child2 = Node(3)
    root.children = [child1, child2]
    child1.children = [Node(4), Node(5)]
    child2.children = [Node(6), Node(7)]

    goal_node = iterative_deepening_search(root, 5)
    if goal_node:
        print(f"Goal found: {goal_node.value}")
    else:
        print("Goal not found.")
