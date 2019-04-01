# Libraries
from aco_tsp import SolveTSPUsingACO

# Reading location dataset
# Filename - location_ll.txt
location = []
f = open('tsp dataset/location_ll.txt', 'r')
for line in f.readlines():
    location.append(tuple(map(float, line.split('\t'))))

# Main
if __name__ == '__main__':

    # Parameters
    _colony_size = 5
    _steps = 50
    _nodes = location
    # print(len(_nodes))
    # print(_nodes)

    # Model
    acs = SolveTSPUsingACO(mode='ACS', colony_size=_colony_size, steps=_steps, nodes=_nodes)
    time, dist = acs.run()
    route = acs.global_best_tour
    print('Runtime: ', time, 's')
    print('Minimum distance: ', dist)
    print('Route: ', '->'.join(list(map(str, route))))
