from pathlib import Path
import numpy as np


def read_input(file_path="input/input.txt"):
    with open(file_path, "r") as f:
        lines = f.readlines()
        lines = [int(x.strip()) for x in lines]
    return lines


def solve_problem1(radar_output):
    diff = np.diff(radar_output)
    positives = np.where(diff > 0)[0]
    print(f"solution 1 : {len(positives)}")


def solve_problem2(radar_output, rollers=[0, -1, -2]):
    rolled_values = [np.roll(radar_output, x) for x in rollers]
    sums = np.sum(rolled_values, axis=0)
    diff = np.diff(sums)
    positives = np.where(diff > 0)[0]
    print(f"solution 2: {len(positives)}")


def main():
    radar_output = read_input()
    solve_problem1(radar_output)

    solve_problem2(radar_output)


if __name__ == "__main__":
    main()
