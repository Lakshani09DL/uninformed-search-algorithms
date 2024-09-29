class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def depth_limited_search(node, goal, limit, path=[]):
    path.append(node.value)
    if limit < 0:
        return None

    if node.value == goal:
        return path

    for child in node.children:
        result_path = depth_limited_search(child, goal, limit - 1, path.copy())
        if result_path is not None:
            return result_path
    return None


if __name__ == '__main__':
    root = Node(1)
    child1 = Node(2)
    child2 = Node(3)
    child1.children.append(Node(4))
    child1.children.append(Node(5))
    child2.children.append(Node(6))
    child2.children.append(Node(7))
    root.children.append(child1)
    root.children.append(child2)

    depth_limit = 2
    goal_node = 5

    result = depth_limited_search(root, goal_node, depth_limit)

    if result is not None:
        print(f"Path to {goal_node}: {result}")
    else:
        print(f"Node {goal_node} not found within depth limit.")
