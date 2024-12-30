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

        # find all paths recursively
        self.paths.append(Path(self.start_node))
        self.paths[0].explore()


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
        self.is_winner = None
        self.costs = [0]
        self.maze = start.maze

    def __repr__(self):
        nodes = [f"({node.x}, {node.y}):{cost}"
                 for node, cost in zip(self.nodes, self.costs)]
        return f"Path(\n    {'\n  → '.join(nodes)}\n)"

    def get_total_cost(self):
        return sum(self.costs)

    def add_node(self, node):
        self.nodes.append(node)
        self.update_cost()

    def explore(self):

        if self.is_winner is not None:
            return

        # did path reach the end?
        head_node = self.nodes[-1]
        if head_node == self.maze.end_node:
            self.is_winner = True
            return

        # did path reach a fork?
        next_nodes = [
            node for node in head_node.connected_to
            if node not in self.nodes]

        # dead end
        if not next_nodes:
            self.is_winner = False
            return

        for index, next_node in enumerate(next_nodes):
            if index != len(next_nodes)-1:
                # initiate new paths by copying current path
                new_path = self.copy()
                new_path.add_node(next_node)
                new_path.explore()
                self.maze.paths.append(new_path)
            else:
                # lastly, extend current path
                self.add_node(next_node)
                self.explore()

    def update_cost(self):

        def are_nodes_aligned(nodes):

            if len(nodes) == 3:
                node0, node1, node2 = nodes
                vector0 = (node1.x-node0.x, node1.y-node0.y)
                vector1 = (node2.x-node1.x, node2.y-node1.y)

            else:
                node1, node2 = nodes
                vector1 = (node2.x-node1.x, node2.y-node1.y)
                vector0 = (1, 0)

            if vector0 == vector1:
                return True
            return False

        self.costs.append(1)
        if not are_nodes_aligned(self.nodes[-3:]):
            self.costs.append(1000)

    def copy(self):
        new_path = Path(self.maze.start_node)  # ugly
        new_path.nodes = self.nodes[:]
        new_path.is_winner = self.is_winner
        new_path.costs = self.costs[:]
        new_path.maze = self.maze
        return new_path


with open("16e.txt") as _:
    puzzle_input = _.read().strip()

maze = Maze(puzzle_input)

winning_paths = [path for path in maze.paths if path.is_winner]
best_path = min(winning_paths, key=lambda path: path.get_total_cost())

print(best_path)
print(best_path.get_total_cost())
