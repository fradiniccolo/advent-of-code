class Maze:

    def __init__(self, file):
        self.start_node = None
        self.nodes = []
        self.end_node = None
        self.paths = []
        self.initialise(file)

    def initialise(self, file):

        # build all nodes
        for y, row in enumerate(file.split('\n')):
            for x, char in enumerate(row):
                if char == 'S':
                    self.start_node = Node(x, y, self)
                    self.nodes.append(self.start_node)
                elif char == 'E':
                    self.end_node = Node(x, y, self)
                    self.nodes.append(self.end_node)
                elif char == '.':
                    self.nodes.append(Node(x, y, self))

        # connect all nodes recursively
        self.start_node.connect()

        # find all paths
        self.paths.append(Path(self.start_node))
        while any([path.is_winner is None for path in self.paths]):
            for path in self.paths:
                path.explore()


class Node:

    def __init__(self, x, y, maze):
        self.x = x
        self.y = y
        self.connected_to = []
        self.maze = maze

    def __str__(self):
        return f"Node{self.x, self.y}"

    def __repr__(self):
        return f"Node{self.x, self.y}"

    def connect(self):
        if self.connected_to:
            return
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            for node in self.maze.nodes:
                if (self.x+dx, self.y+dy) == (node.x, node.y):
                    self.connected_to.append(node)
                    node.connect()


class Path:

    def __init__(self, start):
        self.nodes = [start]
        self.cost = 0
        self.costs = [0]
        self.is_winner = None
        self.maze = start.maze

    def __repr__(self):
        nodes = [f"({node.x}, {node.y}):{cost}"
                 for node, cost in zip(self.nodes, self.costs)]
        return f"Path(\n    {'\n  → '.join(nodes)})"

    def explore(self):

        if not self.is_winner is None:
            return

        # did path reach the end?
        head = self.nodes[-1]
        if head == self.maze.end_node:
            self.is_winner = True
            return

        # did path reach a fork?
        next_nodes = [
            node for node in head.connected_to
            if node not in self.nodes]

        # dead end
        if not next_nodes:
            # self.maze.paths.remove(self)
            self.is_winner = False
            return

        for index, next_node in enumerate(next_nodes):
            if index == len(next_nodes)-1:
                # extend current path
                self.nodes.append(next_node)
                self.update_cost()
            else:
                # initiate new paths
                new_path = self.copy()
                new_path.nodes.append(next_node)
                new_path.update_cost()
                self.maze.paths.append(new_path)

    def update_cost(self):

        def are_nodes_aligned(nodes):

            if len(nodes) == 3:
                node0, node1, node2 = nodes
                vector0 = (node1.x-node0.x, node1.y-node0.y)
                vector1 = (node2.x-node1.x, node2.y-node1.y)
                if vector0 == vector1:
                    return True
                return False

            else:
                node1, node2 = nodes
                vector1 = (node2.x-node1.x, node2.y-node1.y)
                if vector1 == (1, 0):
                    return True
                return False

        last_nodes = self.nodes[-3:]  # that's 2 or 3 nodes

        if are_nodes_aligned(last_nodes):
            self.cost += 1
            self.costs.append(1)
        else:
            self.cost += 1000
            self.costs.append(1000)

    def copy(self):
        new_path = Path(self.maze.start_node)  # ugly
        new_path.nodes = self.nodes[:]
        new_path.cost = self.cost
        new_path.maze = self.maze
        return new_path


with open("16e.txt") as _:
    puzzle_input = _.read().strip()

maze = Maze(puzzle_input)

min_path = min([path for path in maze.paths if path.is_winner],
               key=lambda path: path.cost)

print(min_path)
print(min_path.cost)
