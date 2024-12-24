with open("12e.txt") as _:
    puzzle_input = _.read().strip()

from pprint import pprint
    
class Garden:
    
    def __init__(self, map_text):
        self.size = None  # square
        self.plots = {}
        self.regions = []  # one to many
        self.setup(map_text)
        
    def setup(self, text):
        self.get_plots_from_text(text)
        self.get_neighbouring_plots()
        self.get_regions()
        
    def get_plots_from_text(self, text):
        rows = text.split('\n')
        self.size = len(rows)
        for y, row in enumerate(rows):
            for x, char in enumerate(row):
                self.plots[(x, y)] = Plot((x, y), char)
    
    def get_neighbouring_plots(self):
        for (x, y), node in self.plots.items():
            if x > 0:
                west_node = self.plots[(x-1, y)]
                node.neighbours.append(west_node)
            if x < self.size-1:
                east_node = self.plots[(x+1, y)]
                node.neighbours.append(east_node)
            if y > 0:
                north_node = self.plots[(x, y-1)]
                node.neighbours.append(north_node)
            if y < self.size-1:
                south_node = self.plots[(x, y+1)]
                node.neighbours.append(south_node)
    
    def get_regions(self):
                
        for plot in self.plots.values():
            
            if not self.regions:
                self.regions.append([plot])
            
            else:
                found = False
                for region in self.regions:
                    if any([plot.plant == region_plot.plant for region_plot in region]):
                        # if any([plot in region_plot.neighbours for region_plot in region]):
                        region.append(plot)
                        found = True
                        break
                if not found:
                    self.regions.append([plot])
            
            

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
        self.setup()
    
    def __repr__(self):
        neighbours = ', '.join([neighbour.plant for neighbour in self.neighbours])
        return f"Plot(plant={self.plant}, coords={(self.x, self.y)}, neighbours=({neighbours}))"
    
    def setup(self):
        pass

print(puzzle_input)

garden_map = Garden(puzzle_input)
# for plot in garden_map.plots.values():
#     print(plot)

for region in garden_map.regions:
    print(region[0].plant, len(region))
    # pprint(region)

# scan map plot by plot
# determine each plot neighbours

# use tree nodes to determine regions (one-to-many)
#     what is the key/id?
# get area by counting plots in region
# get perimeter by counting all not connected edges