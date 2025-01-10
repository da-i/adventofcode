#!/bin/python3
from dataclasses import dataclass

import numpy as np
from itertools import product

@dataclass
class Point:
    x: int 
    y: int 


def read_input(file_path="day9/input/input.txt"):
    with open(file_path, "r") as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
        signal = [list(x) for x in lines]
        signal = np.array(signal, dtype="int8")
    return signal


def find_minima(mat):
    vallies = []
    matrix_max_x = mat.shape[0]
    matrix_max_y = mat.shape[1]
    for x, y in product(range(matrix_max_x), range(matrix_max_y)):
        vally = True
        val = mat[x][y]
        for nx, ny in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # fix the edges
            if x == 0 and nx == -1:
                continue
            elif y == 0 and ny == -1:
                continue
            elif x == matrix_max_x -1 and nx == 1:
                continue
            elif y == matrix_max_y -1 and ny == 1:
                continue
            # compare to neighborg
            neighborg = mat[x + nx][y + ny]
            if val >= neighborg:
                vally = False
                break
        if vally:
            vallies.append((x, y))
    return vallies


def find_solution1(minima, mat):

    solution = 0
    for min in minima:
        solution += mat[min[0]][min[1]]
        solution += 1
    print(solution)

def get_neigbourgs(x,y):
    
    targets = [(x -1, y),
            (x + 1, y),
            (x,  y -1),
            (x,  y +1)]
    return targets


def calculcate_basin_size(point, height_map):
    size = 0
    if (point.x >= 0
        and point.y >= 0
        and point.y < len(height_map)
        and point.x < len(height_map[point.y])):
        if height_map[point.y][point.x] < 9:
            size = 1
            height_map[point.y][point.x] = 9
            size += calculcate_basin_size(Point(point.x - 1, point.y),
                                          height_map)
            size += calculcate_basin_size(Point(point.x + 1, point.y),
                                          height_map)
            size += calculcate_basin_size(Point(point.x, point.y - 1),
                                          height_map)
            size += calculcate_basin_size(Point(point.x, point.y + 1),
                                          height_map)
    return size

def main():
    signal = read_input("day9/input/input.txt")
    minima = find_minima(signal)
    print(minima)
    find_solution1(minima, signal)
    basin_size = [calculcate_basin_size(Point(x[0],x[1]), signal) for x in minima]
    basin_size.sort()
    print(basin_size[-1]*basin_size[-2]*basin_size[-3])

if __name__ == "__main__":
    main()
