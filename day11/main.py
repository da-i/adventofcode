from typing import Counter
import statistics
import math
import numpy as np

DIFF_KERNEL = np.array(
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        )
STEPS = 100

def split(word):
    return [char for char in word]
     
def read_input(file_path="day11/input/input.txt"):
    with open(file_path, "r") as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
        # lines = lines[0].split(",")
        lines = [split(x) for x in lines]
        array = np.array(lines, dtype="uint8")
    return array


def update_matrix(dumbo_octo, has_flashed, coords, XMAX , YMAX):
    if has_flashed[coords[0], coords[1]] == 1:
        return dumbo_octo, has_flashed

    x_low = coords[0] - 1 if coords[0] > 0 else 0
    x_high = coords[0] + 1 if coords[0] <= XMAX else XMAX
    y_low = coords[1] - 1 if coords[1] > 0 else 0
    y_high = coords[1] + 1 if coords[1] <= YMAX else YMAX
    # its up to, not until in slicing
    x_high += 1
    y_high += 1
    #  add one to all neighborgs
    dumbo_octo[x_low:x_high, y_low:y_high] += 1
    # set self to 0
    dumbo_octo[coords[0]][coords[1]] = 0
    has_flashed[coords[0]][coords[1]] = 1
    # print(dumbo_octo)
    # print(coords)
    # print(dumbo_octo[0][0])
    # print(dumbo_octo[x_low:x_high, y_low:y_high])

    return dumbo_octo, has_flashed


def main():
    # dumbo_octo = read_input("day11/input/test_input.txt")
    dumbo_octo = read_input()
    flashes = 0
    for i in range(STEPS):
        print(i)
        # print(dumbo_octo)
        dumbo_octo += 1
        substep = 0
        lights = np.where(dumbo_octo > 9)
        # print(f"\t{i}-i: found {len(lights[0])} initial lightpoints!")
        has_flashed = np.zeros(dumbo_octo.shape)
        while len(lights[0]) > 0:
            for light in zip(lights[0], lights[1]):
                dumbo_octo, has_flashed = update_matrix(dumbo_octo, has_flashed, light, 10, 10) #TODO update shape                
                flashes += 1
            lights = np.where(dumbo_octo > 9)
            # print(f"\t{i}-{substep}: found {len(lights[0])} new lightpoints!")
            substep += 1
        # print(has_flashed)
        dumbo_octo[has_flashed == 1] = 0
    print('solution 1:')
    print(flashes)
    
    i = 0
    dumbo_octo = read_input()
    # dumbo_octo = read_input("day11/input/test_input.txt")
    while True:
        i += 1
        print(i)
        dumbo_octo += 1

        has_flashed = np.zeros(dumbo_octo.shape)
        lights = np.where(dumbo_octo > 9)
        has_flashed = np.zeros(dumbo_octo.shape)
        while len(lights[0]) > 0:
            for light in zip(lights[0], lights[1]):
                dumbo_octo, has_flashed = update_matrix(dumbo_octo, has_flashed, light, 10, 10) #TODO update shape                
                flashes += 1
            lights = np.where(dumbo_octo > 9)
        dumbo_octo[has_flashed == 1] = 0
        if np.sum(has_flashed) == 100:
            break

    print('solution 2:')
    print(i)







if __name__ == "__main__":
    main()
