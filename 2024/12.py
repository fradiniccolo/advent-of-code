with open("12.txt") as _:
    puzzle_input = _.read().strip()


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
        self.get_region_perimeters()

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
            if x > 0:
                west_node = plots[(x-1, y)]
                node.neighbours.append(west_node)
            if x < self.size-1:
                east_node = plots[(x+1, y)]
                node.neighbours.append(east_node)
            if y > 0:
                north_node = plots[(x, y-1)]
                node.neighbours.append(north_node)
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

    def get_region_perimeters(self):
        for region in self.regions:
            perimeter = 0
            for plot in region.plots:
                plot_perimeter = 4
                for neighbour in plot.neighbours:
                    if neighbour.plant == plot.plant:
                        plot_perimeter -= 1
                perimeter += plot_perimeter
            region.perimeter = perimeter


class Region:

    def __init__(self, plant, seed_plot):
        self.plant = plant
        self.plots = [seed_plot]
        self.area = 1
        self.perimeter = 4
        self.setup()

    def setup(self):
        pass


class Plot:

    def __init__(self, coords, plant):
        self.x, self.y = coords
        self.plant = plant
        self.neighbours = []
        self.region = None


garden_map = Garden(puzzle_input)

print(sum([region.area*region.perimeter for region in garden_map.regions]))
