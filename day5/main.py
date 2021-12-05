from dataclasses import dataclass
from itertools import product
from typing import List, Tuple
import numpy as np


def read_input(file_path="day5/input/input.txt"):
    with open(file_path, "r") as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]

    return lines


@dataclass
class ThermalVentMap:
    map: np.array
    lines: list
    straight_lines = []
    diag_lines = []

    def find_stright_lines(self):
        for line in self.lines:
            # formatted as [[x1,y1],[x2,y2]]
            # if we have a straight line
            if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
                self.straight_lines.append(line)

    def find_diag_lines(self):
        for line in self.lines:
            hori_movement = abs(line[0][0] - line[1][0])
            vert_movement = abs(line[0][1] - line[1][1])
            if hori_movement == vert_movement:
                self.diag_lines.append(line)

            # coords_start = line[0]
            # coords_start_move = max(coords_start) - min(coords_start)

            # coords_end = line[1]
            # coords_end_move = max(coords_end) - min(coords_end)

            # if coords_start_move == coords_end_move:
            #     self.diag_lines.append(line)

    def update_map(self):
        for line in self.straight_lines:
            # create a list of x and y coords one will be of length 1.
            x_coords = line[0][0], line[1][0]
            y_coords = line[0][1], line[1][1]
            range_x = list(range(min(x_coords), max(x_coords) + 1))
            range_y = list(range(min(y_coords), max(y_coords) + 1))
            # loop over all combinations
            for pos in list(product(range_x, range_y)):
                if pos == (0, 9):
                    print("")

                self.map[pos[0]][pos[1]] += 1

        # these two loops could be merged by smarter assignment of ranges
        for line in self.diag_lines:
            x_coords = line[0][0], line[1][0]
            y_coords = line[0][1], line[1][1]
            range_x = list(range(min(x_coords), max(x_coords) + 1))
            range_y = list(range(min(y_coords), max(y_coords) + 1))

            if x_coords[0] > x_coords[1]:
                range_x.reverse()
            if y_coords[0] > y_coords[1]:
                range_y.reverse()

            for pos in zip(range_x, range_y):
                self.map[pos[0]][pos[1]] += 1

    def find_dangerous_locations(self, danger_level=1):
        return self.map > danger_level

    def find_solution1(self):
        danger_locs = self.find_dangerous_locations()
        print(np.count_nonzero(danger_locs))


Coords = Tuple[Tuple[int], Tuple[int]]


def clean_input(inputs: List[str], from_to_spitter: str = "->") -> List[Coords]:
    coords = []
    for line in inputs:
        coords_line = line.split(from_to_spitter)
        if len(coords_line) > 2:
            raise IOError("The input contains lines with more than 2 coordinates")
        coords_line = [process_location_string(x) for x in coords_line]
        coords.append(coords_line)
    return coords


def process_location_string(loc_str):
    loc = loc_str.split(",")
    loc = [int(x) for x in loc]
    return loc


def main():
    input = read_input("day5/input/input.txt")
    coordinates = clean_input(input)

    vent_map = ThermalVentMap(np.zeros((1000, 1000)), coordinates)
    vent_map.find_stright_lines()
    vent_map.update_map()
    print("solution 1:")
    vent_map.find_solution1()

    print("solution 2:")
    vent_map2 = ThermalVentMap(np.zeros((1000, 1000)), coordinates)
    # vent_map2.find_stright_lines()
    vent_map2.find_diag_lines()
    vent_map2.update_map()
    vent_map2.find_solution1()

    pass


if __name__ == "__main__":
    main()
