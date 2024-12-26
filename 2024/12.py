class Garden:

    def __init__(self, map_text):
        self.size = None  # square
        self.plots = []
        self.regions = []
        self.setup(map_text)

    def setup(self, input):
        self.get_plots_from_input(input)
        self.get_regions()
        self.get_region_areas()
        self.get_region_perimeters_and_sides()

    def get_plots_from_input(self, text):

        # get plots
        rows = text.split('\n')
        self.size = len(rows)
        plots = {}
        for y, row in enumerate(rows):
            for x, char in enumerate(row):
                plots[(x, y)] = Plot((x, y), char)

        # assign neighbours to plots
        for (x, y), node in plots.items():

            east_node = Plot((x+1, y), None)
            if x < self.size-1:
                east_node = plots[(x+1, y)]
            node.neighbours.append(east_node)

            north_node = Plot((x, y-1), None)
            if y > 0:
                north_node = plots[(x, y-1)]
            node.neighbours.append(north_node)

            west_node = Plot((x-1, y), None)
            if x > 0:
                west_node = plots[(x-1, y)]
            node.neighbours.append(west_node)

            south_node = Plot((x, y+1), None)
            if y < self.size-1:
                south_node = plots[(x, y+1)]
            node.neighbours.append(south_node)

        self.plots = list(plots.values())

    def get_regions(self):

        def make_region(plot):

            # initialise region
            region = Region(plot.plant, plot)
            self.regions.append(region)
            plot.region = region

            # check plot's neighbours
            def check_neighbours(plot):
                for neighbour in plot.neighbours:
                    if neighbour in spare_plots:
                        if neighbour.plant == plot.plant:
                            neighbour.region = plot.region
                            index = spare_plots.index(neighbour)
                            plot.region.plots.append(spare_plots.pop(index))
                            check_neighbours(neighbour)

            check_neighbours(plot)

        spare_plots = [plot for plot in self.plots]
        while spare_plots:
            make_region(spare_plots.pop(0))

    def get_region_areas(self):
        for region in self.regions:
            region.area = len(region.plots)

    def get_region_perimeters_and_sides(self):
        for region in self.regions:
            region.perimeter = 0
            horizontal_sides = []
            vertical_sides = []
            for plot in region.plots:
                for index, neighbour in enumerate(plot.neighbours):
                    if neighbour.plant != plot.plant:
                        region.perimeter += 1
                        if index % 2 != 0:
                            horizontal_sides.append(neighbour)
                        else:
                            vertical_sides.append(neighbour)

            horizontal_sides.sort(key=lambda plot: (plot.y, plot.x))
            horizontal_sides_count = 0
            last_x = -float('inf')
            last_y = -float('inf')
            for plot in horizontal_sides:
                if plot.x != last_x+1 or plot.y != last_y:
                    horizontal_sides_count += 1
                last_x = plot.x
                last_y = plot.y

            vertical_sides.sort(key=lambda plot: (plot.x, plot.y))
            vertical_sides_count = 0
            last_x = -float('inf')
            last_y = -float('inf')
            for plot in vertical_sides:
                if plot.y != last_y+1 or plot.x != last_x:
                    vertical_sides_count += 1
                last_x = plot.x
                last_y = plot.y

            region.sides = horizontal_sides_count + vertical_sides_count


class Region:

    def __init__(self, plant, seed_plot):
        self.plant = plant
        self.plots = [seed_plot]
        self.area = None
        self.perimeter = None
        self.sides = None


class Plot:

    def __init__(self, coords, plant):
        self.x, self.y = coords
        self.plant = plant
        self.neighbours = []
        self.region = None


with open("12.txt") as _:
    puzzle_input = _.read().strip()

garden_map = Garden(puzzle_input)

print(sum([region.area*region.perimeter for region in garden_map.regions]))

print(sum([region.area*region.sides for region in garden_map.regions]))
