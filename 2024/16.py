class Maze:

    def __init__(self, file):
        self.start_node = None
        self.nodes = []
        self.end_node = None
        self.initialise(file)

    def initialise(self, file):

        # build all nodes
        for y, row in enumerate(file.split('\n')):
            for x, char in enumerate(row):
                if char == 'S':
                    self.start_node = Node(x, y)
                    self.nodes.append(self.start_node)
                elif char == 'E':
                    self.end_node = Node(x, y)
                    self.nodes.append(self.end_node)
                elif char == '.':
                    self.nodes.append(Node(x, y))

        # connect all nodes
        coords_to_node = {(node.x, node.y): node for node in self.nodes}
        for node in self.nodes:
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                neighbour = coords_to_node.get((node.x+dx, node.y+dy))
                if neighbour:
                    node.connected_to.append(neighbour)

        # dijkstra's algorithm
        for node in self.nodes:
            node.explored = False
            node.cost = float('inf')
            node.prev = None
        self.start_node.cost = 0
        
        def get_step_cost(current, neighbour):
            
            previous = current.prev

            def are_nodes_aligned(previous, current, neighbour):
                if previous is None:
                    vector0 = (1, 0)
                else:
                    vector0 = (current.x-previous.x, current.y-previous.y)
                vector1 = (neighbour.x-current.x, neighbour.y-current.y)

                if vector0 == vector1:
                    return True
                return False

            if not are_nodes_aligned(previous, current, neighbour):
                return 1001
            return 1
        
        
        unexplored = self.nodes[:]
        while self.end_node in unexplored:
            current = min(unexplored)  # node of min cost
            unexplored.remove(current)
            for neighbour in current.connected_to:
                step_cost = get_step_cost(current, neighbour)
                if current.cost + step_cost < neighbour.cost:
                    neighbour.cost = current.cost + step_cost
                    neighbour.prev = current

class Node:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.connected_to = []
        self.cost = None
        self.dir = None
        self.prev = None

    def __str__(self):
        return f"Node{self.x, self.y}"

    def __repr__(self):
        return f"Node{self.x, self.y}"
    
    def __lt__(self, other):
        return self.cost < other.cost
    
with open("16e.txt") as _:
    puzzle_input = _.read().strip()

maze = Maze(puzzle_input)


path = [maze.end_node]
while True:
    if path[0].prev:
        path.insert(0, path[0].prev)
    else:
        break
for node in path:
    print(node, node.cost)
print()
print(maze.end_node.cost)
# 82460