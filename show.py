# Libraries
import turtle
import numpy as np
from aco_tsp import SolveTSPUsingACO
from sklearn.preprocessing import MinMaxScaler
from time import sleep

# Reading location dataset
# Filename - location_ll.txt
location = []
lats = []
lons = []
f = open('tsp dataset/location_ll.txt', 'r')
for line in f.readlines():
    lat_lon = tuple(map(float, line.split('\t')))
    location.append(list(map(float, line.split('\t'))))
location = np.array(location)

# Scaling dataset
scaler = MinMaxScaler(feature_range=(-90, 175))
location[:, 1] = scaler.fit_transform(location[:, 1].reshape(-1, 1)).reshape(1, -1)
scaler = MinMaxScaler(feature_range=(-80, 75))
location[:, 0] = scaler.fit_transform(location[:, 0].reshape(-1, 1)).reshape(1, -1)

# Main
if __name__ == '__main__':

    # Parameters
    _colony_size = 15
    _steps = 50
    _nodes = location

    # Model
    acs = SolveTSPUsingACO(mode='ACS', colony_size=_colony_size, steps=_steps, nodes=_nodes)
    time, dist = acs.run()
    route = acs.global_best_tour
    print('Runtime: ', time, 's')
    print('Minimum distance: ', dist)

    screen = turtle.Screen()
    screen.setup(1253, 755)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('./assets/map.png')

    loc = turtle.Turtle()
    # sleep(10)
    loc.shape('circle')
    loc.color('green')
    loc.penup()
    start = _nodes[route[0]]
    loc.goto(*start[::-1])
    loc.dot(30)
    loc.color('blue')
    loc.pendown()
    for idx in route[1:len(route)-1]:
        [lat, lon] = _nodes[idx]
        loc.goto(lon, lat)
        loc.dot(5)

    end = _nodes[route[len(route)-1]]
    loc.goto(*end[::-1])
    loc.color('red')
    loc.dot(30)
    loc.hideturtle()
    screen.exitonclick()
