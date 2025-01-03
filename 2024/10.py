with open("10.txt") as _:
    puzzle_input = _.read().strip()


class Node:

    def __init__(self, value):
        self.value = value
        self.reachable_nodes = []


class Trailer:

    def __init__(self, head):
        self.head = head
        self.tails = set()
        self.rating = 0
        self.find_tails(self.head)
        self.score = len(self.tails)

    def find_tails(self, current_node):
        if current_node.value == 9:
            self.tails.add(current_node)
            self.rating += 1
        else:
            for connected_node in current_node.reachable_nodes:
                self.find_tails(connected_node)


class Topomap:

    def __init__(self, text):
        self.matrix = [[int(char) for char in row] for row in text.split('\n')]
        self.size = len(self.matrix)  # maps are square
        self.nodes = {}
        self.setup()
        self.map_score = 0
        self.map_rating = 0
        self.get_map_score_and_rating()

    def setup(self):
        for row_idx, row in enumerate(self.matrix):
            for col_idx, value in enumerate(row):
                self.nodes[(col_idx, row_idx)] = Node(value)
        for (x, y), node in self.nodes.items():
            if x > 0:
                west_node = self.nodes[(x-1, y)]
                if west_node.value - node.value == 1:
                    node.reachable_nodes.append(west_node)
            if x < self.size-1:
                east_node = self.nodes[(x+1, y)]
                if east_node.value - node.value == 1:
                    node.reachable_nodes.append(east_node)
            if y > 0:
                north_node = self.nodes[(x, y-1)]
                if north_node.value - node.value == 1:
                    node.reachable_nodes.append(north_node)
            if y < self.size-1:
                south_node = self.nodes[(x, y+1)]
                if south_node.value - node.value == 1:
                    node.reachable_nodes.append(south_node)

    def get_trailers(self):
        trailheads = [node for node in self.nodes.values() if node.value == 0]
        return [Trailer(trailhead) for trailhead in trailheads]

    def get_map_score_and_rating(self):
        for trailer in self.get_trailers():
            self.map_score += trailer.score
            self.map_rating += trailer.rating


topomap = Topomap(puzzle_input)
print(topomap.map_score)
print(topomap.map_rating)
