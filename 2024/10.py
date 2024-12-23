from pprint import pprint

with open("10.txt") as _:
    puzzle_input = _.read().strip()


class Node:

    def __init__(self, value):
        self.value = value
        self.connections = []

    def __str__(self):
        return f"Node(value={self.value}, conns={[c.value for c in self.connections]})"

    def __repr__(self):
        return f"Node(value={self.value}, conns={[c.value for c in self.connections]})"
    
class Trailer:
    
    def __init__(self, head):
        self.head = head
        self.tails = set()
        self.find_tails(self.head)
        self.trailer_score = len(self.tails)

    
    def find_tails(self, current_node):
        if current_node.value == 9:
            self.tails.add(current_node)
        else:
            for connected_node in current_node.connections:
                self.find_tails(connected_node)

    def __str__(self):
        return f"Trailer(head={self.head})"

    def __repr__(self):
        return f"Trailer(head={self.head})"


class Topomap:

    def __init__(self, text):
        self.matrix = [[int(char) for char in row] for row in text.split('\n')]
        self.size = len(self.matrix)  # maps are square
        self.nodes = {}
        self.setup()
        self.map_score = 0
        self.get_map_score()
    
    def setup(self):
        for row_idx, row in enumerate(self.matrix):
            for col_idx, value in enumerate(row):
                self.nodes[(col_idx, row_idx)] = Node(value)
        for (x, y), node in self.nodes.items():
            if x > 0:
                west_node = self.nodes[(x-1, y)]
                if west_node.value - node.value == 1:
                    node.connections.append(west_node)
            if x < self.size-1:
                east_node = self.nodes[(x+1, y)]
                if east_node.value - node.value == 1:
                    node.connections.append(east_node)
            if y > 0:
                north_node = self.nodes[(x, y-1)]
                if north_node.value - node.value == 1:
                    node.connections.append(north_node)
            if y < self.size-1:
                south_node = self.nodes[(x, y+1)]
                if south_node.value - node.value == 1:
                    node.connections.append(south_node)


    def get_trailers(self):
        trailheads = [node for node in self.nodes.values() if node.value == 0]
        return [Trailer(trailhead) for trailhead in trailheads]


    def get_map_score(self):
        for trailer in self.get_trailers():
            self.map_score += trailer.trailer_score
    
topomap = Topomap(puzzle_input)
pprint(topomap.matrix)
# print(topomap.size)
# pprint(topomap.nodes)
print(topomap.map_score)
