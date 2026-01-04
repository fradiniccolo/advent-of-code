with open("07e.txt", encoding="utf-8") as f:
    puzzle_input = f.read().strip()

# print(puzzle_input)

width = len(puzzle_input.splitlines()[0])
height = len(puzzle_input.splitlines())

room_map = {}
for index, char in enumerate(puzzle_input.replace("\n", "")):
    x = index % width
    y = index // width
    room_map[(x, y)] = char

entrance = [pos for pos, char in room_map.items() if char == "S"][0]
splitters = [pos for pos, char in room_map.items() if char == "^"]


class Node:
    
    def __init__(self, position):
        self.position = position
        self.children = self.add_children()
    
    def __repr__(self):
        return f"Node({self.position})"

    def add_children(self):
        children = []
        x, y = self.position
        if (x, y + 1) in room_map.keys():
            if room_map[(x, y + 1)] != "^":
                return [Node((x, y + 1))]
            else:
                return [Node((x - 1, y + 1)), Node((x + 1, y + 1))]
        return children

head = Node(entrance)

from collections import deque
def bfs(root):
    if not root:
        return []
        
    result = []
    visited = set()
    splits = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node.position in visited:
            continue
        visited.add(node.position)
        result.append(node.position)
        if len(node.children) > 1:
            splits.append(node.position)
        
        for child in node.children:
            queue.append(child)
    
    return result, splits

result, splits = bfs(head)
print(len(set(splits)))
print(len(splits)+1)
