from typing import Counter
import statistics
import math
import numpy as np

def read_input(file_path="day7/input/input.txt"):
    with open(file_path, "r") as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
        lines = lines[0].split(",")
        lines = [int(x) for x in lines]
    return lines


def main():
    # input = read_input("day7/input/test_input.txt")
    input = read_input()
    # might need to floor or ceil????
    median = round(statistics.median(input))
    movement = [abs(median-x) for x in input]
    print(sum(movement))

    mean = statistics.mean(input)
    mean = round(mean)
    arr = np.array(input)
    dists = np.absolute(arr - mean)
    # from the example:
    # ((16-5)**2 + (16-5)) /2
    # (abs(1-5)**2 + abs(1-5)) /2
    #  looked it up before committing: triagulair numbers
    distance = np.sum((dists ** 2 + dists)/2)
    print(distance)

if __name__ == "__main__":
    main()
