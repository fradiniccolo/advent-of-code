with open("12e.txt") as _:
    puzzle_input = _.read().strip()

from pprint import pprint


class Garden:

    def __init__(self, map_text):
        self.size = None  # square
        self.plots = None
        self.regions = None
        self.setup(map_text)

    def setup(self, input):
        self.get_plots_from_input(input)
        self.get_regions()

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

        def assign_region(plot):
            
            # assign region to plot
            region_found = False
            
            if self.regions is None:
                region = Region(plot.plant, plot)
                self.regions = [region]
                region_found = True
            
            else:
                for region in self.regions:
                    if plot.plant == region.plant:
                        if any([plot == neighbour
                                for region_plot in region.plots 
                                for neighbour in region_plot.neighbours]):
                            region_found = True
                            break
            
            if not region_found:
                region = Region(plot.plant, plot)
                self.regions.append(region)

            plot.region = region


            # check plot's neighbours
            for neighbour in plot.neighbours:
                if neighbour in spare_plots:
                    if plot.plant == neighbour.plant:
                        neighbour.region = plot.region
                        index = spare_plots.index(neighbour)
                        plot.region.plots.append(spare_plots.pop(index))
                

        spare_plots = [plot for plot in self.plots]

        while spare_plots:
            assign_region(spare_plots.pop(0))


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
        self.setup()

    def __repr__(self):
        neighbours = ', '.join(
            [neighbour.plant for neighbour in self.neighbours])
        return f"Plot(plant={self.plant}, coords={(self.x, self.y)}, neighbours=({neighbours}))"

    def setup(self):
        pass


print(puzzle_input)

garden_map = Garden(puzzle_input)
# for plot in garden_map.plots.values():
#     print(plot)

for map_region in garden_map.regions:
    print(map_region.plant, len(map_region.plots))
    # pprint(region)

# scan map plot by plot
# determine each plot neighbours

# use tree nodes to determine regions (one-to-many)
#     what is the key/id?
# get area by counting plots in region
# get perimeter by counting all not connected edges
